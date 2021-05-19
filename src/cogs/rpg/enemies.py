import random
from time import sleep
class Enemy:
     def __init__(self):
          self.hp = 0
          self.ap = 0
          self.list = {
               # Monstruos de la fase 1
               'Goblin' : {
                    'hp' : 50,
                    'ap' : 20,
                    'stage' : 1,
                    'rewards' : {
                         'XP' : random.randint(7,14),
                         'Money' : random.randint(3,9)
                    }
               },
               'Verdugo' : {
                    'hp' : 100,
                    'ap' : 30,
                    'stage' : 1,
                    'rewards' : {
                         'XP' : random.randint(10,25),
                         'Money' : random.randint(6,14)
                    }
               },
               'Zombie pirata' : {
                    'hp' : 125,
                    'ap' : 50,
                    'stage' : 1,
                    'rewards' : {
                         'XP' : random.randint(20,34),
                         'Money' : random.randint(15,24)
                    }
               }
               
          }
          
     def attack(
          self,
          user_hp=None,
          user_rp=None,
          enemy_ap=None,
          ):
          """[summary]

          Args:
              user_hp (Int, optional): [Puntos de vida usuario]. Defaults to None.
              user_rp ([Int], optional): [puntos de resistencia]. Defaults to None.
              enemy_ap ([Int], optional): [Puntos de ataque del enemigo]. Defaults to None.
          """
          new_enemy_atack_points_pc = 100-((user_rp/enemy_ap)*100)
          print(new_enemy_atack_points_pc, '%')
          enemy_attack_pt = (new_enemy_atack_points_pc/100)*enemy_ap
          
          print('antiguo: ', enemy_ap, '\nnuevo: ', enemy_attack_pt)
          
          counter = 0
          for x in range(random.randint(4,6)):
               counter += 1
               print(f'Hp del usuario: {user_hp}, el enemigo ataca: te quita {enemy_attack_pt} HP', end='\n')
               if counter == 1:
                    user_hp -= enemy_attack_pt
                    enemy_attack_pt -= enemy_attack_pt/random.randint(2,5)
               else:
                    enemy_attack_pt -= enemy_attack_pt/random.randint(4,10)
                    user_hp -= enemy_attack_pt
               sleep(1)
               if user_hp <= 0:
                    print("\n\n\nHas muerto")
                    return
          print(f'Has ganado el duelo, has quedado con {user_hp} vida')
          
Enemigo = Enemy()
Enemigo.attack(
     user_hp=25,
     user_rp=90,
     enemy_ap=100
)