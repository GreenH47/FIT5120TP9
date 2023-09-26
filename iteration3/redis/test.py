def my_function(b, c):
    # Function logic goes here
    a = b+c
    return a


# Additional function definitions go here

def function_test():
    c = 1 + 2
    if c != my_function(2,1):
        print("wrong")
    else:
        print("right")


# Additional test classes and test cases can be defined here

if __name__ == '__main__':
    function_test()
