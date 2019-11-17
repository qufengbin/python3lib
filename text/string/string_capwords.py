# 1.1.1 函数
# 函数 capwords() 会把一个字符串中的所有单词首字母大写。
import string

s = 'The quick brown fox jumped over the lazy dog.'
print(s)
print(string.capwords(s))

# 输出
# The quick brown fox jumped over the lazy dog.
# The Quick Brown Fox Jumped Over The Lazy Dog.