import sys

print("Bienvenido a la isla del tesoro, juego desarollado por Andrea Elbittar \n")
print("Tu mision sera encontrar el tesoro oculto \n")
print ("Estas caminando desolado sin saber donde estas, llegas a un bosque oscuro, lleno de miedo logras ver dos (2) caminos. \n ¿Cual camino tomas? \n ¿(Derecha) o (Izquierda)?")
a1 = input()
if a1 == "derecha":
    print("Caiste en un agujero, gritas y nadie logra escucharte. Fin del juego! \n")
    sys.exit()
else: print("Al tomar el camino de la izquierda llegas a un lago, vez una isla en medio del lago \n ¿(Nadar) o (esperar)?")
a2 = input()
if a2 == "nadar":
   print("Fuiste atacado por una tribu, haz muerto. Fin del juego! \n")
   sys.exit()
else: print("Te quedaste a esperar!, vez un bote con alguien que se acerca, que haces? \n (Llamarlo) o (esconderce)?")
a3 = input()
if a3 == "llamarlo":
    print("Haz llamado a un miembro de la tribu, te han atacado y has muerto. Fin del juego! \n")
    sys.exit()
else: print("Al esconderte logras ver bote oculto en la maleza. \n Logras llegar a la pequeña isla. \n Caminas y logras ver una casa en medio de la isla. \n ¿Que haces? \n ¿Caminas hacia la casa (directamente) o la (rodeas)?")
a4 = input()
if a4 == "rodeas":
    print("Al intentar rodear la casa un miembro de la tribu te a visto y te han atacado!, Haz muerto. Fin del juego!")
else: print("Logras llegar a la casa, vez que se acercan personas peligrosas y decides entras a la casa! \n Pero espera hay tres (3) puertas \n Una roja, una amarilla y una azul, ¿Cual vas a abrir?")
a5 = input()
if a5 == "roja":
    print("Haz sido quemado. Fin del juego! \n")
    sys.exit()
if a5 == "azul":
    print("Haz sido deborado por bestias. Fin del juego! \n")
    sys.exit()
if a5 == "amarilla":
    print("Haz entrado a la casa y conseguiste el tesoro, Haz ganado! \n")
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')