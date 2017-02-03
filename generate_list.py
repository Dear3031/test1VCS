import random
def generate_list():
    while True:
        sum = 0
        alist = [ x for x in range (random.randint(-10, 10)) ]
        for i in range (len(alist)):
            sum+=alist[i]
        assert(sum > -100), "Array value under -100"
        if (alist):
            break
    assert(alist), "Array list is NULL"
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