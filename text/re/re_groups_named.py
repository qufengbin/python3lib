# 1.3.6_3 用组解析匹配
# Python 扩展了基本组语法，还增加了命名组。通过使用名字来指示组可以更容易地修改模式，而不必同时修改使用了匹配结果的代码。要设置一个组的名字，可以使用语法 (?P<name>pattern)。

import re

text = 'This is some text -- with punctuation.'

print(text)
print()

patterns = [
    r'^(?P<first_word>\w+)',
    r'(?P<last_word>\s+)\S*',
    r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)',
    r'(?P<ends_with_t>\wt)\b'
]

# 可以使用 groupdict() 函数获取一个字典，它将组名映射为匹配的子串。命名模式也包含在 groups() 函数返回的有序序列中。

for pattern in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print("'{}'".format(pattern))
    print('    ',match.groups())
    print('    ',match.groupdict())
    print()

# 输出
# This is some text -- with punctuation.
#
# '^(?P<first_word>\w+)'
#      ('This',)
#      {'first_word': 'This'}
#
# '(?P<last_word>\s+)\S*'
#      (' ',)
#      {'last_word': ' '}
#
# '(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)'
#      ('text', 'with')
#      {'t_word': 'text', 'other_word': 'with'}
#
# '(?P<ends_with_t>\wt)\b'
#      ('xt',)
#      {'ends_with_t': 'xt'}