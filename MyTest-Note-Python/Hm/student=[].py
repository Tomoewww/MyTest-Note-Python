student=[]
while True:
    print(" กรุณากรอกชื่อ")
    print(" เมื่อกรอกเสร็จกรุณาพิมพ์ : OK :")
    name=str(input("จุดใส่ชื่อ"))
    
    if name == "OK":
        break
    student.append(name)

print(student)
student.sort()
print(student)
student.reverse()
print(student)