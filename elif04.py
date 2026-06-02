
'''
🔹 4. Transport tanlash
Vazifa: Masofani (km) so'rang va transportni tavsiya qiling:

0-1 km: "Piyoda yuring"
1-5 km: "Velosiped yoki elektr skuter"
5-50 km: "Avtobus yoki mashina"
50+ km: "Poyezd yoki samolyot"
Manfiy masofa kiritilsa, "Masofa manfiy bo'la olmaydi!" deb chiqaring.
'''

masofa = float(input("Masofani kiriting (km): "))
if masofa >= 0:
    if masofa <= 1:
        print("Piyoda yuring")
    elif masofa <= 5:
        print("Velosiped yoki elektr skuter")
    elif masofa <= 50:
        print("Avtobus yoki mashina")
    else:
        print("Poyezd yoki samolyot")
else:
    print("Masofa manfiy bo'la olmaydi!")
    