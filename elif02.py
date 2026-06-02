
'''
🔹 2. Sodda kalkulyator
Vazifa: Foydalanuvchidan ikkita son va amalni (+, -, *, /) so'rang. Hisoblashni bajaring.

Agar bo'lishda ikkinchi son 0 bo'lsa: "Nolga bo'lish mumkin emas!"
Noto'g'ri amal kiritilsa: "Noto'g'ri amal. Faqat +, -, *, / ishlatiladi."
Misol:

1-son: 10
2-son: 3  
Amal: +
Natija: 10 + 3 = 13
'''

frist_num = int(input("Birinchi sonni kiriting: "))
second_num = int(input("Ikkinchi sonni kiriting: "))
amal = input("Amalni kiriting (+, -, *, /): ")

if amal == "+":
    natija = frist_num + second_num
    print(f"{frist_num} + {second_num} = {natija}")
elif amal == "-":
    natija = frist_num - second_num
    print(f"{frist_num} - {second_num} = {natija}")
elif amal == "*":
    natija = frist_num * second_num
    print(f"{frist_num} * {second_num} = {natija}")
elif amal == "/":
    if second_num != 0:
        natija = frist_num / second_num
        print(f"{frist_num} / {second_num} = {natija}")
    else:
        print("Nolga bo'lish mumkin emas!")
else:
    print("Noto'g'ri amal. Faqat +, -, *, / ishlatiladi.")