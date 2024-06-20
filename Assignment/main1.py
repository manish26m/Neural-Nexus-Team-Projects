import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import mysql.connector
from PIL import Image, ImageTk

class Assignment:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("600x600")
        self.root.configure(bg="#f0f0f0")

        self.frame_login = ttk.Frame(self.root, padding="10")
        self.frame_login.pack(fill=tk.BOTH, expand=True)
        self.frame_login.configure(style="Login.TFrame")

        self.title_label = ttk.Label(self.frame_login, text="Login", font=("Helvetica", 24, "bold"), style="DarkText.TLabel")
        self.title_label.pack(pady=10)

        self.student_id_label = ttk.Label(self.frame_login, text="Student ID:", font=("Helvetica", 14), style="DarkText.TLabel")
        self.student_id_label.pack(pady=10)

        self.entry_student_id = ttk.Entry(self.frame_login, width=20, font=("Helvetica", 14))
        self.entry_student_id.pack(pady=10)

        self.login_button = ttk.Button(self.frame_login, text="Login", command=lambda: self.login(self.entry_student_id), style="Accent.TButton")
        self.login_button.pack(pady=10)

    def upload_file(self, label):
        file_path = filedialog.askopenfilename()
        if file_path:
            label.config(text=f"Selected file: {file_path}")
            messagebox.showinfo("Upload File", "File uploaded successfully")

    def get_assignments(self, student_id):
        try:
            conn = mysql.connector.connect(
                host='127.0.0.1',
                user='neuralnexus',
                password='neuralnexus@01',
                database='futurense'
            )
            cursor = conn.cursor()

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
                assignment_frame.configure(style="Card.TFrame")

                assignment_label = ttk.Label(assignment_frame, text=f"{assignment[0]}", font=("Helvetica", 18, "bold"), style="2DarkText.TLabel")
                assignment_label.pack(side=tk.LEFT, padx=20)

                details_frame = ttk.Frame(assignment_frame, padding="10")
                details_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=20)

                description_label = ttk.Label(details_frame, text=f"Description: {assignment[1]}", font=("Helvetica", 14), style="1LightText.TLabel")
                description_label.pack(anchor="w")

                deadline_label = ttk.Label(details_frame, text=f"Deadline: {assignment[2]}", font=("Helvetica", 14), style="1LightText.TLabel")
                deadline_label.pack(anchor="w")

                file_label = ttk.Label(assignment_frame, text="", padding="10")
                file_label.pack(side=tk.LEFT, padx=10)

                upload_button = ttk.Button(assignment_frame, text="Upload File", command=lambda l=file_label: self.upload_file(l), style="Accent.TButton")
                upload_button.pack(side=tk.RIGHT, padx=10)

        else:
            message = ttk.Label(self.frame_assignments, text="No assignments found for this student", font=("Helvetica", 14), style="LightText.TLabel")
            message.pack(anchor="w")

    def login(self, entry_student_id):
        student_id = entry_student_id.get()

        if not student_id.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid student ID")
            return

        for widget in self.root.winfo_children():
            widget.destroy()

        self.show_assignments_window(student_id)

    def show_assignments_window(self, student_id):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.frame_header = ttk.Frame(self.root, padding="10")
        self.frame_header.pack(fill=tk.X)
        self.frame_header.configure(style="Header.TFrame")

        self.title_label = ttk.Label(self.frame_header, text="Student Assignments", font=("Helvetica", 24, "bold"), style="1DarkText.TLabel")
        self.title_label.pack(pady=10)

        self.frame_navbar = ttk.Frame(self.root, padding="10", style="Navbar.TFrame")
        self.frame_navbar.pack(side=tk.LEFT, fill=tk.Y, expand=False, anchor="nw")

        self.dashboard_button = ttk.Button(self.frame_navbar, text="Dashboard", style="Navbar.TButton")
        self.dashboard_button.pack(pady=10, fill=tk.X)

        self.assignments_button = ttk.Button(self.frame_navbar, text="Assignments", style="Navbar.TButton")
        self.assignments_button.pack(pady=10, fill=tk.X)

        self.grades_button = ttk.Button(self.frame_navbar, text="Grades", style="Navbar.TButton")
        self.grades_button.pack(pady=10, fill=tk.X)

        self.frame_profile = ttk.Frame(self.root, padding="10")
        self.frame_profile.pack(fill=tk.X)
        self.frame_profile.configure(style="Profile.TFrame")

        self.profile_title_label = ttk.Label(self.frame_profile, text="Student Profile", font=("Helvetica", 18, "bold"), style="DarkText.TLabel")
        self.profile_title_label.pack(pady=10)

        self.profile_frame = ttk.Frame(self.frame_profile, padding="10")
        self.profile_frame.pack(fill=tk.X, padx=20)
        self.profile_frame.configure(style="Profile.TFrame")

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

        self.name_label = ttk.Label(self.profile_frame, text="Name:", font=("Helvetica", 14), style="DarkText.TLabel")
        self.name_label.grid(row=0, column=0, padx=10)

        self.name_value_label = ttk.Label(self.profile_frame, text=student_data[0], font=("Helvetica", 14), style="LightText.TLabel")
        self.name_value_label.grid(row=0, column=1, padx=10)

        self.email_label = ttk.Label(self.profile_frame, text="Email:", font=("Helvetica", 14), style="DarkText.TLabel")
        self.email_label.grid(row=1, column=0, padx=10)

        self.email_value_label = ttk.Label(self.profile_frame, text=student_data[1], font=("Helvetica", 14), style="LightText.TLabel")
        self.email_value_label.grid(row=1, column=1, padx=10)

        self.frame_assignments = ttk.Frame(self.root, padding="10")
        self.frame_assignments.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.frame_assignments.configure(style="Assignments.TFrame")

        self.show_assignments(student_id)

        self.root.title("Student Assignments")
        self.root.geometry("1200x800")

root = tk.Tk()

def start():
    style = ttk.Style()
    style.configure("Login.TFrame", background="#f0f0f0")
    style.configure("Header.TFrame", background="#292929")
    style.configure("Navbar.TFrame", background="#292929")
    style.configure("Navbar.TButton", background="#fff", foreground="#000", font=("Helvetica", 14), padding=10)
    style.configure("Profile.TFrame", background="#f0f0f0")
    style.configure("Assignments.TFrame", background="#fff")
    style.configure("Card.TFrame", background="#daa520")
    style.configure("Accent.TButton", background="#7A288A", foreground="#000", font=("Helvetica", 14), padding=10)
    style.configure("1DarkText.TLabel", background="#292929", foreground="#fff")
    style.configure("DarkText.TLabel", background="#f0f0f0", foreground="#333")
    style.configure("2DarkText.TLabel", background="#daa520", foreground="#000")
    style.configure("LightText.TLabel", background="#f0f0f0", foreground="#333")
    style.configure("1LightText.TLabel", background="#f0f0f0", foreground="#333")
    assignment = Assignment(root)
    root.mainloop()

start()
