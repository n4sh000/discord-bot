import sqlite3

c = sqlite3.connect('/home/lvoidi/Desktop/discord/src/database/users_data.db')
cr = c.cursor()
"""
armors = [
     ('Armadura no tan dura',
      'Una simple armadura de cuero', 50, 1, 1, 10),
     ('Armadura de bronce',
      'Una armadura de bronce, simple mejora', 85, 1, 1, 15),
     ('Armadura sombria',
      'Armadura perfecta para cazar en la noche', 105, 1, 1, 15),
     (
          'Armadura de plomo',
          'Armadura hecha de plomo, bastante buena', 135, 2, 1, 37  
          ),
     (
          'Armadura de platino',
          'Armadura hecha de platino', 146,2,2,50
          ),
     (
          'Armadura de elixir',
          'Armadura hecha de elixir de la vida', 186,3,2,72
          ),
     
     (
          'Armadura del dragón',
          'Esta armadura se hizo con escamas del dragón', 200,3,2,84
          
          ),
]

weapons = [
     (
          'Palo',
          'Un palo que has encontrado en medio del bosque',
          0,
          1,
          1,
          10,
     ),
     (
          'Espada de madera',
          'Una espada de madera de roble',
          20,
          1,
          1,
          15,
     ),
     (
          'Espada de piedra',
          'Una espada de piedra básica',
          30,
          1,
          1,
          26,
     ),
     (
          'Espada de bronce',
          'Espada hecha de bronce',
          40,
          1,
          1,
          35,
     ),
     (
          'Espada de hierro',
          'Forjada con el hierro mas básico del mundo',
          70,
          2,
          1,
          43,
     ),
     (
          'Espada de acero inoxidable',
          'Forjada con uno de los mejores aceros encontrados',
          85,
          2,
          2,
          58,
     ),
     (
          'Espada encantada',
          'Esta espada está hecha del acero inoxidable, tiene mas poder que el anterior',
          100,
          3,
          2,
          70,
     ),
     (
          'Espada del exilio',
          'Espada hecha de escamas de dragón, capaz de terminar con vidas en segundos',
          120,
          3,
          2,
          82,
     ),
     (
          'Espada del oblivion',
          'No recuerdo donde encontré esta espada... maldita',
          70,
          4,
          2,
          95,
     ),
]

items = [
     (
          'Poción de curación',
          'Esta poción te curará 50Hp',
          20,
          1,
          1
     ),
     (
          'Poción de fuerza',
          'Esta poción te dará un 15%% de tu fuerza actual durante un día',
          40,
          2,
          1
     ),
     (
          'Poción de resistencia',
          'Esta poción te dará un 25%% de tu resistencia actual durante un día',
          40,
          2,
          1
     )
]
"""

cr.execute("CREATE TABLE USERS(ID INTEGER PRIMARY KEY, USERNAME VARCHAR(50) UNIQUE, BALANCE INTEGER, LEVEL INTEGER, STAGE INTEGER, XP INTEGER)")


c.commit()
c.close()