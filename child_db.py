import sqlite3

class Child(object):

    def __init__(self):
        print(self)

    def create_child(self, toy, child, bag):
        with sqlite3.connect('bagofloot.db') as conn:
            c = conn.cursor()
            c.execute("SELECT LootbagId FROM Lootbag WHERE Name='{}'".format(bag))
            selected_bag = c.fetchall()
            print(selected_bag)
            try: 
                c.execute("INSERT INTO Child VALUES (?, ?, ?, ?)", (None, child, 0, selected_bag[0][0]))
            except sqlite3.OperationalError:
                pass
            c.execute("SELECT ChildId FROM Child WHERE Name='{}'".format(child))
            selected_child = c.fetchall()
            print(selected_child)
            try:
                c.execute("INSERT INTO Toy VALUES (?, ?, ?)", (None, toy, selected_child[0][0]))
            except sqlite3.OperationalError:
                pass
        conn.close()        

    def add_toy(self, child, toy):
        with sqlite3.connect('bagofloot.db') as conn:
            c = conn.cursor()
            c.execute("SELECT ChildId FROM Child WHERE Name='{}'".format(child))
            selected_child = c.fetchall()
            print(selected_child)
            try:
                c.execute("INSERT INTO Toy VALUES (?, ?, ?)", (None, toy, selected_child[0][0]))
            except sqlite3.OperationalError:
                pass
        conn.close()

    def remove_toy(self, child, toy):
        with sqlite3.connect('bagofloot.db') as conn:
            c = conn.cursor()
            c.execute("SELECT ChildId FROM Child WHERE Name='{}'".format(child))
            selected_child = c.fetchall()
            try:
                c.execute("DELETE FROM Toy  WHERE ChildId={} AND Name='{}'".format(selected_child[0][0], toy))
            except sqlite3.OperationalError:
                pass
        conn.close()

    def change_delivery_status(self, child, status):
        print(status)

        if status == True:
            status_int = 1
        else:
            status_int = 0
        print(status_int)
        with sqlite3.connect('bagofloot.db') as conn:
            c = conn.cursor()
            c.execute("""UPDATE Child
                SET DeliveryStatus = {}
                WHERE Name='{}'
                """.format(status_int, child))
        conn.close()

    def get_all_toys(self, child):
        with sqlite3.connect('bagofloot.db') as conn:
            c = conn.cursor()
            c.execute("SELECT t.Name FROM Toy t, Child c WHERE c.Name='{}' and c.ChildId = t.Childid".format(child))
            selected_toys = c.fetchall()
            print(selected_toys)
        conn.close()

    def remove_all_toys(self, child):
        with sqlite3.connect('bagofloot.db') as conn:
            c = conn.cursor()
            c.execute("SELECT ChildId FROM Child WHERE Name='{}'".format(child))
            selected_child = c.fetchall()
            try:
                c.execute("DELETE FROM Toy  WHERE ChildId={}".format(selected_child[0][0]))
            except sqlite3.OperationalError:
                pass
        conn.close()

    # def __str__(self):
    #     return "{} has {}, which has the delivery status of {}". format(self.name, str(self.toys).strip('[]'), self.delivery_status)
