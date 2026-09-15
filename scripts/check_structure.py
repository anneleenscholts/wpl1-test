#!/usr/bin/env python3
"""Controleert projectconventies die html5validator niet afdwingt:
geen inline/embedded CSS, en geïmporteerde scripts enkel in <head>."""
import sys
from html.parser import HTMLParser
from pathlib import Path


class StructureChecker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tag_stack = []
        self.violations = []

    def in_head(self):
        return "head" in self.tag_stack

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        line, _ = self.getpos()

        if tag == "style":
            self.violations.append((line, "CSS moet via een externe stylesheet, geen <style>-blok."))

        if "style" in attrs:
            self.violations.append((line, f"Inline style-attribuut op <{tag}> is niet toegestaan."))

        if tag == "script" and "src" in attrs and not self.in_head():
            self.violations.append((line, "Geïmporteerd <script src> moet in <head> staan."))

        self.tag_stack.append(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.tag_stack) - 1, -1, -1):
            if self.tag_stack[i] == tag:
                del self.tag_stack[i:]
                break


def check_file(path: Path):
    checker = StructureChecker()
    checker.feed(path.read_text(encoding="utf-8"))
    return checker.violations


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "public")
    had_errors = False

    for html_file in sorted(root.rglob("*.html")):
        for line, message in check_file(html_file):
            print(f"::error file={html_file},line={line}::{message}")
            had_errors = True

    if had_errors:
        sys.exit(1)
    print("Geen inline CSS en alle geïmporteerde scripts staan in <head>.")


if __name__ == "__main__":
    main()
