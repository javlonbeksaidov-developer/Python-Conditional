
'''
🔹 4. Yoshga bog'liq chegirma
Vazifa: Chipta narxi 100 so'm. Foydalanuvchidan yoshini so'rang va chegirmani qo'llang:

7 yoshgacha (0-6): 50% chegirma
7-17 yosh: 20% chegirma
60 yoshdan katta: 30% chegirma
Yakuniy narxni chiqaring. Faqat if ishlating (bir nechta if dan foydalanish mumkin).

Misol:

Kirish: 5
Chiqish: Yakuniy narx: 50 so'm (50% chegirma qo'llanildi)
'''

chek_format = "Yakuniy narx: {} so'm ({}% chegirma qo'llanildi)"
chipta_narxi = 100
yosh = int(input("Yoshingizni kiriting: "))
if yosh < 7:
    chegirma = chipta_narxi * 0.5
    yakuniy_narx = chipta_narxi - chegirma
    print(chek_format.format(yakuniy_narx, 50))

if 7 <= yosh <= 17:
    chegirma = chipta_narxi * 0.2
    yakuniy_narx = chipta_narxi - chegirma
    print(chek_format.format(yakuniy_narx, 20))

if yosh > 60:
    chegirma = chipta_narxi * 0.3
    yakuniy_narx = chipta_narxi - chegirma
    print(chek_format.format(yakuniy_narx, 30))