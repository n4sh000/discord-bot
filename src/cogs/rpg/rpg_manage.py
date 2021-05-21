import sqlite3

class Item:
    def __init__(self):
        self.armors = {}
        self.weapons = {}
        self.items = {}
        self.keywords_armors = [
        'armor',
        'armors',
        'a',
        'arm',
        'amror',
        'amorr',
        'armosr',
        ]

        self.keywords_weapons = [
        'weapon',
        'weapons',
        'w',
        'wpn',
        'weapno',
        'wepaon',
        'weap',
        ]

        self.keywords_items = [
        'item',
        'items',
        'i',
        'itm',
        'ietm',
        'itme',
        'tiem',
        ]

    def section_parser(self, section: str):
        if section.lower() in self.keywords_armors:

            return 'ARMOR'

        elif section.lower() in self.keywords_weapons:
            return 'WEAPON'

        elif section.lower() in self.keywords_items:
            return 'ITEM'

        else:
            return False

    def get_armors(self,
        where='',
        inlist=False):
        with sqlite3.connect('/home/lvoidi/Desktop/discord/src/database/shop.db') as connect:
            cursor = connect.cursor()
            if where == '':

                cursor.execute(r'''
                                SELECT * FROM ARMOR 

                                ''')
            else:
                cursor.execute(f'''
                                SELECT * FROM ARMOR WHERE {where}
                                ''')        

            gotten = cursor.fetchall()
            if inlist:
                for got in gotten:
                    self.armors = [
                    got[0],
                    got[1],
                    got[2],
                    got[3],
                    got[4],
                    got[5],
                    got[6]
                    ]
                return self.armors
            if inlist == False:
                for got in gotten:
                    self.armors[got[1]] = {
                        'id' : got[0],
                        'producto' : got[1],
                        'descripcion' : got[2],
                        'precio' : got[3],
                        'nivel' : got[4],
                        'fase' : got[5],
                        'puntos de defensa' : got[6]
                    }
                return self.armors
            connect.commit()
            


    def get_weapons(self,
        where='',
        inlist=False):
        with sqlite3.connect('/home/lvoidi/Desktop/discord/src/database/shop.db') as connect:
            cursor = connect.cursor()
            if where == '':

                cursor.execute(r'''
                                SELECT * FROM WEAPON 

                                ''')
            else:
                cursor.execute(f'''
                                SELECT * FROM WEAPON WHERE {where}
                                ''')        

            gotten = cursor.fetchall()

            if inlist:
                for got in gotten:
                    self.weapons = [
                    got[0],
                    got[1],
                    got[2],
                    got[3],
                    got[4],
                    got[5],
                    got[6]
                    ]
                return self.weapons
            if inlist == False:
                for got in gotten:
                    self.weapons[f"{got[1]}"] = {
                        'id' : got[0],
                        'producto' : got[1],
                        'descripcion' : got[2],
                        'precio' : got[3],
                        'nivel' : got[4],
                        'fase' : got[5],
                        'puntos de defensa' : got[6]
                    }
                return self.weapons
            connect.commit()
            


    def get_items(self,
        where='',
        inlist=False):
        with sqlite3.connect('/home/lvoidi/Desktop/discord/src/database/shop.db') as connect:
            cursor = connect.cursor()
            if where == '':

                cursor.execute(r'''
                                SELECT * FROM ITEM 

                                ''')
            else:
                cursor.execute(f'''
                                SELECT * FROM ITEM WHERE {where}
                                ''')        

            gotten = cursor.fetchall()

            if inlist:
                for got in gotten:
                    self.weapons = [
                    got[0],
                    got[1],
                    got[2],
                    got[3],
                    got[4],
                    got[5]
                    ]

                return self.armors
            if inlist == False:
                for got in gotten:
                    self.items[f"{got[1]}"] = {
                        'id' : got[0],
                        'producto' : got[1],
                        'descripcion' : got[2],
                        'precio' : got[3],
                        'nivel' : got[4],
                        'fase' : got[5],
                    }
                return self.items
            connect.commit()

class User:
    def __init__(self):
        self.stats_list = []
        self.stats_dict = {}
        

    def get_by(self, username='', id=0, where='', inlist=False):
        with sqlite3.connect('/home/lvoidi/Desktop/discord/src/database/users_data.db') as con:
            cur = con.cursor()

            if where == '':
                if username != '':
                    cur.execute('SELECT * FROM USERS WHERE USERNAME={}'.format(username))

                if id != 0:
                    cur.execute('SELECT * FROM USERS WHERE ID={}'.format(id))

            else:
                if username != '':
                    cur.execute('SELECT * FROM USERS WHERE {}'.format(where))

                if id != 0:
                    cur.execute('SELECT * FROM USERS WHERE {}'.format(where))
            stats = cur.fetchall()

            con.commit()
        c = 0
        if inlist:
            for stat in stats:


                for x in range(len(stat)):
                    self.stats_list.append(stat[c])
                    c += 1
            return self.stats_list

        else:
            for stat in stats:
                self.stats_dict = {
                    'id' : stat[0],
                    'username' : stat[1],
                    'balance' : stat[2],
                    'nivel' : stat[3],
                    'fase' : stat[4],
                    'xp' : stat[5]
                }
            return self.stats_dict

class Inventory:
    def __init__(self):
        self.inventory_list = []
        self.inventory_dict = {}

    def fetch_inventory(self, where='', inlist=False, usr=''):
        with sqlite3.connect('/home/lvoidi/Desktop/discord/src/database/users_data.db') as connection:
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM {}_INV WHERE {}'.format(usr, where))
            items = cursor.fetchall()

            connection.commit()

        if inlist:
            for item in items:
                self.inventory_list.append(item[0])
                self.inventory_list.append(item[1])
                self.inventory_list.append(item[2])
                self.inventory_list.append(item[3])
                self.inventory_list.append(item[4])

            return self.inventory_list

        else:
            for item in items:
                self.inventory_dict[item[0]] = {
                'id' : item[0],
                'producto' : item[1],
                'uso' : item[2],
                'precio' : item[3],
                'repeticiones' : item[4],
                }
            return self.inventory_dict




class Rpg:
    def __init__(self):
        self.item = Item()
        self.user_class = User()
        self.inventory = Inventory()

    def inventory_insert(self, user: str, item: str, user_id: int):

        # Saca los datos necesarios del usuario
        usr = self.user_class.get_by(id=user_id)
        balance = usr.get('balance')
        username = usr.get('username')

        # Saca los datos necesarios del inventario
        inv = self.inventory.fetch_inventory(usr=username, where='REP>=0')
        list_items = []
        print(inv)
        
        keys = inv.keys()

        print(keys)

        for key in keys:
            dict_all = inv.get(key)
            repe = dict_all.get('repeticiones')
            if repe >=1:
                list_items.append({dict_all.get('producto') : dict_all})
                print(list_items)
            else:
                continue

        
        for dictionary in list_items:
            for k in dictionary.keys():
                dict_items = dictionary.get(k)
                rep = dict_items.get('repeticiones')
                price = dict_items.get('precio')

                print('rep: ', rep, 'price: ', price)

        with sqlite3.connect('/home/lvoidi/Desktop/discord/src/database/users_data.db') as connection:
            try:
                rep += 1
                print('new rep:', rep)
                cursor = connection.cursor()
                new_balance = balance - price
                print(new_balance, 'a', balance, 'p', price)
                cursor.execute(rf"UPDATE USERS SET BALANCE={new_balance} WHERE ID={user_id}")

                cursor.execute(rf'UPDATE {username}_INV SET REP={rep} WHERE PRODUCT="{item}"')

                connection.commit()

            except Exception as e:
                print(e, type(e).__name__)
                return False
