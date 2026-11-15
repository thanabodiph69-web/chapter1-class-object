class member:
  def __init__(self, name, visits, months):
    self.name =name
    self.visits = visits
    self.months= months

#เงื่อนไขตรวจสอบความเสี่ยง
  def is_at_risk(self):
    return self.visits < 4 and self.months > 6
m1 = member("ธนบดี เพชรนาดี", 2 , 10)
m2 = member("แก้ม", 10, 12)
m3 = member("มัธ", 3, 5)

print ("ชื่อมาชิก:  ",m1.name) 
print ("เสี่ยงต่อการเลอกใช้บริการ:  ", m1.is_at_risk()) 
print ("ชื่อมาชิก:  ",m2.name) 
print ("เสี่ยงต่อการเลอกใช้บริการ:  ", m2.is_at_risk()) 
print ("ชื่อมาชิก:  ",m3.name) 
print ("เสี่ยงต่อการเลอกใช้บริการ:  ", m3.is_at_risk()) 