# def outerfunc():
#     message = "hi"
#     def innerfunc():
#         print(message)
#     return innerfunc()
# outerfunc()    

# def outerfunc(msg):
#     # message = msg
#     # message = "hi"
#     def innerfunc():
#         print(msg)
#     return innerfunc
# myfunc = outerfunc('hi')  
# myfunc()

def decorater_func(original_func):
    def wrapper_func(*args,**kwargs):
        print("this ran before {}".format(original_func.__name__))
        return original_func(*args,**kwargs)
    return wrapper_func

# class decorater_class(object):
#     def __init__(self,original_func):
#         self.original_func = original_func
#     def __call__(self,*args,**kwargs):
#         print("call method executed this before {}".format(self.original_func.__name__))
#         return self.original_func(*args,**kwargs)

@decorater_func #func = decorater_func(display)
def display():
    print("display ran")
# func = decorater_func(display)
# func()    
@decorater_func
def display_info(name,age):
    print("display_info ran with arguements({}, {})".format(name,age))
display_info("riddhi",19)
display()

