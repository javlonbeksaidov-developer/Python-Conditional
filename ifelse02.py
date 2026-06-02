
'''
🔹 2. Parol tekshiruvi
Vazifa: Foydalanuvchidan parol kiritsini so'rang. Parol quyidagi shartlarni bajarishi kerak:

Kamida 8 belgidan iborat bo'lishi
Kamida 1 harf va 1 raqam bo'lishi kerak
Agar parol to'g'ri bo'lsa, "Parol qabul qilindi.", aks holda "Parol noto'g'ri. Kamida 8 belgi, 1 harf va 1 raqam bo'lishi kerak." deb chiqaring.

Maslahat: isalpha(), isdigit(), len() funksiyalaridan foydalaning.
'''

password = input("Parolni kiriting: ")

if len(password) < 8:
    print("Parol juda qisqa. Kamida 8 ta belgidan iborat bo'lishi kerak.")
else:
    if password.isalpha():
        print("Parol faqat harflardan iborat. Raqamlar yoki maxsus belgilar qo'shishni o'ylab ko'ring.")
    else:
        if password.isdigit():
            print("Parol faqat raqamlardan iborat. Harflar yoki maxsus belgilar qo'shishni o'ylab ko'ring.")
        else:
            print("Parol qabul qilindi.")