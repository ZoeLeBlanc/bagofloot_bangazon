class Child(object):

    def __init__(self, toy, name):
        self.name = name
        self.toys = [toy]
        self.delivery_status = False

    def add_toy(self, toy):
        self.toys.append(toy)

    def remove_toy(self, toy):
        self.toys.remove(toy)

    def change_delivery_status(self, status):
        self.delivery_status = status

    def get_all_toys(self):
        return self.toys

    def remove_all_toys(self):
        self.toys = []

    # def __str__(self):
    #     return "{} has {}, which has the delivery status of {}". format(self.name, str(self.toys).strip('[]'), self.delivery_status)
