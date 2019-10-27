# 1.3.5 限制搜索_1
# 有些情况下，可以提前知道只需要搜索整个输入的一个子集，在这些情况下，可以告诉 re 限制搜索范围从而进一步约束正则表达式匹配。例如，
# 如果模式必须出现在输入开头，那么使用 match() 而不是 search() 会锚定搜索，而不必显式地在搜索模式中包含一个锚。

import re

text = 'This is some text -- with punctuation.'
pattern = 'is'

print('Text   :',text)
print('Pattern:',pattern)

m = re.match(pattern,text)
print('Match  :',m)
s = re.search(pattern,text)
print('Search :',s)

# 由于字面量文本 is 未出现在输入文本的开头，因此使用 match() 时找不到它。但是这个序列在文本中另外还出现了两次，所以 search() 能搜索到。
# 输出
# Text   : This is some text -- with punctuation.
# Pattern: is
# Match  : None
# Search : <re.Match object; span=(2, 4), match='is'>

pattern2 = 'Th'

print('Text    :',text)
print('pattern2:',pattern2)

m = re.match(pattern2,text)
print('Match  :',m)
s = re.search(pattern2,text)
print('Search :',s)
# 输出
# Text    : This is some text -- with punctuation.
# pattern2: Th
# Match  : <re.Match object; span=(0, 2), match='Th'>
# Search : <re.Match object; span=(0, 2), match='Th'>

# fullmatch() 方法要求整个输入字符串与模式匹配。
print('Text     :',text)
print('pattern  :',pattern)
print('pattern2 :',pattern2)
print('Match    :',m)
print('Search   :',s)
fm = re.fullmatch(pattern2,text)
print('fullmatch:',fm)
# 输出
# Text     : This is some text -- with punctuation.
# pattern  : is
# pattern2 : Th
# Match    : <re.Match object; span=(0, 2), match='Th'>
# Search   : <re.Match object; span=(0, 2), match='Th'>
# fullmatch: None

pattern3 = 'This'
print('Text      :',text)
print('pattern3  :',pattern3)
m = re.match(pattern3,text)
print('Match     :',m)
s = re.search(pattern3,text)
print('Search    :',s)
fm = re.fullmatch(pattern3,text)
print('fullmatch :',fm)
# 输出
# Text      : This is some text -- with punctuation.
# pattern3  : This
# Match     : <re.Match object; span=(0, 4), match='This'>
# Search    : <re.Match object; span=(0, 4), match='This'>
# fullmatch : None

text = 'This'
print('Text      :',text)
print('pattern3  :',pattern3)
m = re.match(pattern3,text)
print('Match     :',m)
s = re.search(pattern3,text)
print('Search    :',s)
fm = re.fullmatch(pattern3,text)
print('fullmatch :',fm)
# 输出
# Text      : This
# pattern3  : This
# Match     : <re.Match object; span=(0, 4), match='This'>
# Search    : <re.Match object; span=(0, 4), match='This'>
# fullmatch : <re.Match object; span=(0, 4), match='This'>