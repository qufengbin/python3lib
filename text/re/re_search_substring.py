# 1.3.5 限制搜索_2
import re
text = 'This is some text -- with punctuation.'
pattern = re.compile(r'\b\w*is\w*\b')

print('Text:',text)
print()

pos = 0
while True:
    match = pattern.search(text,pos)
    if not match:
        break
    s = match.start()
    e = match.end()
    print(' {:>2d} : {:>2d} = "{}"'.format(s , e-1, text[s:e]))
    # 进行下一个匹配
    pos = e

# 输出
# Text: This is some text -- with punctuation.
#
#   0 :  3 = "This"
#   5 :  6 = "is"