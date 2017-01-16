class Lootbag(object):

    def __init__(self):
        self.children = set()
        self.all_toys = []

    def add_child(self, child):
        print(child)
        self.children.add(child)

    def remove_child(self, child):
        self.children.remove(child)

    def update_toys(self):
        for child in self.children:
            self.all_toys.extend(child.toys)

    def get_toy_list(self):
        return self.all_toys

    def get_all_kids(self):
        kids = []
        for child in self.children:
            kids.append(child.name)
        return kids

    def __str__(self):
        return "This bag has these children: {} and these toys: {}".format(str(self.get_all_kids()).strip('[]'), str(self.get_toy_list()).strip('[]'))