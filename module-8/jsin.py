import json

# Open a JSON file and load its contents into a Python dictionary
with open('student.json') as file:
 data = json.load(file)


def print_class_list(data):
    class_list = data
    for student in class_list:
        print(f"{student['L_Name']}, {student['F_Name']}: ID {student['Student_ID']}, Email = {student['Email']}")

print("This is the original Student List:")

print_class_list(data)
print("")
# New student's details
new_student = {
    "F_Name": "Rashai",
    "L_Name": "Robertson",
    "Student_ID": "54321",
    "Email": "Robertson.R@Bellevue.com"
}

# Append the new student to the class list
data.append(new_student)

def print_class_list(data):
    class_list = data
    for student in class_list:
        print(f"{student['L_Name']}, {student['F_Name']}: ID {student['Student_ID']}, Email = {student['Email']}")

print("This is the updated Student List:")

# Print the updated class list
print_class_list(data)

with open("student.json", "w") as outfile:
 json.dump(data, outfile)


print("The JSON file has been updated!")
