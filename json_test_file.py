import sys
import json
import sqlite3
from lootbag import *
from child import *


def main(args):
    print(args)

def loadData(bag):
    with open("{}.json".format(bag), "r") as bag_file:
        data = json.load(bag_file)
        # print(data)
        return data
        bag_file.close()

def createBag(bag):
    with open("{}.json".format(bag), "w+") as new_bag:
        newBag = Lootbag(bag)
        newBag = newBag.__dict__
        # test = newBag.__dict__
        json.dump(newBag, new_bag)
        new_bag.close()

def addChildAndToyToBag(toy, child, bag):
    child_bag = loadData(bag)
    new_child = Child(toy, child)
    new_child = new_child.__dict__
    print(new_child)
    with open("{}.json".format(bag), "w+") as bag_file:
        try:
            child_bag['children'][child]['toys'].append(toy)
        except KeyError:
            child_bag['children'][child] = dict()
            child_bag['children'][child] =new_child
            child_bag['children'][child]['toys'] = list()
            child_bag['children'][child]['toys'].append(toy)
        print(child_bag)
        json.dump(child_bag, bag_file)
        bag_file.close()

def removeToy(child, toy, bag):
    child_bag = loadData(bag)
    with open("{}.json".format(bag), "w+") as bag_file:
        child_bag['children'][child]['toys'].remove(toy)
        bag_file.close()

def listOfChildrenInBag(bag):
    list_bag = loadData(bag)
    print([child for child in list_bag['children']])

def removeNaughtyChild(child, bag):
    child_bag = loadData(bag)
    with open("{}.json".format(bag), "w+") as bag_file:
        del child_bag['children'][child]
        bag_file.close()

if __name__ == "__main__":
    main(sys.argv[1:])
    if sys.argv[1] == "create":
        createBag(sys.argv[2])
    elif sys.argv[1] == "add":
        addChildAndToyToBag(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1] == "remove":
        removeToy(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "ls" and sys.argv[2] == "bag":
        listOfChildrenInBag(sys.argv[3]) 

