students_list = []  
students_dict = {}

name = input("enter student name")
age = input("enter student age")
grade = input("enter student grade")
students_list.append(name)
students_dict[name] = {'age': age, 'grade': grade}
print("student information added successfully")

if name in students_dict:
    print(f"Name: {name}, Age: {students_dict[name]["age"]}, Grade: {students_dict[name]["grade"]}")
else:
    print("student not found")

if name in students_list:
    students_list.remove(name)
    students_dict[name]
