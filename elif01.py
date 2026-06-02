
'''
🔹 1. Baholash tizimi
Vazifa: Foydalanuvchidan ball (0-100) so'rang va bahoni chiqaring:

90-100: "A (A'lo)"
80-89: "B (Yaxshi)"
70-79: "C (Qoniqarli)"
60-69: "D (Qoniqarsiz)"
0-59: "F (Rad)"
Agar 0-100 oralig'idan tashqari son kiritilsa, "Ball 0-100 oralig'ida bo'lishi kerak!" deb chiqaring.
'''

ball = int(input("Ballni kiriting (0-100): "))
if 0 <= ball <= 100:
    if ball >= 90:
        print("A (A'lo)")
    elif ball >= 80:
        print("B (Yaxshi)")
    elif ball >= 70:
        print("C (Qoniqarli)")
    elif ball >= 60:
        print("D (Qoniqarsiz)")
    else:
        print("F (Rad)")
else:
    print("Ball 0-100 oralig'ida bo'lishi kerak!")