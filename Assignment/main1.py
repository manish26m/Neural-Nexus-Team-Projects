import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import mysql.connector
from PIL import Image, ImageTk

class Assignment:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("600x600")

        self.frame_login = ttk.Frame(self.root, padding="10")
        self.frame_login.pack(fill=tk.BOTH, expand=True)

        self.title_label = ttk.Label(self.frame_login, text="Login", font=("Helvetica", 24, "bold"), foreground="#333")
        self.title_label.pack(pady=10)

        self.student_id_label = ttk.Label(self.frame_login, text="Student ID:", font=("Helvetica", 14), foreground="#333")
        self.student_id_label.pack(pady=10)

        self.entry_student_id = ttk.Entry(self.frame_login, width=20, font=("Helvetica", 14))
        self.entry_student_id.pack(pady=10)

        self.login_button = ttk.Button(self.frame_login, text="Login", command=lambda: self.login(self.entry_student_id), padding="10")
        self.login_button.pack(pady=10)

    def upload_file(self, label):
        # Open file dialog to select a file
        file_path = filedialog.askopenfilename()
        if file_path:
            # Display the selected file path
            label.config(text=f"Selected file: {file_path}")
            messagebox.showinfo("Upload File", "File uploaded successfully")

    def get_assignments(self, student_id):
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

    def show_assignments(self, student_id):
        assignments = self.get_assignments(student_id)

        for widget in self.frame_assignments.winfo_children():
            widget.destroy()

        if assignments:
            for assignment in assignments:
                assignment_frame = ttk.Frame(self.frame_assignments, padding="10")
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

                upload_button = ttk.Button(assignment_frame, text="Upload File", command=lambda l=file_label: self.upload_file(l), padding="10")
                upload_button.pack(side=tk.RIGHT, padx=10)

        else:
            message = ttk.Label(self.frame_assignments, text="No assignments found for this student", font=("Helvetica", 14), foreground="#666")
            message.pack(anchor="w")

    def login(self, entry_student_id):
        student_id = entry_student_id.get()

        if not student_id.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid student ID")
            return

        # Clear the main window's content
        for widget in self.root.winfo_children():
            widget.destroy()

        # Show the assignments window content
        self.show_assignments_window(student_id)

    def show_assignments_window(self, student_id):
        self.frame_header = ttk.Frame(self.root, padding="10")
        self.frame_header.pack(fill=tk.X)

        self.title_label = ttk.Label(self.frame_header, text="Student Assignments", font=("Helvetica", 24, "bold"), foreground="#333")
        self.title_label.pack(pady=10)

        self.frame_navbar = ttk.Frame(self.root, padding="10")
        self.frame_navbar.pack(fill=tk.X)

        self.dashboard_button = ttk.Button(self.frame_navbar, text="Dashboard", padding="10")
        self.dashboard_button.pack(side=tk.LEFT, padx=10)

        self.assignments_button = ttk.Button(self.frame_navbar, text="Assignments", padding="10")
        self.assignments_button.pack(side=tk.LEFT, padx=10)

        self.grades_button = ttk.Button(self.frame_navbar, text="Grades", padding="10")
        self.grades_button.pack(side=tk.LEFT, padx=10)

        self.frame_profile = ttk.Frame(self.root, padding="10")
        self.frame_profile.pack(fill=tk.X)

        self.profile_title_label = ttk.Label(self.frame_profile, text="Student Profile", font=("Helvetica", 18, "bold"), foreground="#333")
        self.profile_title_label.pack(pady=10)

        self.profile_frame = ttk.Frame(self.frame_profile, padding="10")
        self.profile_frame.pack(fill=tk.X, padx=20)

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

        self.name_label = ttk.Label(self.profile_frame, text="Name:", font=("Helvetica", 14), foreground="#333")
        self.name_label.grid(row=0, column=0, padx=10)

        self.name_value_label = ttk.Label(self.profile_frame, text=student_data[0], font=("Helvetica", 14), foreground="#666")
        self.name_value_label.grid(row=0, column=1, padx=10)

        self.email_label = ttk.Label(self.profile_frame, text="Email:", font=("Helvetica", 14), foreground="#333")
        self.email_label.grid(row=1, column=0, padx=10)

        self.email_value_label = ttk.Label(self.profile_frame, text=student_data[1], font=("Helvetica", 14), foreground="#666")
        self.email_value_label.grid(row=1, column=1, padx=10)

        self.frame_assignments = ttk.Frame(self.root, padding="10")
        self.frame_assignments.pack(fill=tk.BOTH, expand=True)

        self.show_assignments(student_id)

        # Update the main window
        self.root.title("Student Assignments")
        self.root.geometry("1200x800")
root = tk.Tk()
def start():
    
    assignment = Assignment(root)
    root.mainloop()
