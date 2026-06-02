
'''
🔹 5. BMI hisoblash va tasnif
Vazifa: Foydalanuvchidan vazn (kg) va bo'y (m) so'rang. BMI ni hisoblang va tasniflang:

BMI < 18.5: "Kam vazn"
18.5 ≤ BMI < 25: "Normal vazn"
25 ≤ BMI < 30: "Ortiqcha vazn"
BMI ≥ 30: "Semizlik"
Formula: BMI = vazn / (bo'y)²

Qo'shimcha tekshiruvlar:

Vazn va bo'y musbat bo'lishi kerak
Bo'y 0.5-3.0 m oralig'ida bo'lishi kerak
Vazn 1-500 kg oralig'ida bo'lishi kerak
Misol:

Vazn: 70
Bo'y: 1.75
BMI: 22.86
Tasnif: Normal vazn
'''

vazn = float(input("Vazningizni kiriting (kg): "))
boy = float(input("Boyingizni kiriting (m): "))

if vazn >= 1 and vazn <=500:
    if boy >= 0.5 and boy <= 3.0:
        bmi = vazn / (boy ** 2)
        if bmi < 18.5:
            print("BMI: {:.2f}".format(bmi))
            print("Tasnif: Kam vazn")
        elif bmi < 25:
            print("BMI: {:.2f}".format(bmi))
            print("Tasnif: Normal vazn")
        elif bmi < 30:
            print("BMI: {:.2f}".format(bmi))
            print("Tasnif: Ortiqcha vazn")
        else:
            print("BMI: {:.2f}".format(bmi))
            print("Tasnif: Semizlik")
    else:
        print("Bo'y 0.5-3.0 m oralig'ida bo'lishi kerak")
else:
    print("Vazn 1-500 kg oralig'ida bo'lishi kerak")
