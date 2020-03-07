angry = True
bored = True
hungry = False
tired = False

# Example `if` statement
# (This is just an example, you'll have to do much more!)
if bored:
    print('T-Rex roars! RAWR!')
if angry and hungry and bored:
    print('eat triceratops')
elif tired and hungry:
   print ('eat Iguanadon')
elif tired:
   print ('sleeps')
elif angry and bored:
    print('fights  Velociraptor')
elif hungry and bored:
    print(' eats Stegasaurus')
elif angry or bored:
   print ('roars')
else:
    print('Gives a toothy smile')