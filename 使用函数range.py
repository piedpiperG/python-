#只会打印1，2，3，4
for value in range(1,5) :
    print(value)

#使用函数list，将range中的数转换为列表
numbers = list (range(1,6))
print(numbers)

#使用range时，还可以指定步长
even_numbers = list(range(2,11,2))
print(even_numbers)

#使用range创造你想要的数集
squares = []
for value in range (1,11) :
    squares.append(value**2)
print(squares)

