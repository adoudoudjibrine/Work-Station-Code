# To avoid return on line we have to use end
print('Hello Word')
print('Hello Word', end="")# Here we use end to avoid back to the line

print('Hello Word');print('Hello Word')
print('Hello Word',end="");print('Hello Word')

a = 32
nom = 'Darsa'
prenom = 'abdallah'
print(nom , "a" , a ," ans")
print(nom , "a" , a ,"ans", sep='')
print(nom , "a" , a ,"ans", sep='-')

print(nom, prenom)
print(nom,prenom, sep='')
print(nom + prenom)

print(f'{nom} a  {a} ans')


prop_GC = (4500 + 2575)/14800
print('la proportion de GC est : ', prop_GC)
print(f'la proportion de GC est : {prop_GC:.2f} ')#Showing float nmber 
print(f'la proportion de GC est : {prop_GC:.3f} ')
print(f'la proportion de GC est : {prop_GC:.16f} ')

nb_G = 4500
nb_C = 2575
print(f'Ce genome contient {nb_G:d} G et {nb_C:d} C soit une prop de GC de {prop_GC:.2f} ')
perc_GC = prop_GC * 100
print(f'Ce genome contient {nb_G:d} G et {nb_C:d} C soit un %GC de {perc_GC:.2f} ')

print(10);print(1000)
print(f"{10:>6d}");print(f'{1000:>6d}')
print(f"{10:<6d}");print(f'{1000:<6d}')
print(f"{10:^6d}");print(f'{1000:^6d}')
print(f"{10:*^6d}");print(f'{1000:*^6d}')
print(f"{10:0>6d}");print(f'{1000:0>6d}')

print(f'{nom}');print(f'prenom')
print(f'{nom:}');print(f'prenom')

print(f' {prop_GC:7.3f} ')
print(f' {prop_GC:10.3f} ')

print(f'Le resultat de 5*5 est : {5 * 5}')
print(f'Le resultat de l\'operation est : {5.3 * 5}')

print('######### Exercices 2 ########')

adn = 'A'
print(adn * 20)

adn = 'A'* 20 + 'GC' * 40
print(adn)

a = 'Salut'
b = 102
c = 10.318
print(f"a egale a '{a}', b vaut {b} et c vaut {c:.2f}")

perc_GC = ((4500 +2575)/14800)*100
print(f"Le pourcentage de GC est de {perc_GC:.0f}{'%':>6s}")
print(f"Le pourcentage de GC est de {perc_GC:.1f}{'%':>4s}")
print(f"Le pourcentage de GC est de {perc_GC:.2f}{'%':>3s}")
print(f"Le pourcentage de GC est de {perc_GC:.3f}{'%':>2s}")


