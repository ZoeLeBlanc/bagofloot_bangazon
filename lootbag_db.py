import sqlite3

class Lootbag(object):

    def __init__(self):
        print(self)

    def create_bag(self, name):
        print("working")
        with sqlite3.connect('bagofloot.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO Lootbag VALUES (?, ?)", (None, name))
            try:
                c.execute("SELECT Name FROM Lootbag WHERE Name='{}'".format(name))
                selected_bag = c.fetchall()
            except sqlite3.OperationalError:
                pass
        conn.close()

    def remove_child(self, child, bag):
        with sqlite3.connect('bagofloot.db') as conn:
            c = conn.cursor()
            c.execute("SELECT LootbagId FROM Lootbag WHERE Name='{}'".format(bag))
            selected_bag = c.fetchall()
            try:
                c.execute("DELETE FROM Child  WHERE LootbagId={} AND Name='{}'".format(selected_bag[0][0], child))
            except sqlite3.OperationalError:
                pass
        conn.close()

    def get_toy_list(self, bag):
        with sqlite3.connect('bagofloot.db') as conn:
            c = conn.cursor()
            c.execute("SELECT t.Name FROM Toy t, Lootbag l, Child c WHERE l.Name='{}' and l.LootbagId = c.LootbagId and c.ChildId = t.Childid".format(bag))
            selected_toys = c.fetchall()
            print(selected_toys)
        conn.close()

    def get_all_kids(self, bag):
        with sqlite3.connect('bagofloot.db') as conn:
            c = conn.cursor()
            c.execute("SELECT c.Name FROM Lootbag l, Child c WHERE l.Name='{}' and l.LootbagId = c.LootbagId".format(bag))
            selected_kids = c.fetchall()
            print(selected_kids)
        conn.close()

    def toys_delivered(self, bag):
        with sqlite3.connect('bagofloot.db') as conn:
            c = conn.cursor()
            c.execute("SELECT COUNT(t.ToyId) FROM Lootbag l, Child c, Toy t WHERE l.Name='{}' and l.LootbagId = c.LootbagId and c.ChildId = t.ChildId and c.ChildId={}".format(bag, 1))
            delivered_toys = c.fetchall()
            print(delivered_toys)
        conn.close()

    