x = 3
if x==0:   #Проверка если
    print('if')
elif x > 0:
    print('elif')
else:
    print('else')
    
y = 5 
if y == 0:
    y+= 1
print(5/y)



q = 20

if q == 0:
    q == 1
    print('q равен нулю')

elif type(q) == type(5) or type(q) == type(5.5): # and и or 
    print ('q допустимое число')

else:
    print('В q не допустимый тип данных')
    q = 1

print(100/q)
