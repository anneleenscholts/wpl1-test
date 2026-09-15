#!/usr/bin/env python3
"""Controleert enkele basis-SEO-vereisten die html5validator niet afdwingt:
precies één <h1> per pagina, een ingevulde <title> en meta description."""
import sys
from html.parser import HTMLParser
from pathlib import Path


class SeoChecker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.h1_count = 0
        self.title = ""
        self.in_title = False
        self.description = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "h1":
            self.h1_count += 1
        if tag == "title":
            self.in_title = True
        if tag == "meta" and attrs.get("name") == "description":
            self.description = (attrs.get("content") or "").strip()

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data


def check_file(path: Path):
    errors = []
    warnings = []
    checker = SeoChecker()
    checker.feed(path.read_text(encoding="utf-8"))

    if checker.h1_count == 0:
        errors.append("Pagina mist een <h1>.")
    elif checker.h1_count > 1:
        errors.append(f"Pagina heeft {checker.h1_count} <h1>-elementen, gebruik er precies één.")

    title = checker.title.strip()
    if not title:
        errors.append("Pagina mist een ingevulde <title>.")
    elif len(title) > 60:
        warnings.append(f"<title> is {len(title)} tekens lang, hou het bij voorkeur onder 60.")

    if checker.description is None:
        errors.append('Pagina mist <meta name="description">.')
    elif not checker.description:
        errors.append('<meta name="description"> is leeg.')
    elif not (50 <= len(checker.description) <= 160):
        warnings.append(f"Meta description is {len(checker.description)} tekens lang, richt op 50-160.")

    return errors, warnings


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "public")
    had_errors = False

    for html_file in sorted(root.rglob("*.html")):
        errors, warnings = check_file(html_file)
        for message in errors:
            print(f"::error file={html_file}::{message}")
            had_errors = True
        for message in warnings:
            print(f"::warning file={html_file}::{message}")

    if had_errors:
        sys.exit(1)
    print("Basis-SEO-check geslaagd: elke pagina heeft een h1, title en meta description.")


if __name__ == "__main__":
    main()
