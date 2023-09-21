class student:
  
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  
  sorted_students = sorted(student_list,key=lambda student: student.cgpa,reverse=True)
    
  return sorted_students
 

students = [student("Priyanka ", "A04"  ,8.0),student("Keerthana", "A03" ,8.9),student( "Sufiya   ", "A02" ,9.6),student("Sandhiya ", "A01" ,9.9),]

sorted_students = sort_students(students)



for student in sorted_students:
  print("Name : {} ,RollNumber : {},CGPA : {}".format(student.name,student.roll_number,student.cgpa))