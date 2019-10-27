# 1.3.6_2 用组解析匹配
# 要访问单个组的匹配，可以使用 group() 方法。当使用组查找字符串的各个部分时，有些部分尽管与组匹配但在结果中并不需要，此时 group() 方法就很有用

import re

text = 'This is some text -- with punctuation.'
print('Input text            :',text)

regex = re.compile(r'(\bt\w+)\W+(\w+)')
print('Pattern               :',regex.pattern)

match = regex.search(text)
print('Entire match          :',match.group(0))
print('Word starting with "t":',match.group(1))
print('Word after "t" word   :',match.group(2))
# 组 0 表示与整个表达式匹配的字符串，子组按其左括号在表达式中出现的顺序编号，从 1 开始
# 输出
# Input text            : This is some text -- with punctuation.
# Pattern               : (\bt\w+)\W+(\w+)
# Entire match          : text -- with
# Word starting with "t": text
# Word after "t" word   : with