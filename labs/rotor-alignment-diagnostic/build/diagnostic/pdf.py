"""Simple PDF of the report. Iris styles it at G4; this is plain on purpose."""
from __future__ import annotations

import io
import re
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def _inline(s: str) -> str:
    s = escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<i>\1</i>", s)


def make_pdf(report_md: str, title: str = "Leadership alignment report") -> bytes:
    ss = getSampleStyleSheet()
    h1, h2, h3, body = ss["Heading1"], ss["Heading2"], ss["Heading3"], ss["BodyText"]
    story = []
    for raw in report_md.splitlines():
        line = raw.rstrip()
        if not line.strip():
            story.append(Spacer(1, 6))
        elif line.startswith("### "):
            story.append(Paragraph(_inline(line[4:]), h3))
        elif line.startswith("## "):
            story.append(Paragraph(_inline(line[3:]), h2))
        elif line.startswith("# "):
            story.append(Paragraph(_inline(line[2:]), h1))
        elif line.startswith(("- ", "* ")):
            story.append(Paragraph("&bull; " + _inline(line[2:]), body))
        elif re.match(r"^\|[\s\-|:]+\|$", line):
            continue
        elif line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            story.append(Paragraph(" &nbsp;|&nbsp; ".join(_inline(c) for c in cells), body))
        else:
            story.append(Paragraph(_inline(line), body))
    buf = io.BytesIO()
    SimpleDocTemplate(buf, pagesize=letter, title=title, author="Franklin Kinetics").build(story)
    return buf.getvalue()
