# Welcome students to the app
print("Hello! Welcome to your Student Grade Tracking App for Computer Programming for CS class.")
print("You can register your students, enter their grades, and view them.")
print("\n")

student_dict = {}

while True:
    # Ask user for input
    action = int(input("Enter:\n1) Register students\n2) Enter grades for an assignment\n3) View student list and their grades\n4) Exit the program\nYour Selection: "))

    if action == 1:
        quantity = int(input("Great! Welcome to the student Registration Portal. How many students are you registering? "))

        for number in range(quantity):
            student_name = input(f"Kindly enter the name of student {number + 1}: ")
            print(f"Student '{student_name}' added.")

            if number + 1 == quantity:
                print("Successfully registered all your students! 🥳")

            student_dict[student_name] = {}

    elif action == 2:
        # Enter grades for an assignment
        assignment_name = input("Enter the name of the assignment: ")
        total_points = float(input("Enter the total points for the assignment: "))

        for student_name in student_dict.keys():
            grade = float(input(f"Enter grade for {student_name} in '{assignment_name}': "))
            student_dict[student_name][assignment_name] = grade

    elif action == 3:
        # View student list and their grades
        print("_" * 26)
        print("STUDENTS AND THEIR GRADES:")
        print("_" * 26)
        for student_name, grades in student_dict.items():
            print(f"Student: {student_name}")
            for assignment, grade in grades.items():
                print(f"  {assignment}: {grade}")
            print("_" * 26)

    elif action == 4:
        # Quit Program
        print("Thank you for using my App. Send MoMo if you love my app! ;) \nNana Amoako™️")
        break
    
    # elif action == 5:
    #     # Debugger (Print dictionary)
    #     print(student_dict)
            