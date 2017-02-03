import random
def generate_list():
    alist = [ x for x in range (random.randint(-10, 10)) ]
    return alist
    
"""
print agenerted list
"""
def printIt():
    print(generate_list())
    
def main():
    printIt()
    
"""
If this script file is called, it will run main() diractly
"""
if __name__ == '__main__':
    print("Test printIt():")
    main()