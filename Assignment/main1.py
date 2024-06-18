import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import Scrollbar
from file_upload import upload_file

def get_assignments(student_id):
    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='neuralnexus',
            password='neuralnexus@01',
            database='futurense'
        )
        cursor = conn.cursor()

        # Query to fetch assignments for the student
        query = '''
        SELECT Assignment.assignment_name, Assignment.description, Assignment.deadline
        FROM Assignment
        JOIN course ON Assignment.cid = course.cid
        WHERE course.sid = %s
        '''
        cursor.execute(query, (student_id,))
        assignments = cursor.fetchall()

        conn.close()
        return assignments
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return []

def show_assignments(student_id):
    assignments = get_assignments(student_id)
    
    for widget in frame_assignments.winfo_children():
        widget.destroy()

    if assignments:
        for assignment in assignments:
            assignment_frame = Frame(frame_assignments, bg="#f7f7f1", highlightbackground="#ddd", highlightthickness=1)
            assignment_frame.pack(fill=X, pady=10)

            Label(assignment_frame, text=f"{assignment[0]}", font=("Helvetica", 18, "bold"), fg="#333", bg="#f7f7f1").pack(side=LEFT, padx=20)

            details_frame = Frame(assignment_frame, bg="#f7f7f1")
            details_frame.pack(side=LEFT, fill=X, expand=True, padx=20)

            Label(details_frame, text=f"Description: {assignment[1]}", font=("Helvetica", 14), fg="#666", bg="#f7f7f1").pack(anchor="w")
            Label(details_frame, text=f"Deadline: {assignment[2]}", font=("Helvetica", 14), fg="#666", bg="#f7f7f1").pack(anchor="w")

            file_label = Label(assignment_frame, text="", bg="#f7f7f1")
            file_label.pack(side=LEFT, padx=10)

            upload_button = Button(assignment_frame, text="Upload File", command=lambda l=file_label: upload_file(), bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
            upload_button.pack(side=RIGHT, padx=10)

    else:
        Label(frame_assignments, text="No assignments found for this student", fg="#666", bg="#f7f7f1").pack(anchor="w")

def login():
    student_id = entry_student_id.get()
    
    if not student_id.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid student ID")
        return

    login_window.destroy()
    show_assignments_window(student_id)

def show_assignments_window(student_id):
    global frame_assignments
    assignments_window = Tk()
    assignments_window.title("Student Assignments")
    assignments_window.geometry("800x600")

    frame_header = Frame(assignments_window, bg="#333")
    frame_header.pack(fill=X)

    logo_image = PhotoImage(file="logo.png")
    logo_label = Label(frame_header, image=logo_image, bg="#333")
    logo_label.image = logo_image
    logo_label.pack(side=LEFT, padx=10)

    Label(frame_header, text="Student Assignments", font=("Helvetica", 24, "bold"), fg="white", bg="#333").pack(pady=10)

    frame_navbar = Frame(assignments_window, bg="#f7f7f1")
    frame_navbar.pack(fill=X)

    dashboard_image = PhotoImage(file="dashboard.png")
    dashboard_button = Button(frame_navbar, image=dashboard_image, command=lambda: print("Dashboard button clicked"), bg="#f7f7f1", fg="#333")
    dashboard_button.image = dashboard_image
    dashboard_button.pack(side=LEFT, padx=10)

    assignments_image = PhotoImage(file="assignments.png")
    assignments_button = Button(frame_navbar, image=assignments_image, command=lambda: print("Assignments button clicked"), bg="#f7f7f1", fg="#333")
    assignments_button.image = assignments_image
    assignments_button.pack(side=LEFT, padx=10)

    grades_image = PhotoImage(file="grades.png")
    grades_button = Button(frame_navbar, image=grades_image, command=lambda: print("Grades button clicked"), bg="#f7f7f1", fg="#333")
    grades_button.image = grades_image
    grades_button.pack(side=LEFT, padx=10)

    frame_profile = Frame(assignments_window, bg="#f7f7f1")
    frame_profile.pack(fill=X)

    profile_image = PhotoImage(file="profile.png")
    profile_label = Label(frame_profile, image=profile_image, bg="#f7f7f1")
    profile_label.image = profile_image
    profile_label.pack(side=LEFT, padx=10)

    Label(frame_profile, text="Student Profile", font=("Helvetica", 18, "bold"), fg="#333", bg="#f7f7f1").pack(pady=10)

    profile_frame = Frame(frame_profile, bg="#f7f7f1")
    profile_frame.pack(fill=X, padx=20)

    Label(profile_frame, text="Name:", font=("Helvetica", 14), fg="#333", bg="#f7f7f1").grid(row=0, column=0, padx=10)
    Label(profile_frame, text="Ravi Kumar", font=("Helvetica", 14), fg="#666", bg="#f7f7f1").grid(row=0, column=1, padx=10)

    Label(profile_frame, text="Email:", font=("Helvetica", 14), fg="#333", bg="#f7f7f1").grid(row=1, column=0, padx=10)
    Label(profile_frame, text="ravi@example.com", font=("Helvetica", 14),fg="#666", bg="#f7f7f1").grid(row=1, column=1, padx=10)

    Label(profile_frame, text="Phone Number:", font=("Helvetica", 14), fg="#333", bg="#f7f7f1").grid(row=2, column=0, padx=10)
    Label(profile_frame, text="987654321", font=("Helvetica", 14), fg="#666", bg="#f7f7f1").grid(row=2, column=1, padx=10)

    frame_assignments = Frame(assignments_window, bg="#f7f7f1")
    frame_assignments.pack(pady=20, fill=BOTH, expand=True)

    scrollbar = Scrollbar(frame_assignments, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas = Canvas(frame_assignments, yscrollcommand=scrollbar.set, bg="#f7f7f1")
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar.config(command=canvas.yview)

    frame_canvas = Frame(canvas, bg="#f7f7f1")
    canvas.create_window((0,0), window=frame_canvas, anchor=NW)

    show_assignments(student_id)

    assignments_window.mainloop()

login_window = Tk()
login_window.title("Login")
login_window.geometry("300x100")

frame_header = Frame(login_window, bg="#333")
frame_header.pack(fill=X)

logo_image = PhotoImage(file="logo.png")
logo_label = Label(frame_header, image=logo_image, bg="#333")
logo_label.image = logo_image
logo_label.pack(side=LEFT, padx=10)

Label(frame_header, text="Login", font=("Helvetica", 24, "bold"), fg="white", bg="#333").pack(pady=10)

Label(login_window, text="Enter Student ID:").pack()
entry_student_id = Entry(login_window)
entry_student_id.pack()
Button(login_window, text="Login", command=login, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold")).pack()

login_window.mainloop()