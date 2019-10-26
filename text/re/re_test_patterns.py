# 1.3.4 模式语法
# 除了简单的字面量文本字符串，正则表达式还支持强大的模式。模式可以重复，可以锚定到输入中不同的逻辑位置，可以用更紧凑的形式表述而不是在模式中提供每一个字面量字符。可以结合字面量文本值和元字符来使用这些特性。

import re

def test_patterns(text,patterns):
    """
    :param text:
    :param patterns:
    :return:
    """
    for pattern,desc in patterns:
        print("'{}' ({})\n".format(pattern,desc))
        print("    '{}'".format(text))
        for match in re.finditer(pattern,text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslasher = text[:s].count('\\')
            prefix = '.' * (s + n_backslasher)
            print("    {}'{}'".format(prefix,substr))
        print()
    return

if __name__ == '__main__':
    test_patterns('abbaaabbbbaaaaa',[('ab',"'a'后面跟着'b'")])

# 1.3.4.1 重复
    test_patterns('abbaabbba',[
        ('ab*','a 后面跟着0个或多个b'), #匹配0个或多个b
        ('ab+','a 后面跟着1个或多个b'), #匹配1个或多个b
        ('ab?','a 后面跟着0个或1个b'), #匹配0个或1个b
        ('ab{3}','a 后面跟着3个b'), #匹配3个b
        ('ab{2,3}','a 后面跟着2个到3个b') #匹配2个或3个b
    ])

# 可以在重复指令后面加 ? 来关闭贪心行为
    test_patterns('abbaabbba', [
        ('ab*?', 'a 后面跟着0个或多个b'), #匹配0个b
        ('ab+?', 'a 后面跟着1个或多个b'), #匹配1个b
        ('ab??', 'a 后面跟着0个或1个b'), #匹配0个b
        ('ab{3}?', 'a 后面跟着3个b'), #匹配3个b
        ('ab{2,3}?', 'a 后面跟着2个到3个b') #匹配2个b
    ])

# 1.3.4.2 字符集
# 字符集是一组字符，包含可以与模式中当前位置匹配的所有字符。
    test_patterns('abbaabbba', [
        ('[ab]', '匹配a或b'),
        ('a[ab]+', 'a后面跟着1个或多个a或b'),
        ('a[ab]+?','a后面跟着1个a或b')
    ])

# 尖字符（^）意味着要查找不在这个尖字符后面的集合中的字符。
    test_patterns('This is some text -- with punctuation.',[
        ('[^-. ]+','查找不包含字符 -、. 或空格的所有子串')
    ])

# 字符区间（character range）定义一个字符集，包含指定的起点和终点之间所有连续的字符。
    test_patterns('This is some text -- with punctuation.',[
        ('[a-z]+','匹配1个或多个小写字母'),
        ('[A-Z]+','匹配1个或多个大写字母'),
        ('[a-zA-Z]+','匹配1个或多个大小写字母'),
        ('[A-Z][a-z]+','匹配1个大写字母后跟1个或多个小写字母')
    ])

# 作为字符集的一种特殊情况，元字符 点号（.）指示模式应当匹配该位置的单个字符。
    test_patterns('abbaabbba',[
        ('a.','匹配a后面跟任意一个字符'),
        ('a.*b','匹配a后面跟任意多个字符，结尾是b'),
        ('a.*?b', '匹配a后面跟任意多个字符，结尾是b') #非贪心模式
    ])

# 1.3.4.3 转义码
# \d:数字；\D：非数字；\s：空白符（制表符、空格、换行等）；\S：非空白符；\w：字母数字；\W：非字母数字
# 可以在字符前加一个反斜线（\）来指示转义。但是反斜线本身在正常的 Python 字符串中也需要转义，这会带来很难读的表达式。
# 通过使用原始（raw）字符串可以消除这个问题，可以在字面值前加 r 前缀来创建原始字符串。
test_patterns('A prime #1 example',[
    (r'\d+','匹配数字'),
    (r'\D+','匹配非数字'),
    (r'\s+','匹配空白符'),
    (r'\S+','匹配非空白符'),
    (r'\w+','匹配字母数字'),
    (r'\W+','匹配非字母数字')
])

test_patterns(r'\d+ \D+ \s+',[
    (r'\\.\+','escape code')
])

# 1.3.4.4 锚定
# ^：字符串或行的开头；$：字符串或行的末尾；\A：字符串开头；\Z：字符串末尾；\b：单词开头或末尾的空串；\B：非 单词开头或末尾的空串
# 使用锚定指令指定模式在输入文本中的相对位置。
test_patterns('This is some text -- with punctuation.',[
    (r'^\w+','匹配字母数字开头的字符串或行'),
    (r'\A\w+','匹配字母数字开头的字符串'),
    (r'\w+\S*$','匹配字母数字在字符串结尾'),
    (r'\w+\S*\Z','匹配字母数字在字符串结尾'),
    (r'\w*t\w*','单词连接t'),
    (r'\bt\w+','t在单词开头'),
    (r'\w+t\b','t在单词结尾'),
    (r'\Bt\B','t,不在开始或结尾')
])