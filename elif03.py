
'''
🔹 3. Kun davomidagi vaqt
Vazifa: Soatni (0-23) so'rang va vaqt oralig'ini aniqlang:

5-11: "Ertalab"
12-17: "Kunduzi"
18-21: "Kechqurun"
22-4: "Tun"
Agar 0-23 oralig'idan tashqari son kiritilsa, "Soat 0-23 oralig'ida bo'lishi kerak!" deb chiqaring.
'''

soat = int(input("Soatni kiriting (0-23): "))
if 0 <= soat <=23:
    if 5 <= soat < 12:
        print("Ertalab")
    elif 12 <= soat < 18:
        print("Kunduz")
    elif 18 <= soat < 22:
        print("Kechqurun")
    else:
        print("Tun")
else:
    print("Soat 0-23 oralig'ida bo'lishi kerak!")
   