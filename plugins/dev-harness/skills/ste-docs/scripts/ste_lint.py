"""Heuristic ASD-STE100 linter for Markdown docs.

Usage: python ste_lint.py <file.md> [more.md ...]

This is a heuristic. It catches the common violations (sentence length,
-ing forms, passive voice, unapproved words, long paragraphs). It does not
replace the official STE dictionary or a human check.
Exit code 1 if any ERROR is found.
"""
import re
import sys

PROCEDURAL_MAX = 20
DESCRIPTIVE_MAX = 25
PARAGRAPH_MAX = 6

SUBSTITUTIONS = {
    "utilize": "use", "utilise": "use", "leverage": "use", "ensure": "make sure",
    "perform": "do", "carry out": "do", "obtain": "get", "retrieve": "get",
    "commence": "start", "initiate": "start", "terminate": "stop",
    "in order to": "to", "prior to": "before", "subsequent to": "after",
    "approximately": "about", "sufficient": "enough", "additional": "more",
    "a number of": "some / many / the number", "please": "(remove)",
    "simply": "(remove)", "just": "(remove)", "easily": "(remove)",
    "obviously": "(remove)", "basically": "(remove)", "should": "imperative or 'must'",
    "facilitate": "help / let", "functionality": "function", "via": "through / with",
    "e.g.": "for example", "i.e.": "that is", "etc.": "list the items",
}

# Words ending in -ing that are not verb forms (or are approved).
ING_ALLOW = {
    "string", "strings", "thing", "things", "nothing", "something", "anything",
    "everything", "during", "morning", "evening", "ceiling", "spring", "ring",
    "bring", "king", "wing", "sing", "swing", "sling", "sting", "building",
    "warning", "warnings", "setting", "settings", "logging", "routing",
    "caching", "hosting", "pricing", "staging", "testing", "linting",
    "mapping", "mappings", "padding", "heading", "headings", "binding",
    "bindings", "listing", "rendering", "scaffolding", "ping", "boolean",
    "encoding", "encrypting", "hashing", "throttling", "polling", "missing",
}

PASSIVE_RE = re.compile(
    r"\b(is|are|was|were|be|been|being|gets|got)\s+(\w+ly\s+)?(\w+(ed|en))\b",
    re.IGNORECASE,
)
NOT_PARTICIPLE = {"open", "often", "even", "seven", "token", "hidden", "given", "golden", "kitten"}


def strip_markdown(text):
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]*`", "CODE", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    return text


def blocks(text):
    """Yield (kind, block_text) where kind is 'list-num', 'list', 'para'."""
    for raw in re.split(r"\n\s*\n", text):
        lines = [l for l in raw.splitlines() if l.strip()]
        if not lines:
            continue
        if all(l.lstrip().startswith("#") for l in lines):
            continue
        if any(l.lstrip().startswith("|") for l in lines):
            continue  # tables: skip
        if re.match(r"\s*\d+[.)]\s", lines[0]):
            for l in lines:
                yield "list-num", re.sub(r"^\s*\d+[.)]\s*", "", l)
        elif re.match(r"\s*[-*+]\s", lines[0]):
            for l in lines:
                yield "list", re.sub(r"^\s*[-*+]\s*", "", l)
        else:
            body = " ".join(l for l in lines if not l.lstrip().startswith("#"))
            yield "para", body


def sentences(block):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9`\"'(])", block.strip())
    return [p.strip() for p in parts if len(p.split()) > 0]


def lint(path):
    with open(path, encoding="utf-8") as f:
        text = strip_markdown(f.read())
    findings = []

    def add(level, msg, sent):
        snippet = sent if len(sent) < 110 else sent[:107] + "..."
        findings.append((level, msg, snippet))

    for kind, block in blocks(text):
        sents = sentences(block)
        if kind == "para" and len(sents) > PARAGRAPH_MAX:
            add("WARN", f"paragraph has {len(sents)} sentences (max {PARAGRAPH_MAX})", sents[0])
        for s in sents:
            words = re.findall(r"[A-Za-z0-9'][\w'-]*", s)
            limit = PROCEDURAL_MAX if kind == "list-num" else DESCRIPTIVE_MAX
            if len(words) > limit:
                add("ERROR", f"{len(words)} words (max {limit} for "
                    f"{'procedural' if limit == PROCEDURAL_MAX else 'descriptive'})", s)
            elif kind != "list-num" and len(words) > PROCEDURAL_MAX and re.match(r"^[A-Z][a-z]+\s", s) \
                    and words[0].lower() in {"run", "open", "set", "add", "remove", "install", "click", "make", "do", "start", "stop", "change", "copy", "create", "delete", "push", "pull", "deploy"}:
                add("ERROR", f"instruction has {len(words)} words (max {PROCEDURAL_MAX})", s)
            if kind == "list-num" and re.search(r"\b(and then|, then| then )\b", s, re.IGNORECASE):
                add("WARN", "possible two instructions in one step", s)
            for w in words:
                lw = w.lower()
                if lw.endswith("ing") and len(lw) > 4 and lw not in ING_ALLOW:
                    add("WARN", f"'-ing' form: '{w}' (allowed only in technical names)", s)
            for m in PASSIVE_RE.finditer(s):
                if m.group(3).lower() not in NOT_PARTICIPLE:
                    add("WARN", f"possible passive voice: '{m.group(0)}'", s)
            low = " " + s.lower() + " "
            for bad, good in SUBSTITUTIONS.items():
                if re.search(r"(?<![\w-])" + re.escape(bad) + r"(?![\w-])", low):
                    add("ERROR", f"unapproved word '{bad}' -> {good}", s)
    return findings


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    errors = 0
    for path in sys.argv[1:]:
        found = lint(path)
        print(f"== {path}: {len(found)} finding(s)")
        for level, msg, snip in found:
            print(f"  [{level}] {msg}\n      > {snip}")
            errors += level == "ERROR"
    print(f"\n{errors} error(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
