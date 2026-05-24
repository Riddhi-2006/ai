# print('Imported modules')
# test = 'test string'
# def find_index(to_search,target):
#     #find the index of a value in a sequence
#     for i,value in enumerate(to_search):
#         if value == target:
#             return i
#     return -1

import mymodules
from mymodules import greet, PI

courses = ['history', 'math', 'physics', 'compsci']

print(mymodules.find_index(courses, 'math'))  # 1
print(greet("Riddhi"))                        # Hello Riddhi!
print(PI)                                     # 3.14159

if __name__ == "__main__":
    print("Running directly!")