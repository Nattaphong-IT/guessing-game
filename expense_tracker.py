# expense_tracker.py

# ฟังก์ชันสำหรับการแสดงเมนู
def show_menu():
    print("โปรแกรมบันทึกค่าใช้จ่าย")
    print("1. เพิ่มค่าใช้จ่าย")
    print("2. แสดงค่าใช้จ่ายทั้งหมด")
    print("3. คำนวณยอดรวมค่าใช้จ่าย")
    print("4. ออกจากโปรแกรม")

# ฟังก์ชันสำหรับเพิ่มค่าใช้จ่าย
def add_expense(expenses):
    name = input("ป้อนชื่อของค่าใช้จ่าย: ")
    amount = float(input("ป้อนจำนวนเงินค่าใช้จ่าย: "))
    expenses.append({"name": name, "amount": amount})
    print("เพิ่มค่าใช้จ่ายเรียบร้อยแล้ว!")

# ฟังก์ชันสำหรับแสดงค่าใช้จ่ายทั้งหมด
def show_expenses(expenses):
    if len(expenses) == 0:
        print("ยังไม่มีค่าใช้จ่ายบันทึกไว้")
    else:
        print("ค่าใช้จ่ายทั้งหมด:")
        for expense in expenses:
            print(f"{expense['name']}: {expense['amount']} บาท")

# ฟังก์ชันสำหรับคำนวณยอดรวมค่าใช้จ่าย
def calculate_total(expenses):
    total = sum(expense['amount'] for expense in expenses)
    print(f"ยอดรวมค่าใช้จ่ายทั้งหมด: {total} บาท")

# ฟังก์ชันหลัก
def main():
    expenses = []  # ลิสต์เก็บค่าใช้จ่ายทั้งหมด
    while True:
        show_menu()
        choice = input("เลือกตัวเลือก (1-4): ")
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            show_expenses(expenses)
        elif choice == '3':
            calculate_total(expenses)
        elif choice == '4':
            print("ขอบคุณที่ใช้โปรแกรม!")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")

# เรียกใช้ฟังก์ชันหลัก
if __name__ == "__main__":
    main()
