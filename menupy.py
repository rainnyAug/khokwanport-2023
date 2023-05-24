print("##############################################")
print("#                                            #")
print("#              โปรแกรมภาษาไพธอน               #")
print("#   1. คำนวณอายุด้วยการป้อนปีเกิดเป็น คศ.           #")
print("#   2. แสดงเลขคู่แนวนอนตั้งแต่ 1 - 100 และผล บวก   #")
print("#      ของเลขคู่ในบรรทัดถัดมา                     #")
print("#   3. คำนวณหาพื้นที่ของ...                     #")
print("#   4. คำนวณค่าเฉลี่ย                           #")
print("#   5. แสดงแม่สูตรคูณ                           #")
print("#   6. ค้นหารายชื่อ Mook-peaw                   #")
print("#                                            #")
print("##############################################")

x = int(input("เลือกโปรแกรมที่ต้องการ :"))

#โปรแกรมที่1
if (x==1):
  now = 2020
  birth = int(input("กรุณาป้อนปีเกิดของคุณ :"))
  age = now - birth
  print("คุณอายุ %d ปี"%(age))

#โปรแกรมที่2
elif (x==2):
  r=2
  t=2
  while r <= 98:
    print(r, end = " ")
    r=r+2
    t=r+t
  if r==100:
   print(100, end = " ")
  if r>=100 :
    t=t
    print (t)

#โปรแกรมที่3
elif (x==3):
  print("1 : สี่เหลี่ยม")
  print("2 : สามเหลี่ยม")
  print("3 : วงกลม")
  print("4 : สี่เหลี่ยมด้านขนาน")
  print("5 : สี่เหลี่ยมคางหมู")
  shape = int(input("เลือกทรงเรขาคณิตที่ต้องการ"))
  #สี่เหลี่ยม
  if (shape==1):
    l = int(input("ความยาว : "))
    w = int(input("ความกว้าง : "))
    area = l*w
    print("พื้นที่ของสี่เหลี่ยม = %.2f"%(area))
  #สามเหลี่ยม
  elif (shape==2):
    b = int(input("ฐาน : "))
    h = int(input("สูง : "))
    area = (b*h)/2
    print("พื้นที่ของสี่เหลี่ยม = %.2f"%(area))
  #วงกลม
  elif (shape==3):
    r = int(input("รัศมี : "))
    area = (r*r)*3.14
    print("พื้นที่ของวงกลม = %.2f"%(area))
  #ด้านขนาน
  elif (shape==4):
    b = int(input("ฐาน : "))
    h = int(input("สูง : "))
    area = b*h
    print("พื้นที่ของสี่เหลี่ยมด้านขนาน = %.2f"%(area))
  #คางหมู
  elif (shape==5):
    s1 = int(input("ด้านคู่ขนานด้านที่ 1 : "))
    s2 = int(input("ด้านคู่ขนานด้านที่ 2 : "))
    h = int(input("สูง : "))
    area = (s1*s2*h)/2
    print("พื้นที่ของสี่เหลี่ยมคางหมู = %.2f"%(area))
  #error
  else :
    print("ตัวเลือกที่คุณเลือกไม่มีในรายการ กรุณาเลือกใหม่อีกครั้ง")

#โปรแกรมที่4
elif (x==4):
  count = int(input("มีตัวเลขทั้งหมด : "))
  sum = 0
  counts = 0
  if (count>1):
    while count > 0 :
      count = count - 1
      counts = counts + 1
      num = int(input("ใส่ตัวเลข : "))
      sum += num
      num = int(num)
    avg = sum/counts
    print("ค่าเฉลี่ย = %.2f"%(avg))
  else :
    print("ไม่สามารถคำนวณได้ กรุณาเลือกใหม่อีกครั้ง")

#โปรแกรมที่5
elif (x==5):
  num = int(input("ต้องการสูตรคูณแม่ : "))
  print("  สูตรคูณแม่ %d"%(num))
  row = 1
  while row <=12:
    col = 1
    while col <= 1:
     print("%3dx%2d=%3d"%(num, row, num*row), end="")
     col += 1
    print("")
    row += 1
  print("")

#โปรแกรมที่6
elif (x==6):
  name = ["ขอขวัญ", "ขอขวัญ เตชะองอาจ", "Khokwan", "Khokwan Tachaongart", "Ohm", "โอม", "พัฒนพร", "พัฒนพร จงเลิศวราวงศ์", "Pattanaporn", "Pattanaporn Chonglertvarawong", "Fame", "เฟม", "อัครวิชญ์", "อัครวิชญ์ ไร่คลองครุ", "Akaravit Raiklongkru", "Turbo", "เทอร์โบ", "Akaravit", "พรรษกร", "พรรษกร เสริมศรี", "Pasagorn", "Pasagorn Sermsri", "Guy", "กาย"]
  
  search = str(input("กรุณาป้อนรายชื่อที่ต้องการค้นหา : "))
  for n in name:
    if search == n:
        print('%s is found in list'%(search))
        break
    else:
        print('Not found!')
        break

#eror
else :
  print("ตัวเลือกที่คุณเลือกไม่มีในรายการ กรุณาเลือกใหม่อีกครั้ง")