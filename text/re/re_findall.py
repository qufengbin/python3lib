# 1.3.3 多重匹配
# findall() 函数会返回输入中与模式匹配而且不重叠的所有子串。
import re
text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.findall(pattern,text):
    print('Found {!r}'.format(match))

# 输出
# Found 'ab'
# Found 'ab'

# finditer() 返回一个迭代器，它会生成 Match 实例，而不是返回字符串、

for match in re.finditer(pattern,text):
    s = match.start()
    e = match.end()
    print('Found {!r} at {:d}:{:d}'.format(text[s:e],s,e))

# 输出
# Found 'ab' at 0:2
# Found 'ab' at 5:7