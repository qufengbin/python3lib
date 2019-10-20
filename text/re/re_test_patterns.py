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
        ()
    ])