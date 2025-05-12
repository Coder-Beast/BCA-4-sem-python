student = {"name" : 'alex', 'age' : 22, 'course': 'cs', 'grades': 'a'}

student['email'] = 'asdsad'
print(student)
student['age'] = 21
print(student)
del student['email']
print(student)
if 'grades' in student:
    print("yup")

print("keys: ", student.keys())

print("values:", student.values())
