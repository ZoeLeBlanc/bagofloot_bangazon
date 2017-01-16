import unittest
from lootbag import *
from child import *


def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestLootbag(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print ('Set up class')
        #Create initial instance
        self.delivery_bag = Lootbag()

    @classmethod
        def tearDownClass(self):
        print('Tear down class')
    
    def addChildAndGiftToDelivery(self):
        #Checks if you can add a child with a gift to the delivery bag
        zoe = Child('Zoe')
        zoe.toys = 'pony'
        self.delivery_bag.add_child(zoe)
        self.assertIn(zoe, self.delivery_bag.children)

    def removeChildAndAllTheirGiftsFromDelivery(self):
        #checks if you can remove a child and all its associated gifts from the deliverybag
        trent = Child('Trent')
        trent.toys = ['pony', 'baseball']
        self.delivery_bag.add_child(trent)
        self.delivery_bag.remove_child(trent)
        self.assertNotIn(trent, self.delivery_bag.children)

    def getAllToysToBeDelivered(self):
        #Checks if you can get a list of all toys to be delivered
        zoe = Child('Zoe')
        zoe.toys = ['pony','basketball']
        self.delivery_bag.add_child(zoe)
        trent = Child('Trent')
        trent.toys = ['pony', 'baseball']
        self.delivery_bag.add_child(trent)
        self.delivery_bag.update_toys()
        self.assertEqual(self.delivery_bag.all_toys, self.delivery_bag.get_toy_list())

    def listAllChildrenInDeliveryBag(self):
        #Check if you can get a list of the children in the delivery bag
        list_of_all_kids = []
        for child in self.delivery_bag.children:
            list_of_all_kids.append(child[0])
        self.assertEqual(list_of_all_kids, self.delivery_bag.get_all_kids())

    def removeGift(self):
        #Check if you can remove a gift from a child
        drake = Child('Drake')
        drake.toys = 'basketball'
        drake.remove_gift('basketball')
        self.assertNotIn('basketball', drake.toys)

    def addGift(self):
        #Check if you can add a gift to child
        ike = Child('Ike')
        ike.add_gift('laptop')    
        self.assertIn('laptop', ike.toys)

    def changeDeliveryStatus(self):
        #Check if you can change the delivery status of a child
        steve = Child('Steve')
        steve.delivery_status = True
        self.assertTrue(steve.delivery_status)

    def listAllOfChildToys(self):
        #Check if you can get a list of the toys for one child
        whitney = Child('Whitney')
        whitney.toys = ['Bike', 'laptop', 'clothes']
        self.assertEqual(whitney.toys, whitney.get_all_toys())

    def naughtyChild(self):
        #Check if you can remove all of a child's toys if they're naughty
        whitney = Child('Whitney')
        whitney.toys = ['Bike', 'laptop', 'clothes']
        whitney.remove_all_toys()
        self.assertIsNone(whitney.toys)
    
if __name__ == '__main__':
    unittest.main()