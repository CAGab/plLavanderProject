instructor = {"BES241": "Ruiz", "TRONIC1": "Malino", "OBORPRG": "Dereje", "IT212": "Meimban", "MATSCI": "Matias"}
time = {"BES241": "7:30 am", "TRONIC1": "10:30 am", "OBORPRG": "1:30 pm", "IT212": "4:30 pm", "MATSCI": "6:00 pm"}
room = {"BES241": "204", "TRONIC1": "307", "OBORPRG": "308", "IT212": "212", "MATSCI": "303"}
student_name = {"BES241": ['David', 'Jayce', 'Gabriel']}
attendance = {"BES241": []}

print("Here are the following commands for this program:\n" 
      "\nCourses - View details of a course"
      "\nAttendance - Run an attendance check of a course"
      "\nNew - Add a new course"
      "\nChange - Change the details of a course"
      "\nAdd - Add student/s in a course"
      "\nRemove - Remove student/s in a course"
      "\nDelete - Delete a course"
      "\nQuit - Quit the program")

while True:
    user_input = str(input("Please enter a command: "))
    if user_input == "Courses":
        course_code = str(input("Enter a course code: "))
        if course_code in instructor:
            print("Instructor for this course is Prof.", instructor[course_code])
            print("Time for the course: ", time[course_code])
            print("Room for the course: ", room[course_code])
            print("Students under this course: ", student_name[course_code])
            print("Students' attendance, respectively:", attendance[course_code])
        else:
            print("Invalid course code.")

    elif user_input == "Attendance":
        course_code = str(input('Enter Course Code:'))
        print(student_name[course_code])

        def append_value(dict, key, value):
            if key in dict:
                if not isinstance(dict[key], list):
                    dict[key] = [dict[key]]
                dict[key].append(value)
        if course_code in instructor:
            while True:
                attendance_check = str(input("Type 'Present' or 'Absent': "))  # Respectively to the students shown
                append_value(attendance, course_code, attendance_check)
                question2 = int(input('Continue Attendance Check? Press 1 for Yes or 2 for NO:'))
                if question2 == 1:
                    continue
                elif question2 == 2:
                    print("Attendance Check Complete.")
                    break
        else:
            print("Invalid course code")

    elif user_input == "New":
        new_cc = str(input("Enter a new course code: "))
        new_ins = str(input("What is the instructor's name? "))
        new_time = str(input("What is the time for the class? "))
        new_room = str(input("What is the room number for the class? "))
        new_att = str(input("Type '-' to create an attendance list"))
        instructor[new_cc] = new_ins
        time[new_cc] = new_time
        room[new_cc] = new_room
        attendance[new_cc] = new_att

        def append_value(dict, key, value):
            if key in dict:
                if not isinstance(dict[key], list):
                    dict[key] = [dict[key]]
                dict[key].append(value)
        new_student_name = str(input('Enter Student name: '))
        student_name[new_cc] = new_student_name
        question = int(input('Continue Adding Students? Press 1 for Yes or 2 for NO: '))
        if question == 1:
            while True:
                s_name_new = str(input('Enter Student name: '))
                append_value(student_name, new_cc, s_name_new)
                question2 = int(input('Continue Adding Students? Press 1 for Yes or 2 for NO: '))
                if question2 == 1:
                    continue
                elif question2 == 2:
                    print("Course Successfully Created.")
                    break
        elif question == 2:
            print("Addition of students complete.")
        else:
            print("Invalid Input.")

    elif user_input == "Add":
        course_code = str(input('Enter Course Code:'))

        def append_value(dict, key, value):
            if key in dict:
                if not isinstance(dict[key], list):
                    dict[key] = [dict[key]]
                dict[key].append(value)
        if course_code in instructor:
            while True:
                s_name_add = str(input('Enter Student name: '))
                append_value(student_name, course_code, s_name_add)
                question2 = int(input('Continue Adding Students? Press 1 for Yes or 2 for NO: '))
                if question2 == 1:
                    continue
                elif question2 == 2:
                    print("Students Successfully Added.")
                    break
        else:
            print("Invalid course code")

    elif user_input == "Remove":
        course_code = str(input("Enter a course code: "))

        def remove_value(dict, key, value):
            if key in dict:
                if not isinstance(dict[key], list):
                    dict[key] = [dict[key]]
                dict[key].remove(value)
        if course_code in instructor:
            while True:
                s_name_remove = str(input("Enter Student name: "))
                remove_value(student_name, course_code, s_name_remove)
                r_question1 = str(input("Remove the student from the course? Yes or No? "))
                if r_question1 == "Yes" or "yes":
                    print("Student Successfully Removed")
                    r_question2 = int(input("Continue Removing Students? Press 1 for Yes or 2 for No: "))
                    if r_question2 == 1:
                        continue
                    elif r_question2 == 2:
                        print("Students Successfully Removed")
                        break
                elif r_question1 == "No" or "no":
                    continue
        else:
            print("Invalid course code")

    elif user_input == "Change":
        course_code = str(input("Enter a course code: "))
        new_ins = str(input("What is the new instructor's name? "))
        new_time = str(input("What is the new time for the class? "))
        new_room = str(input("What is the new room number for the class? "))
        if course_code in instructor:
            instructor[course_code] = new_ins
            time[course_code] = new_time
            room[course_code] = new_room
        else:
            print("Invalid course code.")

    elif user_input == "Delete":
        course_delete = str(input("Enter a course code to be delete: "))
        if course_delete in instructor:
            sure_delete = str(input("Are you sure you want to delete this course? "))
            if sure_delete == "Yes" or "yes":
                del(instructor[course_delete])
                print("Course has been deleted.")
            elif sure_delete == "No" or "no":
                continue
        else:
            print("Invalid course code.")

    elif user_input == "Quit":
        sure_quit = str(input("Are you sure you want to quit? "))
        if sure_quit == "Yes" or "yes":
            exit()
        elif sure_quit == "No" or "no":
            continue
    else:
        print("Invalid command.")
