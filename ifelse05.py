
'''
🔹 5. Email manzilini tekshirish
Vazifa: Foydalanuvchidan email manzilini so'rang. Email quyidagi shartlarni bajarishi kerak:

@ belgisini o'z ichiga olishi
.com, .uz, .net yoki .org bilan tugashi
Agar to'g'ri bo'lsa, "Email qabul qilindi.", aks holda "Email noto'g'ri formatda." deb chiqaring.
'''

email = input("Email manzilingizni kiriting: ")
if ("@" in email) and ((".com" in email) or (".uz" in email) or (".net" in email) or (".org" in email)):
    print("Email qabul qilindi.")
else:
    print("Email noto'g'ri formatda.")