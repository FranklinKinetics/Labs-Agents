"""Block parser, validator, name stripping (Check C format, Check B anonymity, T1 T3 T7 T8)."""
import re

import pytest

from conftest import REPO, LAB, larchmere_blocks
from diagnostic import blocks as B


def labels_in(text):
    return [l.split(":", 1)[0] for l in text.splitlines()[1:-1] if not l.startswith("-") and ":" in l]


# ---- Check C: the format matches the interviewer pack, by script -----------------

def _pack_block(path, after):
    t = path.read_text(encoding="utf-8")
    t = t[t.index(after):]
    m = re.search(r"(=== ROTOR INTERVIEW SUMMARY ===\n.*?\n=== END SUMMARY ===)", t, re.S)
    return m.group(1).splitlines()


def _expected_from_pack(lines):
    assert lines[0] == B.START and lines[-1] == B.END
    return [l.split(":", 1)[0] for l in lines[1:-1]]


def test_labels_match_interviewer_pack():
    pack = _pack_block(REPO / "rotor" / "interviewer-pack.md", "# Summary block format")
    assert len(pack) == 17                         # start + 15 fields + end
    assert _expected_from_pack(pack) == B.LABELS


def test_labels_match_diagnostic_interviewer():
    ours = _pack_block(LAB / "03-interviewer.md", "# Summary block format")
    assert len(ours) == 17
    assert _expected_from_pack(ours) == B.LABELS


def test_all_five_larchmere_blocks_are_valid():
    for b in larchmere_blocks():
        p = B.parse_block(b)
        assert [l for l, _ in p.fields] == B.LABELS


def test_edited_content_accepted(blocks5):
    edited = blocks5[0].replace("Win the Prairie Ag supply contract", "Win a supply contract: any one")
    edited = edited.replace("- Quotes take too long to get out", "- Quotes: slow\n- A third line I added")
    assert B.parse_block(edited).leader_name == "Dale Kowalchuk"


def test_text_around_the_block_is_ignored_and_not_kept(blocks5):
    p = B.prepare_block("Here you go!\n```\n" + blocks5[1] + "\n```\nThanks, Priya", b"s")
    assert "Here you go" not in p.stripped_text and "Thanks" not in p.stripped_text


# ---- T7: malformed blocks rejected with a plain message --------------------------

def _reject(text):
    with pytest.raises(B.BlockRejected) as e:
        B.parse_block(text)
    return str(e.value)


def test_T7_missing_end_line(blocks5):
    msg = _reject(blocks5[0].replace(B.END, ""))
    assert "last line" in msg


def test_T7_missing_start_line(blocks5):
    assert "first line" in _reject(blocks5[0].replace(B.START, ""))


def test_T7_missing_field(blocks5):
    msg = _reject(blocks5[0].replace("Wave: 1\n", ""))
    assert '"Wave:"' in msg


def test_T7_changed_label(blocks5):
    msg = _reject(blocks5[0].replace("Main effort (their words):", "Main effort:"))
    assert "Main effort" in msg and "changed" in msg


def test_T7_extra_field(blocks5):
    msg = _reject(blocks5[0].replace("Wave: 1\n", "Wave: 1\nMood: cheerful\n"))
    assert "Mood" in msg


def test_T7_reordered_fields(blocks5):
    lines = blocks5[0].splitlines()
    i, j = lines.index("Wave: 1"), next(k for k, l in enumerate(lines) if l.startswith("Date:"))
    lines[i], lines[j] = lines[j], lines[i]
    assert "order" in _reject("\n".join(lines))


def test_T7_two_blocks_at_once(blocks5):
    assert "More than one" in _reject(blocks5[0] + "\n\n" + blocks5[1])


def test_empty_main_effort_rejected(blocks5):
    text = re.sub(r"Main effort \(their words\): .*", "Main effort (their words):", blocks5[0])
    assert "Main effort" in _reject(text)


def test_empty_and_non_block_text():
    assert _reject("")
    assert _reject("hello there")


def test_no_label_like_line_in_messages_leaks_content(blocks5):
    # the message may name a label, but must not echo the leader's content
    msg = _reject(blocks5[0].replace("Wave: 1\n", "Wave: 1\nNote: Dale thinks this is secret\n"))
    assert "secret" not in msg


# ---- Name and role stripping (T1, T3, Check B) -----------------------------------

SALT = b"test-salt"


def stripped(text):
    return B.prepare_block(text, SALT).stripped_text


def test_leader_line_and_leave_out_replaced(blocks5):
    s = stripped(blocks5[1])
    assert "Leader: removed" in s
    assert "Leave out of the summary: none" in s
    assert "Items removed at the leader's request" not in s


def test_T1_name_in_the_body_removed(blocks5):
    t = blocks5[2].replace('"We sell like Costco and build like a jeweller."',
                           '"Marc here: we sell like Costco." and fontaine says so; MARC\'s view; Marc-ish')
    s = stripped(t)
    for bad in ("Marc", "Fontaine", "fontaine", "MARC"):
        assert bad.lower() not in s.lower().replace("[removed]", "")
    assert "[removed]" in s


def test_T3_leave_out_content_is_blanked(blocks5):
    t = blocks5[3].replace("Leave out of the summary: none",
                           "Leave out of the summary:\n- the pending sale of the east plant\n- Janet's health leave")
    s = stripped(t)
    assert "east plant" not in s and "health leave" not in s
    assert s.splitlines()[-2] == "Leave out of the summary: none"


def test_role_removed_everywhere(blocks5):
    t = blocks5[4].replace("- Customers will accept standard options if lead times drop",
                           "- As Engineering Lead I think customers will accept standard options")
    s = stripped(t)
    assert "engineering lead" not in s.lower()


def test_full_name_first_alone_last_alone_case_insensitive(blocks5):
    t = blocks5[0].replace("- Hard to find experienced welders",
                           "- Dale Kowalchuk and dale and KOWALCHUK and Kowalchuk's desk")
    s = stripped(t)
    assert not re.search(r"dale|kowalchuk", s, re.I)


def test_name_removal_respects_word_boundaries(blocks5):
    t = blocks5[3].replace("- Hold off on the new laser", "- Janetta and Janetsville and Janet")
    s = stripped(t)
    assert "Janetta" in s and "Janetsville" in s and "Janet" not in s.replace("Janetta", "").replace("Janetsville", "")


def test_accented_names():
    block = larchmere_blocks()[0].replace("Dale Kowalchuk, President and owner", "Léa Tremblay-Roy, Directrice")
    block = block.replace("- Hard to find experienced welders", "- Lea said so; Léa too; tremblay roy")
    s = B.prepare_block(block, SALT).stripped_text
    assert not re.search(r"\bl[eé]a\b|tremblay|\broy\b", s, re.I)


def test_leader_with_comma_in_role():
    block = larchmere_blocks()[0].replace("President and owner", "VP, Sales and Marketing")
    block = block.replace("- Hard to find experienced welders", "- As VP, Sales and Marketing I see delays")
    assert "vp, sales" not in B.prepare_block(block, SALT).stripped_text.lower()


def test_stripped_text_is_still_a_valid_block(blocks5):
    # what is stored can be handed to the agent, and is the 17-line shape
    for b in blocks5:
        s = stripped(b)
        assert s.splitlines()[0] == B.START and s.splitlines()[-1] == B.END
        assert [l for l in labels_in(s) if l in B.LABELS] == B.LABELS


# ---- Fingerprint (T8 uses it end to end in test_app) -----------------------------

def test_fingerprint_is_one_way_and_normalized():
    a = B.fingerprint("Dale Kowalchuk", SALT)
    assert a == B.fingerprint("  dale   KOWALCHUK. ", SALT)
    assert a != B.fingerprint("Dale Kowalchuk", b"another-salt")
    assert a != B.fingerprint("Dale Kowalchu", SALT)
    assert "dale" not in a.lower() and len(a) == 64


def test_fingerprint_ignores_accents():
    assert B.fingerprint("Léa", SALT) == B.fingerprint("lea", SALT)
