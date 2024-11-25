# Code from https://www.geeksforgeeks.org/how-to-print-the-python-exception-error-hierarchy/

import inspect


def treeClass(cls, ind=0):

    # print name of the class
    print('-' * ind, cls.__name__)

    # iterating through subclasses
    for i in cls.__subclasses__():
        treeClass(i, ind + 3)


print("Hierarchy for Built-in exceptions is : ")

# inspect.getmro() Return a tuple
# of class cls’s base classes.

# building a tree hierarchy
inspect.getclasstree(inspect.getmro(BaseException))

# function call
treeClass(BaseException)
