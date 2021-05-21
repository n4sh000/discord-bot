import sqlite3


class Rpg:
    def shop_item(self, id: int, section: str):
        """[summary]

        Args:
            id (Integer): The id of the product
            section (String): The section of the product (armor, weapon, item)
        """
        if section.lower() == "armor":
            sec = 'ARMOR'
        elif section.lower() == "weapon":
            sec = 'WEAPON'
        elif section.lower() == 'item':
            sec = 'ITEM'
        else:
            print("No entro")
            return False

        connection = sqlite3.connect('/home/lvoidi/Desktop/discord/src/database/shop.db')
        cursor = connection.cursor()

        cursor.execute(rf'SELECT * FROM {sec} WHERE ID={id}')

        the_item = cursor.fetchall()
        print("confirmacion de error en {}".format(the_item))
        for c in the_item:
            self.name = c[1]
            self.price = c[3]
            self.lvl = c[4]
            self.stg = c[5]

        print("Logró imprimir los items: {}".format(self.name))
        connection.commit()
        connection.close()

        return [self.name, self.price, self.lvl, self.stg]

    def get_user_stats(self, userid: int):
        """[summary]

        Args:
            userid (int): id del usuario

        Returns:
            List: List with user stats
        """
        self.id = userid
        with sqlite3.connect('/home/lvoidi/Desktop/discord/src/database/users_data.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM USERS WHERE ID={}'.format(userid))
            the_stats = cursor.fetchall()

            connection.commit()

        for stat in the_stats:
            self.username = stat[1]
            self.user_balance = stat[2]
            self.user_level = stat[3]
            self.user_stage = stat[4]
            self.user_xp = stat[5]

        return [self.username, self.user_balance, self.user_level, self.user_stage, self.user_xp]

    def is_valid(self, user_id):
        """[summary]

        Args:
            user_id (int): id del usuario

        Returns:
            Bool: If user has valid stats, returns True, except if there's an invalid stat
        """

        stats = self.get_user_stats(user_id)
        print(self.price, self.lvl, self.stg, "\n Los stats del jugador: ", stats[1], stats[2], stats[3])
        if stats[1] > self.price and stats[2] >= self.lvl and stats[3] >= self.stg:
            return True
        else:
            return False

    def inventory_insert(self, username: str, item: str):
        with sqlite3.connect('/home/lvoidi/Desktop/discord/src/database/users_data.db') as connection:
            try:
                cursor = connection.cursor()
                new_balance = self.user_balance - self.price
                print("\n\na XD")
                cursor.execute(rf"UPDATE USERS SET BALANCE={new_balance} WHERE ID={self.id}")
                print(rf"UPDATE USERS SET BALANCE={new_balance} WHERE ID={self.id}")
                cursor.execute(rf'INSERT INTO {username}_INV VALUES ("{item}", "f")')

                connection.commit()
            except Exception as e:
                print(e, type(e).__name__)
                return False

    def get_inventory(self, usr):
        try:
            with sqlite3.connect('/home/lvoidi/Desktop/discord/src/database/users_data.db') as con:
                cursor = con.cursor()
                inv = self.get_user_stats(userid=usr)

                cursor.execute(f"SELECT * FROM {inv[0]}_INV")

                the_inventory = cursor.fetchall()
                con.commit()
                for item in the_inventory:
                    string_1 = f'{item[0]}'
                    if item[1].lower() == 'f':
                        string_2 = 'Aun no está en uso'
                    else:
                        string_2 = 'Está en uso actualmente'

                return string_1, string_2
        except (UnboundLocalError, Exception):
            return False
