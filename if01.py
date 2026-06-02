
'''
🔹 1. Absolyut qiymat
Vazifa: Foydalanuvchidan butun son kiritsini so'rang. Agar son manfiy bo'lsa, uni musbatga o'zgartirib chiqaring. Faqat if dan foydalaning.

Misol:

Kirish: -5
Chiqish: 5
'''

son = int(input("Son kiriting: "))
if son < 0:
    son = -son

print(f"Absolyut qiymat: {son}")