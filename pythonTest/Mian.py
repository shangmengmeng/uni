# print("我在这")
# 第二个注释
print("我是谁")
print("再来一次")
# 缩进方式来表示代码块，如果缩进不一致会导致报错
# python 中数字有四种类型：整数，布尔型，浮点型，复数
# int bool float complex
# 字符串 String
word = '字符串'
print(word)
print(word[0 - 1])
print(word * 2)  # 输出字符串两次
print('hello\nsam')  # 使用反斜杠+n 进行转义
print(r'hello\sam')  # 使用r,表示原始字符，不会发生转义

# input("\n\n按下  enter 键后退出，")
# 同一行执行多条语句的时候，可以用;号隔开
import sys

x = "sam"
sys.stdout.write(x + "\n")
