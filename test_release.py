"""Static release smoke test: stdlib only. Run after serving directory on port 8780."""
import json, urllib.request
from pathlib import Path
root=Path(__file__).parent
html=(root/'index.html').read_text(encoding='utf-8')
assert '<title>学习计划助手' in html
for needle in ['完成量','做完记录什么','确认调整并生成新版本','localStorage','导出数据','导入数据','每科仅一个主资料','每天大概能学多久','isValidImport','todayTasks','目标节点','adjustingKind === "blocked"']:
    assert needle in html, needle
assert 'const isSafeId = (value)' in html
assert '^[A-Za-z][A-Za-z0-9_-]{0,63}$' in html
assert 'function loadState()' in html
schema=json.loads((root/'data-model.json').read_text())
assert schema['properties']['tasks']['type']=='array'
goal=schema['properties']['goal']
assert 'dailyHours' in goal['required']
assert goal['properties']['officialStatus']['enum']==['user-defined','to-verify']
print('PASS: static artifact and data contract checks')
