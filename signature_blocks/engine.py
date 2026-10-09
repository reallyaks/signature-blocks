"""Find signature blocks. Not legal advice and not a notary."""
from __future__ import annotations

import re
from dataclasses import dataclass

BLOCK_RE = re.compile(
    r"By:\s*(?P<by>.+)\nName:\s*(?P<name>.+)\nTitle:\s*(?P<title>.+)",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Signer:
    by: str
    name: str
    title: str


def find_signers(text: str) -> list[Signer]:
    return [
        Signer(match.group("by").strip(), match.group("name").strip(), match.group("title").strip())
        for match in BLOCK_RE.finditer(text)
    ]


def render(signers: list[Signer], source: str) -> str:
    lines = [
        f"# Signature blocks — {source}",
        "",
        "These are labels in the text. A block here was not checked against a wet signature.",
        "",
        "| By | Name | Title |",
        "| --- | --- | --- |",
    ]
    if not signers:
        lines.append("| — | — | — |")
    for signer in signers:
        lines.append(f"| {signer.by} | {signer.name} | {signer.title} |")
    lines.append("")
    return "\n".join(lines)
