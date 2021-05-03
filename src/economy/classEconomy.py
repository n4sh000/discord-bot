# import sqlite3
import random


class User_economy:
    def __init__(self):
        self.money = 0
    def failure_work(self):
        self.failure_works = {
            1: "No lograste conseguir trabajo",
            2: "Trabajaste de dependiente en una tienda pero fuiste asaltado, perdiendolo todo",
            3: "Intentaste trabajar cuidando perros pero atropellaron el perro de uno de tus clientes",
            4: "Viste una oportunidad para trabajar como oficinista en una empresa pero no pudiste por tu falta de estudios universitarios",
            5: "Trabajaste como programador pero entregaste un trabajo lleno de bugs",
            6: "No conseguiste trabajo debido a tu falta de estudios"
        }
        self.random_state = self.failure_works.get(random.randint(1,6))
        self.random_lost = random.randint(-244,-128)
        self.money += self.random_lost
    def succesful_work(self):
        self.succesful_works = {
            1:"Hiciste un muy buen trabajo atendiendo en un call center",
            2:"Entregaste un muy buen front-end en una página web",
            3:"Trabajas en un mcdonalds y obtienes un sueldo decente",
            4:"Trabajas en un uber eats y logras hacer bastantes entregas",
            5:"Consigues que tu jefe te ascienda en tu trabajo como oficinista",
            6:"Trabajas como profesor en una universidad",
            7:"Puedes trabajar y ganar un poco como dependiente de una tienda",
            8:"Consigues un trabajo freelance en fiverr"
            
        }
        self.random_success = self.succesful_works.get(random.randint(1,8))
        self.gained = random.randint(128,244)
        self.money += self.gained
    def random_selection(self):
        if random.randint(1,2) is 2:
            self.failure_work()
            self.selection="l"
            return f"{self.random_state} y {self.random_lost}"
            
        elif random.randint(1,2) is 1:
            self.succesful_work()           
            self.selection = "w"
            return f"{self.random_success} y {self.gained}"

