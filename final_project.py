import json

def calculate_grade(score):
    if 80 <= score <= 100:
        return "A"
    elif 70 <= score < 80:
        return "B"
    elif 60 <= score < 70:
        return "C"
    elif 50 <= score < 60:
        return "D"
    else:
        return "F"

students = []

# รับข้อมูลนักเรียน 3 คน
for i in range(3):
    print(f"\nกรอกข้อมูลนักเรียนคนที่ {i + 1}")
    student = {}
    student["ชื่อ"] = input("ชื่อ: ")
    student["นามสกุล"] = input("นามสกุล: ")
    student["รหัสนักเรียน"] = input("รหัสนักเรียน: ")

    while True:
        try:
            math = int(input("คะแนนคณิตศาสตร์ (0-100): "))
            science = int(input("คะแนนวิทยาศาสตร์ (0-100): "))
            art = int(input("คะแนนศิลปะ (0-100): "))
            if 0 <= math <= 100 and 0 <= science <= 100 and 0 <= art <= 100:
                break
            else:
                print("กรุณาใส่คะแนนที่อยู่ในช่วง 0 ถึง 100")
        except ValueError:
            print("กรุณากรอกตัวเลขเท่านั้น")

    # เก็บคะแนนและเกรด
    student["math"] = math
    student["grade_math"] = calculate_grade(math)
    student["science"] = science
    student["grade_science"] = calculate_grade(science)
    student["art"] = art
    student["grade_art"] = calculate_grade(art)

    students.append(student)

# เขียนข้อมูลทั้งหมดลง students.json
with open("students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=4)

# แสดงผลจากไฟล์ students.json
print("\n📖 ข้อมูลทั้งหมดจากไฟล์ students.json:")
with open("students.json", "r", encoding="utf-8") as f:
    loaded_students = json.load(f)

for idx, s in enumerate(loaded_students, 1):
    print(f"\nนักเรียนคนที่ {idx}")
    print(f"ชื่อ: {s['ชื่อ']} {s['นามสกุล']}")
    print(f"รหัส: {s['รหัสนักเรียน']}")
    print(f"คณิตศาสตร์: {s['math']} เกรด: {s['grade_math']}")
    print(f"วิทยาศาสตร์: {s['science']} เกรด: {s['grade_science']}")
    print(f"ศิลปะ: {s['art']} เกรด: {s['grade_art']}")
