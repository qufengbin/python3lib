# 1.3.6_4 用组解析匹配
# 更新的 test_patterns() 会显示一个模式匹配的编号组和命名组，使例子更容易理解
import re

def test_patterns(text,patterns):
    """
    输入一个文本和一个表达式列表，在文本中为每个表达式寻找匹配并展示它们。
    :param text:
    :param patterns:
    :return:
    """
    for pattern,desc in patterns:
        print('{!r} ({})\n'.format(pattern,desc))
        print('    {!r}'.format(text))
        for match in re.finditer(pattern,text):
            s = match.start()
            e = match.end()
            prefix = ' ' * (s)
            print('    {}{!r}{} '.format(prefix,text[s:e],' ' * (len(text) - e)),end=' ')

            print(match.groups())
            if match.groupdict():
                print('{}{}'.format(' ' * (len(text) - s),match.groupdict()))

        print()
    return

if __name__ == "__main__":

    # 在这里，组 (a*) 匹配一个空串，所以 groups() 的返回值包含空串作为匹配值。
    test_patterns('abbaabbba',[
        (r'a((a*)(b*))','匹配 a 后面跟随 0-n 个 a 和 0-n 个 b')
    ])

    # 组还可以用于指定替代模式，可以使用管道符号（|）指示应当匹配某一个模式。如果一个替代组不匹配，但是整个模式匹配，那么 groups() 的返回值会在序列中本应出现替代组的位置包含一个 None 值
    test_patterns('abbaabbba',[
        (r'a((a+)|(b+))','匹配 a 后面跟着一个完全由某一个字母（a 或 b）组成的序列'),
        (r'a((a|b)+)','匹配 a 后面跟着一个可能包含 a 或 b 的序列')
    ])

    # 如果匹配子模式的字符串不必从整个文本中抽取出来，那么在这种情况下，定义包含子模式的组也很有用。这些组被称为非捕获组。
    # 非捕获组可以用来描述重复模式或替代，而不会隔离返回值中字符串的匹配部分。使用语法 (?:pattern) 创建一个非捕获组。
    test_patterns('abbaabbba',[
        (r'a((a+)|(b+))','捕获组'),
        (r'a((?:a+)|(?:b+))', '非捕获组')
    ])