#! Insert the current diractory path to Python path
import sys
import os
cwd = os.getcwd()

sys.path.append(cwd)
#print (sys.path)

#Test the module: generate_list
from genlist_test import printIt
printIt()