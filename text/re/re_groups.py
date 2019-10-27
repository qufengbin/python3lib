# 1.3.6_1 用组解析匹配
# 搜索模式匹配是正则表达式强大能力的基础。为模式提供组可以隔离匹配文本的各个部分，以扩展这些功能来创建一个解析器。可以用 小括号包围 模式来定义组。
# from text.re.re_test_patterns import test_patterns
#
# test_patterns(
#     'abbaaabbbbaaaaa',[
#         ('a(ab)','匹配a后面跟着ab'),
#         ('a(a*b*)','匹配a后面跟着 0-n 个 a 和 0-n 个 b'),
#         ('a(ab)*','匹配a后面跟着 0-n 个 ab'),
#         ('a(ab)+','匹配a后面跟着 1-n 个 ab')
#     ]
# )

# 要访问与模式中各个组匹配的子串，可以使用 match 对象的 groups() 方法。
# match.groups() 按匹配字符串的组在表达式中的顺序返回一个字符串序列。

import re

text = 'This is some text -- with punctuation.'

print(text)
print()

# \d:数字；\D：非数字；\s：空白符（制表符、空格、换行等）；\S：非空白符；\w：字母数字；\W：非字母数字
# ^：字符串或行的开头；$：字符串或行的末尾；\A：字符串开头；\Z：字符串末尾；\b：单词开头或末尾的空串；\B：非 单词开头或末尾的空串

patterns = [
    (r'^(\w+)','匹配开头的字母数字'),
    (r'(\w+)\S*$','匹配结尾的字母数字,和一个非空白符'),
    (r'(\bt\w+)\W+(\w+)','t开头的字母数字，和之后的一个字母数字'),
    (r'(\w+t)\b','t结尾的字母数字')
]

for pattern,desc in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print("'{}' ({})\n".format(pattern,desc))
    print('    ',match.groups())
    print()