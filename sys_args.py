import sys
from lootbag_db import *
from child_db import *

if __name__ == "__main__":
    test = Lootbag()
    test_child = Child()
    # bag commands
    if sys.argv[1] == "cr":
        print(sys.argv[2])
        test.create_bag(sys.argv[2])
    elif sys.argv[1] == "rm" and sys.argv[3] == "from":
        test.remove_child(sys.argv[2], sys.argv[4])
    elif sys.argv[1] == "ls" and sys.argv[2] == "toys" and sys.argv[3] == "in":
        test.get_toy_list(sys.argv[4])
    elif sys.argv[1] == "ls" and sys.argv[2] == "kids" and sys.argv[3] == "in":
        test.get_all_kids(sys.argv[4])
    elif sys.argv[1] == "ls" and sys.argv[2] == "deliveries" and sys.argv[3] == "in":
        test.toys_delivered(sys.argv[4])
    # child commands
    elif sys.argv[1] == "add" and sys.argv[3] == "for" and sys.argv[5] =="in" :
        test_child.create_child(sys.argv[2], sys.argv[4], sys.argv[6])
    elif sys.argv[1] == "add" and sys.argv[2] == "new":
        test_child.add_toy(sys.argv[4], sys.argv[3])
    elif sys.argv[1] == "rm" and sys.argv[3] == "for":
        test_child.remove_toy(sys.argv[4], sys.argv[2])
    elif sys.argv[1] == "ud":
        test_child.change_delivery_status(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "ls" and sys.argv[2] == "toys" and sys.argv[3] == "for":
        test_child.get_all_toys(sys.argv[4])
    elif sys.argv[1] == "rm" and sys.argv[2] == "all" and sys.argv[3] == "toys":
        test_child.remove_all_toys(sys.argv[4])