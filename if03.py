
'''
🔹 3. Bo'linuvchanlikni tekshirish
Vazifa: Foydalanuvchidan son kiritsini so'rang. Shu son:

2 ga bo'linishini
3 ga bo'linishini
5 ga bo'linishini
alohida if lar bilan tekshiring va har bir holat uchun alohida xabar chiqaring.

Misol:

Kirish: 30
Chiqish: 
30 soni 2 ga bo'linadi
30 soni 3 ga bo'linadi
30 soni 5 ga bo'linadi
'''

son = int(input("Son kiriting: "))
if son % 2 == 0:
    print(f"{son} soni 2 ga bo'linadi")
    
if son % 3 == 0:
    print(f"{son} soni 3 ga bo'linadi")

if son % 5 == 0:
    print(f"{son} soni 5 ga bo'linadi")
