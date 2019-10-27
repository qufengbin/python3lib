# 1.3.1 查找文本中的正则表达式
# search() 函数取模式和要扫描的文本作为输入，找到这个模式时，就返回一个 Match 对象。如果没有找到模式，search() 将返回 None。
import re

pattern = 'this'
text = 'Dose this text match the pattern?'

match = re.search(pattern,text)

# start() 和 end() 方法可以提供字符串中的相应索引，指示与模式匹配的文本在字符串中出现的位置。
s = match.start()
e = match.end()

print('Found "{}" in "{}" from {} to {} ("{}")'.format(match.re.pattern,match.string,s,e,text[s:e]))

# 输出
# Found "this" in "Dose this text match the pattern?" from 5 to 9 ("this")