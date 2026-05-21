# def func(x):
#     return x+5
# print(func(9))
# func2 = lambda x : x+9
# print(func2(5))
# func3 = lambda x,y : x + y
# print(func3(8,9))
# a = [1,2,3,4,5]
# new_list = list(map(lambda x : x , a))
# print(new_list)
# new_list = list(map(lambda x : x%2 == 0 , a))
# print(new_list)
# new_list = list(filter(lambda x : x%2 == 0 , a))
# print(new_list)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map — apply a function to every element
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# filter — keep only elements that match condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# combining both — filter evens then square them
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)