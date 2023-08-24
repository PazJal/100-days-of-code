student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#1: Create an empty dictionary called student_grades.
student_grades = {}

#2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
  letter_grade = ""
  number_grade = student_scores[key]
  if(number_grade >= 91 and number_grade <= 100):
    letter_grade = "Outstanding"
  elif(number_grade >= 81 and number_grade <= 90):
    letter_grade = "Exceeds Expectations"
  elif(number_grade >= 71 and number_grade <= 80):
    letter_grade = "Acceptable"
  elif(number_grade <= 70):
    letter_grade = "Fail"
  student_grades[key] = letter_grade 
  

# 🚨 Don't change the code below 👇
print(student_grades)