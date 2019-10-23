for letter in "Python":
    if letter == "h":
        break
    print("当前字母为：", letter)

# 当前字母为： P
# 当前字母为： y
# 当前字母为： t

# 元组和列表的区别：元组用的括号，列表用的方括号
# 字典：就是key,Value

tup1 = (1, 2, 3, 4, 5)

print(tup1[1:3])


def hello(word):
    print(word + "你好")


hello("sam同志")
