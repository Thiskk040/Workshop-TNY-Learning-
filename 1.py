def calculate_price(age, movie, day, people):
    # ราคาในวันธรรมดา (จันทร์-พฤหัสบดี)
    weekday_prices = {
        "Frozen": {"adult": 719, "child": 649},
        "Marvel": {"adult": 719, "child": 649},
    }

    # ราคาในวันสุดสัปดาห์ (ศุกร์-อาทิตย์ และวันหยุดนักขัตฤกษ์)
    weekend_prices = {
        "Frozen": {"adult": 879, "child": 789},
        "Marvel": {"adult": 879, "child": 789},
    }

    # ตรวจสอบวันว่าเป็นวันธรรมดาหรือสุดสัปดาห์
    if day.lower() in ["friday", "saturday", "sunday", "holiday"]:
        prices = weekend_prices
    else:
        prices = weekday_prices

    # ตรวจสอบว่าเป็นผู้ใหญ่หรือเด็ก
    if age >= 18:
        ticket_type = "adult"
    else:
        ticket_type = "child"

    # คำนวณราคาสำหรับคนที่เลือก
    price_per_person = prices[movie][ticket_type]
    total_price = price_per_person * people

    return total_price


while True:
    name = input("กรุณาใส่ชื่อของคุณ: ")
    if name.lower() == "exit":
        break
    
    age = int(input("กรุณาใส่อายุของคุณ: "))
    movie = input("กรุณาเลือกหนังที่ต้องการดู (Frozen/Marvel): ")
    if movie.lower() == "exit":
        break
    
    day = input("กรุณาใส่วันที่ต้องการดู (e.g. Monday, Friday, holiday): ")
    if day.lower() == "exit":
        break
    
    people = int(input("กรุณาใส่จำนวนคนที่ต้องการซื้อตั๋ว: "))
    if people == 0:
        print("จำนวนคนไม่สามารถเป็น 0 ได้")
        continue

    total_price = calculate_price(age, movie.capitalize(), day.capitalize(), people)
    print(f"ราคาตั๋วรวมสำหรับ {people} คน: {total_price} บาท\n")

print("ขอบคุณที่ใช้บริการ!")








