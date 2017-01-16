import sys
from lootbag import *
from child import *

def main(args):
    print(args)


if __name__ == "__main__":
    main(sys.argv[1:])
    testbag = Lootbag()
    if "add" == sys.argv[1]:
        child = Child(sys.argv[2], sys.argv[3])
        testbag.add_child(child)
        print(testbag)
    if "remove" == sys.argv[1]:
        if sys.argv[2] in testbag.children:
            print("exists")
        else:
            print("doesn't exist")
            print(testbag)
        # sys.argv[2].remove_toy(sys.argv[3])
    if "ls" == sys.argv[1]:
        testbag.get_all_kids()

    