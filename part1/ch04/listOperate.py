#一系列按特定顺序排列的元素
cities = ['北京', '上海', '深圳', '杭州','川渝']
print(cities)

#列表是有序集合，访问列表的任何元素，只需将该元素的位置（索引)
print(cities[0])
#获取列表元素时，Python 只返回该元素，而不包括方括号
#import full_name
#print(full_name[0].title())


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#meth01
# 创建一个新列表来存储首字母大写的元素
capitalized_bicycles = []

# 遍历原列表中的每个元素
for bike in bicycles:
    # 将每个元素首字母大写并添加到新列表
    capitalized_bicycles.append(bike.title())

# 打印新列表
print(capitalized_bicycles,"使用 for 循环（最基础）")


#meth02
#一行代码完成

capitalized_bicycles = [bike.title() for bike in bicycles]

print(capitalized_bicycles,"使用列表推导式（更简洁）")


#meth03

for bike in bicycles:
    print(bike.title(),"直接遍历并打印每个元素的首字母大写形式")
##Trek 直接遍历并打印每个元素的首字母大写形式
##Cannondale 直接遍历并打印每个元素的首字母大写形式
##Redline 直接遍历并打印每个元素的首字母大写形式
##Specialized 直接遍历并打印每个元素的首字母大写形式


#meth04
capitalized_bicycles = list(map(str.title, bicycles))

print(capitalized_bicycles,"使用map函数应用title()方法到每个元素")


#Python 为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1，可让 Python 返回最后一个列表元素：
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[2].title()}."
print(message)

##修改
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

##添加append，添加到列表末尾
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)


##插入insert
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
#的每个既有元素都右移一个位置


##删除del
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)


##pop
##pop() 方法删除列表末尾的元素，并让你能够接着使用它。术语弹出（pop）源自这样的类比：列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。
print("一一一一一一一一一一一一一一一一一一一一一一一一一")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


##pop删除
print("一一一一一一一一一一一一一一一一一一一一一一一一一")
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(2)
print(f"The first motorcycle I owned was a {first_owned.title()}.")


##根据值删除元素remove
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda',  'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")


##使用 sort() 方法对列表进行永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
cars.sort(reverse=True)
print(cars)
