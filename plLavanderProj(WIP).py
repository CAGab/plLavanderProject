instructor = {"BES241": "Ruiz", "TRONIC1": "Malino", "OBORPRG": "Dereje", "IT212": "Meimban", "MATSCI": "Matias"}
time = {"BES241": "7:30 am", "TRONIC1": "10:30 am", "OBORPRG": "1:30 pm", "IT212": "4:30 pm", "MATSCI": "6:00 pm"}
room = {"BES241": "204", "TRONIC1": "307", "OBORPRG": "308", "IT212": "212", "MATSCI": "303"}
student_name = {"BES241": {'David', 'Jayce', 'Gabriel'}}
student_no = {"BES241": {'0-01', '0-02', '0-03'}}

print("Here are the following commands for this program:\n" 
      "\nCourses - to view details of a course" 
      "\nNew - to add a new course"
      "\nChange - to change details of a course"
      "\nAdd - to add student/s to a course"
      "\nDelete - to delete a course"
      "\nQuit - to quit the program")

while True:
    user_input = str(input("Please enter a command: "))
    if user_input == "Courses":
        course_code = str(input("Enter a course code: "))
        if course_code in instructor:
            print("Instructor for this course is Prof.", instructor[course_code])
            print("Time for the course: ", time[course_code])
            print("Room for the course: ", room[course_code])
        else:
            print("Invalid course code.")

    elif user_input == "New":
        new_cc = str(input("Enter a new course code: "))
        new_ins = str(input("What is the instructor's name? "))
        new_time = str(input("What is the time for the class? "))
        new_room = str(input("What is the room number for the class? "))
        instructor[new_cc] = new_ins
        time[new_cc] = new_time
        room[new_cc] = new_room

        def append_value(dict, key, value):
            if key in dict:
                if not isinstance(dict[key], list):
                    dict[key] = [dict[key]]
                dict[key].append(value)
        new_student_name = str(input('Enter Student name: '))
        student_name[new_cc] = new_student_name
        new_student_no = str(input('Enter Student no.: '))
        student_no[new_cc] = new_student_no
        question = int(input('Continue Adding Students? Press 1 for Yes or 2 for NO: '))
        if question == 1:
            while True:
                s_name_new = str(input('Enter Student name: '))
                append_value(student_name, new_cc, s_name_new)
                s_no_new = str(input('Enter Student number: '))
                append_value(student_no, new_cc, s_no_new)
                question2 = int(input('Continue Adding Students? 1 for Yes or 2 for NO: '))
                if question2 == 1:
                    continue
                elif question2 == 2:
                    print("List of Students are now closed.")
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
                s_no_add = str(input('Enter Student number: '))
                append_value(student_no, course_code, s_no_add)
                question2 = int(input('Continue Adding Students? Press 1 for Yes or 2 for NO:'))
                if question2 == 1:
                    continue
                elif question2 == 2:
                    print("Student List Closed.")
                    break
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
