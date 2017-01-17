class Lootbag(object):

    def __init__(self, name):
        self.name = name
        self.children = dict()
        self.all_toys = []

    def add_child(self, child):
        self.children[child.name] = child.__dict__

    def remove_child(self, child):
        del self.children[child]

    def update_toys(self):
        for key, item in self.children.items():
            print(item['toys'])
            self.all_toys += item['toys']
        # return self.all_toys

    def get_toy_list(self):
        return self.all_toys

    def get_all_kids(self):
        kids = []
        print(self.children)
        for key, item in self.children.items():
            kids.extend({item['name']})
        return kids

    def toys_delivered(self):
        delivered_toys = []
        for key, item in self.children.items():
            if item['delivery_status'] is True:
                print(item)
                delivered_toys += item['toys']
        return delivered_toys

    # def __str__(self):
    #     return "This bag has these children: {} and these toys: {}, of which these {} have been delivered".format(str(self.get_all_kids()).strip('[]'), str(self.get_toy_list()).strip('[]'), str(self.toys_delivered()).strip('[]'))