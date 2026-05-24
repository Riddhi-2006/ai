# mymodule.py

def greet(name):
    return f"Hello {name}!"

# this runs ONLY when you run this file directly
# it will NOT run when you import this file elsewhere
if __name__ == "__main__":
    print("Testing greet function:")
    print(greet("Riddhi"))