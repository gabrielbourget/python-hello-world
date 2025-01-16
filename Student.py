class Student:
  def __init__(self, name, major, gpa, is_on_probation):
    self.name = name
    self.major = major
    self.gpa = gpa
    self.is_on_probation = is_on_probation
  
  def on_honor_roll(self):
    if self.gpa >= 3.5:
      return True
    else:
      return False

student= { 
  "name": "Bob",
  "major": "Computer Science",
  "gpa": 3.5,
  "is_on_probation": True}

student2 = [
  "Bob",
  "Computer Science",
  3.5,
  True
]

s = Student(**student1) # destructures object
s2 = Student(*student2) # destructures list
s3 = Student(major="Computer Science", name="Bob", gpa=3.5, is_on_probation=True) # default args along with explicit arg names