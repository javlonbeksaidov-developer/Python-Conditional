
'''
🔹 4. Bank hisobini tekshirish
Vazifa: Hisobingizda 5000 so'm bor. Foydalanuvchidan yechmoqchi bo'lgan summani so'rang.

Agar mablag' yetarli bo'lsa: "Pul yechildi. Qolgan balans: X so'm"
Yetarli bo'lmasa: "Mablag' yetarli emas. Sizning balansingiz: 5000 so'm"
Qo'shimcha: Manfiy son kiritilsa, "Manfiy summa kiritib bo'lmaydi." deb chiqaring.
'''

mablag = 5_000
summa = int(input("Summani kiriting: "))
if summa >= 0:
    if summa <= mablag:
        qolgan_balans = mablag - summa
        print(f"Pul yechildi. Qolgan balans: {qolgan_balans} so'm")
    else:
        print(f"Mablag' yetarli emas. Sizning balansingiz: {mablag} so'm")
else:
    print("Manfiy summa kiritib bo'lmaydi.")