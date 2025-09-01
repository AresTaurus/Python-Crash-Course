message="Hello Python World!"
#print message   ##variable__value
#print(message)

message = "Hello Python Crash Course World!"
#print(message)

message = "小结练习"
##print("message")
#print(message)


name = "ada lovelace"
#print(name.title())
##title() 方法以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写

name = "Ada Lovelace"
#print(name.upper())
#print(name.lower())

first_name = 'Ada'
last_name = "Lovelace"
full_name = f"{first_name} {last_name}"
#print(full_name)
##要在字符串中插入变量的值，可先在左引号前加上字母 f（见❶），再将要插入的变量放在花括号内。
##字符串称为 f 字符串。f 是 format（设置格式）的简写，因为 Python 通过把花括号内的变量替换为其值来设置字符串的格式。


first_name = 'Ada'
last_name = "Lovelace"
full_name = f"{first_name} {last_name}"
#print("hello",full_name)
#print("hello",full_name.upper())


##要在字符串中添加制表符，可使用字符组合 \t：
##要在字符串中添加换行符，可使用字符组合 \n：
#print("\n\n\nPython")
#print("Python")
#print("\tPython")

##。要确保字符串右端没有空白，可使用 rstrip() 方法。
##以删除字符串左端的空白或同时删除字符串两端的空白，分别使用lstrip() 方法和 strip() 方法即可
favorite_language = ' python '
print("\n",favorite_language)
favorite_language.rstrip()
print("\n",favorite_language)
favorite_language.lstrip()
print("\n",favorite_language)
favorite_language.strip()
print("\n",favorite_language)

