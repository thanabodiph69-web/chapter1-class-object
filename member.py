class member:
  def __init__(self, name, visits, months, monthly_fee):
    self.name =name
    self.visits = visits
    self.months= months
    self.monthly_fee = monthly_fee

#เงื่อนไขตรวจสอบความเสี่ยง
  def is_at_risk(self):
    return self.visits < 4 and self.months > 6

  def total_paid(self):
      return self.monthly_fee * self.months
  
m1 = member("ธนบดี เพชรนาดี", 2 , 10, 1200)
m2 = member("แก้ม", 10, 12, 12000)
m3 = member("มัธ", 3, 5, 3000)

print ("ชื่อมาชิก:  ",m1.name) 
print ("เสี่ยงต่อการเลอกใช้บริการ:  ", m1.is_at_risk()) 
print ("ค่าบริการ:  ", m1.total_paid())
print ("ชื่อมาชิก:  ",m2.name) 
print ("เสี่ยงต่อการเลอกใช้บริการ:  ", m2.is_at_risk()) 
print ("ค่าบริการ:  ", m2.total_paid())
print ("ชื่อมาชิก:  ",m3.name) 
print ("ค่าบริการ:  ", m3.total_paid()) 
print ("เสี่ยงต่อการเลอกใช้บริการ:  ", m3.is_at_risk()) 