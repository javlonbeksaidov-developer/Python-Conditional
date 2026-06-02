
'''
🔹 3. Fayl mavjudligini tekshirish
Vazifa: Foydalanuvchidan fayl nomini so'rang. Agar fayl mavjud bo'lsa, "Fayl '<fayl nomi>' mavjud.", aks holda "Fayl '<fayl nomi>' topilmadi." deb chiqaring.

Maslahat: os.path.exists() funksiyasidan foydalaning.

import os
'''

import os
file = input("Fayl nomini kiriting: ")

if os.path.exists(file):
    print(f"Fayl '{file}' mavjud.")
else:
    print(f"Fayl '{file}' topilmadi.")