class student:
  def __(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cypa = cypa

def sort_students(student_list):
  #Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,key=lambda student: student.cypa,reverse=True)
  return sorted_students


# Example usage:
students = [
   Student("Hari","A123",7.8),
   Student("Srikanth","A124",8.9),
   Student("Saumya","A125",9.1),
   Student("Mahidhar","A126",9.9),
]

sorted_students = sort_students(students)

#print the Sorted list of students
for student in sorted_students:
  print("Name: {},Roll Number: {}, CYPA: {}".format(student.name,))
  student.roll_number,
  student.cypa))