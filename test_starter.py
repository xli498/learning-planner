from pathlib import Path

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
required = [
    'onclick="createStarterPlan()"',
    'const STARTER_TEMPLATES',
    '"国考"',
    '"行测·资料分析"',
    '"申论"',
    '资料均为待替换占位',
    '关联科目',
]
missing = [item for item in required if item not in html]
if missing:
    raise SystemExit("FAIL missing: " + ", ".join(missing))
print("PASS: starter templates and guided setup present")
