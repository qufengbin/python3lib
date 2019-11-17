# 1.3.7 搜索选项
# 选项标识用来改变匹配引擎处理表达式的方式。可以使用位或（OR）操作结合这些标志，然后传递到 compile()、search()、match() 和其他接受搜索模式的函数。
# 1.3.7.1 大小写无关的匹配
import re

text = 'This is some text -- with punctuation.'
pattern = r'\bT\w+'
with_case = re.compile(pattern)
without_case = re.compile(pattern,re.IGNORECASE)

print('Text:\n  {!r}'.format(text))
print('Pattern:\n  {}'.format(pattern))
print('Case-sensitive:')
for match in with_case.findall(text):
    print('    {!r}'.format(match))
print('Case-insensitive:')
for match in without_case.findall(text):
    print('    {!r}'.format(match))

# 输出
# Text:
#   'This is some text -- with punctuation.'
# Pattern:
#   \bT\w+
# Case-sensitive:
#     'This'
# Case-insensitive:
#     'This'
#     'text'