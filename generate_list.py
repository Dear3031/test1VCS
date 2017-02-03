import random
def generate_list():
    
    while True:
        alist = [ -x-100 for x in range (random.randint(0, 10)) ]
        if(alist):
            break
    
    
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