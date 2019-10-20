# 1.3.2 编译表达式
# 尽管 re 包括模块级函数，可以处理作为文本字符串的正则表达式，但对于程序频繁使用的表达式而言，编译它们更为高效。
# compile() 函数会把一个表达式字符串转换为一个 RegexObject。
import re
regexes = [
    re.compile(p)
    for p in ['this' , 'that']
]
text = 'Dose this text match the pattern?'

print('Text: {!r}'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern),end=' ')

    if regex.search(text):
        print('match')
    else:
        print('no match')

# 输出
# Text: 'Dose this text match the pattern?'
# Seeking "this" -> match
# Seeking "that" -> no match