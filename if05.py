
'''
🔹 5. Haroratga mos maslahat
Vazifa: Foydalanuvchidan haroratni (°C) so'rang va maslahat bering:

0°C dan past: "Juda sovuq! Issiq kiyim kiying."
0-14°C orasida: "Sovuq. Kurtka kiying."
15°C va undan yuqori: "Ob-havo yaxshi."
Har bir shartni alohida if bilan tekshiring.
'''

harorat = int(input("Haroratni kiriting: "))
if harorat < 0:
    print("Juda sovuq! Issiq kiyim kiying.")
    
if 0 <= harorat < 15:
    print("Sovuq. Kurtka kiying.")
    
if harorat >= 15:
    print("Ob-havo yaxshi.")