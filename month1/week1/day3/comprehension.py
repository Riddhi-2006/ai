# nums = [1,2,3,4,5,6,7,8,9,10]
# my_list = []
# for n in nums :
#     my_list.append(n)
# print(my_list)

# my_list = [n for n in nums]
# print (my_list)

# for n in nums:
#     my_list.append(n*n)
# print(my_list)

# my_list = [n*n  for n in nums]
# print(my_list)
#using maps and lambda
# my_list =list( map(lambda n : n*n , nums))
# print(my_list)

# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)
# my_list = [n for n in nums if n%2 == 0]
# print(my_list)
#using filter+ lambda
# my_list = list(filter (lambda n :n%2 == 0,nums))
# print(my_list)

# for letter in 'abcd':
#     for n in range(4):
#         my_list.append((letter,n))

# print(my_list)        

# my_list = [(letter,n) for letter in 'abcd' for n in range(4) ]

#dictionary comprehension
# name = ['riddhi','rohan','shruti','amruta']
# surname = ['nashine','nandanwar','dhole','gotmare']
# print(list(zip(name,surname)))
# my_dict = {}
# for name,surname in zip(name,surname):
#     my_dict[name]= surname
# print(my_dict)
# my_dict = {name : surname for name,surname in zip(name,surname) if name!= 'amruta'}
# print(my_dict)

#set comprehension set have unique values
# nums = [1,1,2,3,4,4,5,5,6,7,7,8,9,9]
# my_set = set()
# for n in nums :
#     my_set.add(n)
# print(my_set)
# my_set = {n for n in nums}
# print(my_set)
#generator function
nums = [1,2,3,4,5,6,7,8]
def gen_func(nums):
    for n in nums:
        yield n*n
my_gen = gen_func(nums)
# print(list(my_gen))
# for i in my_gen:
#     print (i)
gen_func = (n*n for n in nums)
for i in gen_func:
    print (i)