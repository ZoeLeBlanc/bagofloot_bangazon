import sys
import json
from lootbag import *
from child import *


def main(args):
    print(args)

def createBag(bag):
    with open("{}.txt".format(bag), "w+") as new_bag:
        newBag = Lootbag(bag)
        # test = newBag.__dict__
        new_bag.write(newBag.name)
        new_bag.close()

def addChildrenToBag(child, toys, bag):
    with open("{}.txt".format(child), "a+") as child_file:
        new_child = Child(toys, child)
        newBag.add_child(new_child)
        print(newBag)
        child_file.write(str(child.toys).strip('[]') + "\n") 
    # with open("{}.txt".format(sys.argv[4]), "r") as bag_file: 
    #     lines = [line.rstrip('\n') for line in bag_file]
    #     bag_file.close()
    # with open("{}.txt".format(sys.argv[4]), "a+") as bag_file:
    #                 for line in lines:
    #                     if sys.argv[3] is line:
    #                         print(line)
                            
    #                     else:
    #                         print("test")
    #                         # bag_file.write(sys.argv[3] + "\n")
if __name__ == "__main__":
    main(sys.argv[1:])
    if "create" == sys.argv[1]:
        createBag(sys.argv[2])
    if "add" == sys.argv[1]:
       addChildrenToBag(sys.argv[3], sys.argv[2], sys.argv[4])
    if "remove" == sys.argv[1]:
        with open("{}.txt".format(sys.argv[2]), "r") as child_file:
            lines = [line.rstrip('\n') for line in child_file]
            print(lines)
            child_file.close()
            with open("{}.txt".format(sys.argv[2]), "w") as child_file:
                # test = 
                for line in lines:
                    if line[1:-1] != sys.argv[3]:
                        child_file.write(line[1:-1] + "\n")
            child_file.close()
    # if "ls" == sys.argv[1]:
        # if sys.argv[2] 

