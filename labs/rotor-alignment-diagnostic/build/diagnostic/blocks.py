"""Summary block: check the format, strip the name and role, fingerprint the name.

The block is the 17-line text the interviewer produces (see
rotor/interviewer-pack.md). A leader may edit what is written after each
label. The labels, their order, and the start and end lines must not change.

Nothing in this file stores anything. It takes text in and returns either a
BlockRejected (with a plain-language message) or the stripped text and a
fingerprint.
"""
from __future__ import annotations

import hmac
import hashlib
import re
import unicodedata
from dataclasses import dataclass

START = "=== ROTOR INTERVIEW SUMMARY ==="
END = "=== END SUMMARY ==="

LABELS = [
    "Company",
    "Leader",
    "Wave",
    "Date",
    "Main effort (their words)",
    "Trade-offs they named",
    "How they would resolve a collision between priorities",
    "Beliefs the plan rests on",
    "Early warning signs they named",
    "Friction (where work waits)",
    "Decisions that didn't stick",
    "Images, metaphors and sayings (exact words)",
    "Questions they want the leadership team to settle",
    "Corrections they made to the read-back",
    "Leave out of the summary",
]

LEADER = "Leader"
LEAVE_OUT = "Leave out of the summary"
MAIN_EFFORT = "Main effort (their words)"

REMOVED = "[removed]"

_PASTE_AGAIN = (
    " You can change what is written after each label, but the labels "
    "themselves must stay exactly as the interviewer wrote them. Please copy "
    "the block again from the interviewer, from the first === line to the "
    "last, and paste it here."
)


class BlockRejected(Exception):
    """The pasted text can't be accepted. str(exc) is safe to show the leader."""


@dataclass
class ParsedBlock:
    # one entry per label, in order; each entry is the list of lines for that
    # field, the first line being the "Label: ..." line itself
    fields: list[tuple[str, list[str]]]
    leader_name: str
    leader_role: str


# ---------------------------------------------------------------- parsing

_LABEL_LIKE = re.compile(r"^[A-Za-z][^:\n]{1,90}:(\s|$)")


def _known_label(line: str) -> str | None:
    s = line.lstrip()
    for label in LABELS:
        if s.startswith(label + ":"):
            return label
    return None


def parse_block(text: str) -> ParsedBlock:
    """Check the text holds exactly one well-formed block, or raise BlockRejected."""
    if not isinstance(text, str) or not text.strip():
        raise BlockRejected("Nothing was pasted. Please paste the whole summary block." + _PASTE_AGAIN)

    text = text.replace("\r\n", "\n").replace("\r", "\n").lstrip("﻿")
    lines = text.split("\n")
    starts = [i for i, l in enumerate(lines) if l.strip() == START]
    ends = [i for i, l in enumerate(lines) if l.strip() == END]

    if len(starts) > 1 or len(ends) > 1:
        raise BlockRejected(
            "More than one summary was pasted. Please send one summary at a "
            "time, with only one leader's block in the box."
        )
    if not starts:
        raise BlockRejected(
            f'The first line of the summary ("{START}") is missing.' + _PASTE_AGAIN
        )
    if not ends:
        raise BlockRejected(
            f'The last line of the summary ("{END}") is missing.' + _PASTE_AGAIN
        )
    if ends[0] < starts[0]:
        raise BlockRejected("The first and last lines of the summary are in the wrong order." + _PASTE_AGAIN)

    inner = lines[starts[0] + 1 : ends[0]]

    found: list[str] = []
    entries: list[list] = []  # [label, lines] in the order they appear
    current: list | None = None
    for raw in inner:
        line = raw.rstrip()
        if not line.strip():
            continue
        label = _known_label(line)
        if label is not None:
            found.append(label)
            current = [label, [line.lstrip()]]
            entries.append(current)
            continue
        if current is None:
            raise BlockRejected(
                "There is extra text between the first line and the first label."
                + _PASTE_AGAIN
            )
        s = line.lstrip()
        if not s.startswith(("-", "*", "•")) and _LABEL_LIKE.match(s):
            shown = s.split(":", 1)[0][:40]
            raise BlockRejected(
                f'The line starting "{shown}:" looks like a label that was '
                "added or changed." + _PASTE_AGAIN
            )
        current[1].append(line.lstrip())

    if found != LABELS:
        missing = [l for l in LABELS if l not in found]
        dupes = sorted({l for l in found if found.count(l) > 1})
        if missing:
            shown = ", ".join(f'"{m}:"' for m in missing[:3])
            more = "" if len(missing) <= 3 else f" and {len(missing) - 3} more"
            raise BlockRejected(
                f"These labels are missing or have been changed: {shown}{more}." + _PASTE_AGAIN
            )
        if dupes:
            raise BlockRejected(f'The label "{dupes[0]}:" appears more than once.' + _PASTE_AGAIN)
        raise BlockRejected("The labels are not in their original order." + _PASTE_AGAIN)

    fields = [(label, lines) for label, lines in entries]

    def value_of(label: str) -> str:
        first = dict(fields)[label][0][len(label) + 1 :].strip()
        rest = " ".join(dict(fields)[label][1:]).strip()
        return (first + " " + rest).strip()

    if not value_of(MAIN_EFFORT):
        raise BlockRejected(
            'The "Main effort (their words):" line is empty. The report needs '
            "at least that line filled in. Please check the summary and paste it again."
        )
    leader = value_of(LEADER)
    name, _, role = leader.partition(",")
    name, role = name.strip(), role.strip()
    if not name:
        raise BlockRejected(
            'The "Leader:" line should read "name, role". It is needed so '
            "the name can be removed. It is never stored."
        )
    return ParsedBlock(fields=fields, leader_name=name, leader_role=role)


# ---------------------------------------------------------------- stripping

_PARTICLES = {"de", "la", "le", "van", "von", "der", "den", "del", "di", "da", "du",
              "jr", "sr", "ii", "iii", "of", "the", "and", "st"}


def _fold_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def normalize_name(name: str) -> str:
    s = _fold_accents(unicodedata.normalize("NFKC", name)).casefold()
    s = re.sub(r"[^\w\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def fingerprint(name: str, salt: bytes) -> str:
    """One-way code for the normalized name. HMAC-SHA256 with a per-company secret salt."""
    return hmac.new(salt, normalize_name(name).encode("utf-8"), hashlib.sha256).hexdigest()


def _variants(s: str) -> list[str]:
    folded = _fold_accents(s)
    return [s] if folded == s else [s, folded]


def _phrase_pattern(phrase: str) -> str:
    parts = [re.escape(p) for p in phrase.split()]
    return r"(?<!\w)" + r"\s+".join(parts) + r"(?!\w)"


def _name_patterns(name: str, role: str) -> list[str]:
    pats: list[str] = []
    # longest first: the full name, the role, then single name parts
    for v in _variants(" ".join(name.split())):
        pats.append(_phrase_pattern(v))
    if role.strip():
        for v in _variants(" ".join(role.split())):
            pats.append(_phrase_pattern(v))
    tokens = [t for t in re.split(r"[\s\-]+", name) if t]
    for t in tokens:
        t = re.sub(r"^\W+|\W+$", "", t)
        if len(t) < 2 or t.casefold().rstrip(".") in _PARTICLES:
            continue
        for v in _variants(t):
            pats.append(r"(?<!\w)" + re.escape(v) + r"(?!\w)")
    return pats


def strip_identity(parsed: ParsedBlock) -> str:
    """Return the block text with name and role removed everywhere.

    The Leader value becomes "removed"; the Leave-out field becomes "none".
    """
    pats = [re.compile(p, re.IGNORECASE) for p in _name_patterns(parsed.leader_name, parsed.leader_role)]
    out = [START]
    for label, lines in parsed.fields:
        if label == LEADER:
            out.append(f"{LEADER}: removed")
            continue
        if label == LEAVE_OUT:
            out.append(f"{LEAVE_OUT}: none")
            continue
        for line in lines:
            for p in pats:
                line = p.sub(REMOVED, line)
            out.append(line)
    out.append(END)
    return "\n".join(out)


@dataclass
class Prepared:
    stripped_text: str
    fingerprint: str


def prepare_block(text: str, salt: bytes) -> Prepared:
    """Validate, strip, fingerprint. Raises BlockRejected. Stores nothing."""
    parsed = parse_block(text)
    return Prepared(strip_identity(parsed), fingerprint(parsed.leader_name, salt))
