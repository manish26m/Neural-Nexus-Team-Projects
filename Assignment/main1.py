import mysql.connector
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import Scrollbar
from PIL import Image, ImageTk
from file_upload import *

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
            assignment_frame = ttk.Frame(frame_assignments, padding="10")
            assignment_frame.pack(fill=tk.X, pady=10)

            assignment_label = ttk.Label(assignment_frame, text=f"{assignment[0]}", font=("Helvetica", 18, "bold"), foreground="#333")
            assignment_label.pack(side=tk.LEFT, padx=20)

            details_frame = ttk.Frame(assignment_frame, padding="10")
            details_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=20)

            description_label = ttk.Label(details_frame, text=f"Description: {assignment[1]}", font=("Helvetica", 14), foreground="#666")
            description_label.pack(anchor="w")

            deadline_label = ttk.Label(details_frame, text=f"Deadline: {assignment[2]}", font=("Helvetica", 14), foreground="#666")
            deadline_label.pack(anchor="w")

            file_label = ttk.Label(assignment_frame, text="", padding="10")
            file_label.pack(side=tk.LEFT, padx=10)

            upload_button = ttk.Button(assignment_frame, text="Upload File", command=lambda l=file_label: upload_file(), padding="10")
            upload_button.pack(side=tk.RIGHT, padx=10)

    else:
        message = ttk.Label(frame_assignments, text="No assignments found for this student", font=("Helvetica", 14), foreground="#666")
        message.pack(anchor="w")

def login():
    student_id = entry_student_id.get()

    if not student_id.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid student ID")
        return

    # Clear the main window's content
    for widget in login_window.winfo_children():
        widget.destroy()

    # Show the assignments window content
    show_assignments_window(student_id)

def show_assignments_window(student_id):
    global frame_assignments

    # Create the assignments window content
    frame_header = ttk.Frame(login_window, padding="10")
    frame_header.pack(fill=tk.X)

    title_label = ttk.Label(frame_header, text="Student Assignments", font=("Helvetica", 24, "bold"), foreground="#333")
    title_label.pack(pady=10)

    frame_navbar = ttk.Frame(login_window, padding="10")
    frame_navbar.pack(fill=tk.X)

    dashboard_button = ttk.Button(frame_navbar, text="Dashboard", padding="10")
    dashboard_button.pack(side=tk.LEFT, padx=10)

    assignments_button = ttk.Button(frame_navbar, text="Assignments", padding="10")
    assignments_button.pack(side=tk.LEFT, padx=10)

    grades_button = ttk.Button(frame_navbar, text="Grades", padding="10")
    grades_button.pack(side=tk.LEFT, padx=10)

    frame_profile = ttk.Frame(login_window, padding="10")
    frame_profile.pack(fill=tk.X)

    profile_title_label = ttk.Label(frame_profile, text="Student Profile", font=("Helvetica", 18, "bold"), foreground="#333")
    profile_title_label.pack(pady=10)

    profile_frame = ttk.Frame(frame_profile, padding="10")
    profile_frame.pack(fill=tk.X, padx=20)

    # Fetch student data from database
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='neuralnexus',
        password='neuralnexus@01',
        database='futurense'
    )
    cursor = conn.cursor()

    query = "SELECT sname, email FROM student WHERE sid = %s"
    cursor.execute(query, (student_id,))
    student_data = cursor.fetchone()

    conn.close()

    name_label = ttk.Label(profile_frame, text="Name:", font=("Helvetica", 14), foreground="#333")
    name_label.grid(row=0, column=0, padx=10)

    name_value_label = ttk.Label(profile_frame, text=student_data[0], font=("Helvetica", 14), foreground="#666")
    name_value_label.grid(row=0, column=1, padx=10)

    email_label = ttk.Label(profile_frame, text="Email:", font=("Helvetica", 14), foreground="#333")
    email_label.grid(row=1, column=0, padx=10)

    email_value_label = ttk.Label(profile_frame, text=student_data[1], font=("Helvetica", 14), foreground="#666")
    email_value_label.grid(row=1, column=1, padx=10)

    frame_assignments = ttk.Frame(login_window, padding="10")
    frame_assignments.pack(fill=tk.BOTH, expand=True)

    show_assignments(student_id)

    # Update the main window
    login_window.title("Student Assignments")
    login_window.geometry("1200x800")

login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("600x600")

frame_login = ttk.Frame(login_window, padding="10")
frame_login.pack(fill=tk.BOTH, expand=True)

title_label = ttk.Label(frame_login, text="Login", font=("Helvetica", 24, "bold"), foreground="#333")
title_label.pack(pady=10)

student_id_label = ttk.Label(frame_login, text="Student ID:", font=("Helvetica", 14), foreground="#333")
student_id_label.pack(pady=10)

entry_student_id = ttk.Entry(frame_login, width=20, font=("Helvetica", 14))
entry_student_id.pack(pady=10)

login_button = ttk.Button(frame_login, text="Login", command=login, padding="10")
login_button.pack(pady=10)

login_window.mainloop()