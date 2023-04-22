animaux = [" girafe ", " tigre ", " singe ", " souris "]
tailles = [5 , 2.5 , 1.75 , 0.15]
mixte = [" girafe ", 5, " souris " , 0.15]

print(animaux)
print(tailles)
print(mixte)

print()
print( animaux [0])
print(tailles[1])
print(mixte[2])

print()
ani1 = [" girafe ", " tigre "]
ani2 = [" singe ", " souris "]
print( ani1 + ani2)
print( ani1 * 3)

print()
a = []
print(a)
a = a + ['i']
print(a)
a = a + ['le suivant']
print(a)

x = [0 , 1, 2, 3, 4, 5 , 6 , 7, 8, 9]
print()
x [::1]
print(x)
x [::2]
print(x)
x [1:6:3]
print(x)

print()
l =  list ( range (10))
print(l)
liste = list ( range (0 , 5))
print(liste)
l =  list ( range (0 , 1000 , 200))
print(l)
l = list ( range (2 , -2, -1))
print(l)
l =  list ( range (10 ,0 , -1))
print(l)

print()
enclos1 = [" girafe ", 4]
enclos2 = [" tigre " , 2]
enclos3 = [" singe " , 5]
zoo = [ enclos1 , enclos2 , enclos3 ]
print(zoo)

liste = list ( range (10))
print(max(liste), min(liste), sum(liste))

print("######## Exercices ########")
print()
print("######## Exercice 1  ########")
liste_semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
print(f'les 7 jours de la semaine sont {liste_semaine}')
jours_semaine = liste_semaine[0:5]
week_end = liste_semaine[5:7]
print(f'les jours de la semaine sont : {jours_semaine}')
print(f'les jours du week-end sont : {week_end}')
jours_semaine = liste_semaine[-7:-2]
week_end = liste_semaine[-2::]
print(f'les jours de la semaine sont : {jours_semaine}')
print(f'les jours du week-end sont : {week_end}')
dernier = liste_semaine[-1]
dernier_jr = liste_semaine[6]
print(f'le dernier jour de la semaine est : {dernier}')
print(f'le dernier jour de la semaine est : {dernier_jr}')
jours_semaine = liste_semaine[:7:]
print(jours_semaine)

print()
print("######## Exercice 2  ########")

hiver = ['Janvier', 'Fevrier', 'Mars']
printemps = ['Avril', 'Mai', 'Juin']
ete = ['Juillet', 'Aout', 'Septembre']
automne = ['Octobre', 'Novembre', 'Decembre']

saisons = ['hiver', 'printemps', 'ete', 'automne']

print(saisons[2])
print(saisons[1][0])
print(saisons[1:2])
print(saisons[:][1])

print()
print("######## Exercice 3  ########")

print('La table de multiplication par 9 ')
table = list (range (0 , 99, 9))
print(table)

print()
print("######## Exercice 4  ########")
print(f' le nombre des nombres pairs dans l\’intervalle [2, 10000] est : {len(list(range(0,10000,2)))}')

