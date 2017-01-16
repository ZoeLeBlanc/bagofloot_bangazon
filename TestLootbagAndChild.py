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
        self.delivery_bag = Lootbag("delivery bag")

    # @classmethod
    #     def tearDownClass(self):
    #     print('Tear down class')
    
    def test_addChildAndGiftToDelivery(self):
        #Checks if you can add a child with a gift to the delivery bag
        zoe = Child('pony', 'Zoe')
        self.delivery_bag.add_child(zoe)
        self.assertIn(zoe, self.delivery_bag.children)

    def test_removeChildAndAllTheirGiftsFromDelivery(self):
        #checks if you can remove a child and all its associated gifts from the deliverybag
        trent = Child(['pony', 'baseball'], 'Trent')
        self.delivery_bag.add_child(trent)
        self.delivery_bag.remove_child(trent)
        self.assertNotIn(trent, self.delivery_bag.children)

    def test_getAllToysToBeDelivered(self):
        #Checks if you can get a list of all toys to be delivered
        zoe = Child('basketball', 'Zoe')
        self.delivery_bag.add_child(zoe)
        trent = Child('pony', 'Trent')
        self.delivery_bag.add_child(trent)
        self.delivery_bag.update_toys()
        self.assertEqual(self.delivery_bag.all_toys, self.delivery_bag.get_toy_list())

    def test_listAllChildrenInDeliveryBag(self):
        #Check if you can get a list of the children in the delivery bag
        zoe = Child('basketball', 'Zoe')
        self.delivery_bag.add_child(zoe)
        trent = Child('pony', 'Trent')
        self.delivery_bag.add_child(trent)
        list_of_all_kids = []
        for child in self.delivery_bag.children:
            list_of_all_kids.append(child.name)
        self.assertEqual(list_of_all_kids, self.delivery_bag.get_all_kids())

    def test_toysDelivered(self):
        #Check which toys are delivered
        zoe = Child('basketball', 'Zoe')
        self.delivery_bag.add_child(zoe)
        trent = Child('pony', 'Trent')
        self.delivery_bag.add_child(trent)
        list_of_all_delivered_toys = []
        for child in self.delivery_bag.children:
            if child.delivery_status is True:
                list_of_all_delivered_toys.append(child.toys)
        self.assertEqual(list_of_all_delivered_toys, self.delivery_bag.toys_delivered())
    def test_removeToy(self):
        #Check if you can remove a toy from a child
        drake = Child('basketball', 'Drake')
        drake.remove_toy('basketball')
        self.assertNotIn('basketball', drake.toys)

    def test_addToy(self):
        #Check if you can add a toy to child
        ike = Child('laptop', 'Ike')
        ike.add_toy('bike')    
        self.assertIn('bike', ike.toys)

    def test_changeDeliveryStatus(self):
        #Check if you can change the delivery status of a child
        steve = Child('ipad,', 'Steve')
        steve.change_delivery_status(True)
        self.assertTrue(steve.delivery_status)

    def test_listAllOfChildToys(self):
        #Check if you can get a list of the toys for one child
        whitney = Child('laptop', 'Whitney')
        self.assertEqual(whitney.toys, whitney.get_all_toys())

    def test_naughtyChild(self):
        #Check if you can remove all of a child's toys if they're naughty
        whitney = Child('Bike', 'Whitney')
        whitney.remove_all_toys()
        self.assertFalse(whitney.toys)

if __name__ == '__main__':
    unittest.main()