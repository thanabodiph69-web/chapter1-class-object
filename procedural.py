name = "ธนบดี เพชรนาดี"
visit = 2 
months =10

#ฟังก์ชั่นตรวจสอบความเสี่ยง
def is_at_risk(visit,months):
  return visit < 4 and months > 6

#แสดงผลลัพธ์
print("ชื่อสมาชิก:  ", name)
print("จำนวนที่ใช้งาน:  ", visit , " ครั้ง")
print("อายุสมาชิก:  ", months , " เดือน")
print("ความเสี่ยงต่อการเลิกใช้บริการ:  ",is_at_risk(visit,months))