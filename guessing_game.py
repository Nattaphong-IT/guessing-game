import random

# ฟังก์ชันที่ให้คำแนะนำในการทาย
def start_game():  # ต้องมีวงเล็บหลังชื่อฟังก์ชัน

    print("ยินดีต้อนรับสู่เกมทายตัวเลข!")
    print("ฉันได้เลือกตัวเลขระหว่าง 1 ถึง 100 ลองทายดูว่าคือเลขอะไร!")

    # สุ่มตัวเลขระหว่าง 1 ถึง 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        # ให้ผู้ใช้กรอกเลขทาย
        try:
            user_guess = int(input("ทายเลขของคุณ: "))
        except ValueError:
            print("กรุณากรอกตัวเลขเท่านั้น!")
            continue
        
        attempts += 1
        
        # ตรวจสอบว่าผู้ใช้ทายถูกหรือไม่
        if user_guess < number_to_guess:
            print("ทายต่ำเกินไป! ลองใหม่อีกครั้ง.")
        elif user_guess > number_to_guess:
            print("ทายสูงเกินไป! ลองใหม่อีกครั้ง.")
        else:
            print(f"ยินดีด้วย! คุณทายถูกต้องใน {attempts} ครั้ง.")
            break

# เรียกฟังก์ชันเพื่อเริ่มเกม
if __name__ == "__main__":
    start_game()  # ต้องมีวงเล็บ
