students = {}
def add_student():
    name = input("enter name: ")
    marks = []
    subjects = int(input("enter number of subjects: "))
    for i in range(subjects):
        marks_input = input(f"enter marks for student {name} and subject {i+1} or 'done': ")
        if marks_input == 'done':
            break
        marks.append(int(marks_input))
    students[name] = {"marks": marks}   

while True:
    add_student()
    cont = input("add another student? (y/n): ")
    if cont.lower() != 'y':
        break
print(students)

def result(name):
    if name in students:
        marks = students[name]["marks"]
        total = sum(marks)
        average = total / len(marks) if marks else 0
        print(f"Total marks for {name}: {total}")
        print(f"Average marks for {name}: {average}")
    else:
        print("Student not found.")
name = input("enter name to check result: ")
result(name)