import os
import time
from student import Student, save_breaks, load_breaks
import threading

file_path = 'student_list.txt'

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_commands():
    print()
    print("-----")
    print("Available Commands:")
    print("  start break [StudentName] - Start a break for a student")
    print("  end break [StudentName] - End a break for a student")
    print("Enter command:")
    print()

def print_pause_time():
    for student in students.values():
        current_break = student.get_current_break()
        if current_break:
            print(current_break)

def process_command(command):
    global students  # If students is a global variable

    if len(command) == 1 and command[0] == "show":
        print_pause_time()
    elif len(command) == 3 and command[0] in ["start", "end"] and command[1] == "break":
        student_name = command[2]
        if student_name in students:
            if command[0] == "start":
                students[student_name].start_break()
            else:
                students[student_name].end_break()
        else:
            print(f"Student {student_name} not found.")
    else:
        print("Invalid command.")

    save_breaks(students)

def handle_input():
    while True:
        command = input().split()
        process_command(command)

students = load_breaks()
if not students:
    student_names = []
    with open(file_path, 'r') as file:
        for line in file:
            name = line.strip()
            student_names.append(name)
    students = {name: Student(name) for name in student_names}

input_thread = threading.Thread(target=handle_input)
input_thread.daemon = True
input_thread.start()

while True:
    clear_console()
    show_commands()
    print_pause_time()
    time.sleep(5)