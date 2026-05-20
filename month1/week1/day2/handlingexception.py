try:
    f = open('text.txt')
    # if f.name == text.txt:
    #     raise Exception
    # var = bad_var
# except FileNotFoundError as e:
#     print(e)

except FileNotFoundError:
    print("sorry error occured")
except Exception :
    print("error found")    
else :
    print(f.read())
    f.close()
finally:
    print("runs no matter what")