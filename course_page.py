import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CourseAppBase(tk.Toplevel):
    def __init__(self, title, logo_image, left_logo_image, teacher_name, student_name, assignment_name):
        super().__init__()
        
        self.title(title)
        self.geometry("800x600")
        
        # Create top canvas for logo and menu button
        self.top_canvas = tk.Canvas(self, bg='black', height=100)
        self.top_canvas.pack(side=tk.TOP, fill=tk.X)
        
        # Right logo
        right_logo_label = tk.Label(self.top_canvas, image=logo_image, bg='black')
        right_logo_label.image = logo_image
        right_logo_label.place(relx=0.9, rely=0.5, anchor='center')
        
        # Left logo
        left_logo_label = tk.Label(self.top_canvas, image=left_logo_image, bg='black')
        left_logo_label.image = left_logo_image
        left_logo_label.place(relx=0.1, rely=0.5, anchor='center')
        
        # Sidebar button
        sidebar_btn = tk.Button(self.top_canvas, text="Menu", bg='white', font=('Arial', 10), command=self.toggle_sidebar)
        sidebar_btn.place(relx=0.9, rely=1.1, anchor='center')  # Adjusted to place below right logo and smaller
        
        # Sidebar frame
        self.sidebar_frame = tk.Frame(self, bg='black', width=200)  # Changed bg to black
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar_frame.pack_propagate(False)
        
        sidebar_buttons = ["Profile", "Grades", "Logout", "Support"]
        for btn_text in sidebar_buttons:
            btn = tk.Button(self.sidebar_frame, text=btn_text, bg='black', fg='white', font=('Arial', 12), command=lambda t=btn_text: self.show_content(t))  # Changed bg to black and fg to white
            btn.pack(fill=tk.X, pady=2, padx=10)  # Adjusted padding for vertical spacing
        
        self.sidebar_visible = True
        
        # Main content frame
        self.content_frame = tk.Frame(self, bg='white')
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Display teacher's name at the top
        self.teacher_label = tk.Label(self.content_frame, text=f"Teacher            :               {teacher_name}", font=('Arial', 14, 'bold'), bg='white')
        self.teacher_label.pack(pady=10, anchor='n')
        
        # Display assignment name below teacher's name
        self.assignment_label = tk.Label(self.content_frame, text=f"Assignment                   :                    {assignment_name}", font=('Arial', 12), bg='white')
        self.assignment_label.pack(pady=5, anchor='n')
        
        # Main content below the assignment name
        self.current_content = tk.Label(self.content_frame, bg='white')
        self.current_content.pack(expand=True)
        
        # Display student's name at the bottom
        self.student_label = tk.Label(self.content_frame, text=f"Student            :              {student_name}", font=('Arial', 14), bg='white')
        self.student_label.pack(pady=10, anchor='s')
    
    def toggle_sidebar(self):
        if self.sidebar_visible:
            self.sidebar_frame.pack_forget()
            self.content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        else:
            self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
            self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.sidebar_visible = not self.sidebar_visible
    
    def show_content(self, content):
        self.current_content.pack_forget()
        self.current_content = tk.Label(self.content_frame, text=content, font=('Arial', 16), bg='white')
        self.current_content.pack(expand=True)

class Course1App(CourseAppBase):
    def __init__(self, logo_image, left_logo_image, teacher_name, student_name, assignment_name):
        super().__init__("Course 1 Application", logo_image, left_logo_image, teacher_name, student_name, assignment_name)
        
class Course2App(CourseAppBase):
    def __init__(self, logo_image, left_logo_image, teacher_name, student_name, assignment_name):
        super().__init__("Course 2 Application", logo_image, left_logo_image, teacher_name, student_name, assignment_name)

class Course3App(CourseAppBase):
    def __init__(self, logo_image, left_logo_image, teacher_name, student_name, assignment_name):
        super().__init__("Course 3 Application", logo_image, left_logo_image, teacher_name, student_name, assignment_name)

class Course4App(CourseAppBase):
    def __init__(self, logo_image, left_logo_image, teacher_name, student_name, assignment_name):
        super().__init__("Course 4 Application", logo_image, left_logo_image, teacher_name, student_name, assignment_name)

class Course5App(CourseAppBase):
    def __init__(self, logo_image, left_logo_image, teacher_name, student_name, assignment_name):
        super().__init__("Course 5 Application", logo_image, left_logo_image, teacher_name, student_name, assignment_name)

class Course6App(CourseAppBase):
    def __init__(self, logo_image, left_logo_image, teacher_name, student_name, assignment_name):
        super().__init__("Course 6 Application", logo_image, left_logo_image, teacher_name, student_name, assignment_name)

class CoursesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Courses Application")
        self.geometry("800x600")
        
        # Create top canvas for logo and dashboard options
        self.top_canvas = tk.Canvas(self, bg='black', height=100)
        self.top_canvas.pack(side=tk.TOP, fill=tk.X)
        
        # Right logo
        logo_path = "backgroung3.jpeg"
        logo = Image.open(logo_path)
        logo = logo.resize((100, 100), Image.LANCZOS)
        self.logo_image = ImageTk.PhotoImage(logo)

        # Left logo
        left_logo_path = r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\left.jpeg"
        left_logo = Image.open(left_logo_path)
        left_logo = left_logo.resize((100, 100), Image.LANCZOS)
        self.left_logo_image = ImageTk.PhotoImage(left_logo)
        
        # Place the logos on the canvas
        left_logo_label = tk.Label(self.top_canvas, image=self.left_logo_image, bg='black')
        left_logo_label.image = self.left_logo_image
        left_logo_label.place(relx=0.1, rely=0.5, anchor='center')
        
        right_logo_label = tk.Label(self.top_canvas, image=self.logo_image, bg='black')
        right_logo_label.image = self.logo_image
        right_logo_label.place(relx=0.9, rely=0.5, anchor='center')
        
        # Add the "MY COURSES" label in the middle of the top canvas
        courses_label = tk.Label(self.top_canvas, text="MY COURSES", bg='black', fg='white', font=('Arial', 24, 'bold'))
        courses_label.place(relx=0.5, rely=0.5, anchor='center')
        
        # Sidebar button
        sidebar_btn = tk.Button(self.top_canvas, text="Menu", bg='white', font=('Arial', 10), command=self.toggle_sidebar)
        sidebar_btn.place(relx=0.9, rely=0.95, anchor='center')  # Adjusted to place below right logo and smaller
        
        # Sidebar frame
        self.sidebar_frame = tk.Frame(self, bg='black', width=200)  # Changed bg to black
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar_frame.pack_propagate(False)
        
        sidebar_buttons = ["Profile", "Grades", "Logout", "Support"]
        for btn_text in sidebar_buttons:
            btn = tk.Button(self.sidebar_frame, text=btn_text, bg='black', fg='white', font=('Arial', 12))  # Changed bg to black and fg to white
            btn.pack(fill=tk.X, pady=10, padx=10)  # Adjusted padding for vertical spacing
        
        self.sidebar_visible = True
        
        # Main content frame for courses
        self.courses_frame = tk.Frame(self, bg='white')  # Change bg to white
        self.courses_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Sample courses data
        courses = [
            {"title": "Course 1", "description": "Description for course 1", "teacher": "Teacher A", "assignment": "Assignment 1"},
            {"title": "Course 2", "description": "Description for course 2", "teacher": "Teacher B", "assignment": "Assignment 2"},
            {"title": "Course 3", "description": "Description for course 3", "teacher": "Teacher C", "assignment": "Assignment 3"},
            {"title": "Course 4", "description": "Description for course 4", "teacher": "Teacher D", "assignment": "Assignment 4"},
            {"title": "Course 5", "description": "Description for course 5", "teacher": "Teacher E", "assignment": "Assignment 5"},
            {"title": "Course 6", "description": "Description for course 6", "teacher": "Teacher F", "assignment": "Assignment 6"}
        ]
        
        self.student_name = "Student Name"  # Sample student name
        
        # Create course cards
        self.create_course_cards(self.courses_frame, courses)
        
        # Bind the window resize event to the on_resize method
        self.bind("<Configure>", self.on_resize)
    
    def toggle_sidebar(self):
        if self.sidebar_visible:
            self.sidebar_frame.pack_forget()
            self.courses_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        else:
            self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
            self.courses_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.sidebar_visible = not self.sidebar_visible
    
    def create_course_cards(self, parent, courses):
        self.course_cards = []
        
        for i, course in enumerate(courses):
            card = tk.Frame(parent, bg='goldenrod2', bd=2, relief=tk.RAISED)
            card.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="nsew")
            
            title_label = tk.Label(card, text=course["title"], bg='goldenrod2', font=('Arial', 14, 'bold'))
            title_label.pack(pady=5)
            
            desc_label = tk.Label(card, text=course["description"], bg='goldenrod2', font=('Arial', 10))
            desc_label.pack(pady=5)
            
           # assignment_label = tk.Label(card, text=f"Assignment: {course['assignment']}", bg='goldenrod2', font=('Arial', 10))
            #assignment_label.pack(pady=5)
            
            open_btn = tk.Button(card, text="Get Started", font=('Arial', 12), bg='blue', fg='white', padx=10, pady=5, command=lambda c=course: self.open_course(c))
            open_btn.pack(pady=5)
            
            self.course_cards.append(card)
        
        for i in range(len(courses)//2 + len(courses)%2):
            self.courses_frame.grid_rowconfigure(i, weight=1)
        for i in range(2):  # Assume a max of 2 columns for simplicity
            self.courses_frame.grid_columnconfigure(i, weight=1)
    
    def on_resize(self, event):
        width = self.courses_frame.winfo_width()
        if width < 400:
            columns = 1
        elif width < 800:
            columns = 2
        else:
            columns = 3
        
        for index, card in enumerate(self.course_cards):
            card.grid_forget()
            card.grid(row=index//columns, column=index%columns, padx=10, pady=10, sticky="nsew")
        
        for i in range(len(self.course_cards)//columns + len(self.course_cards)%columns):
            self.courses_frame.grid_rowconfigure(i, weight=1)
        for i in range(columns):
            self.courses_frame.grid_columnconfigure(i, weight=1)
    
    def open_course(self, course):
        print(f"Opening {course['title']}: {course['description']}")
        
        if course["title"] == "Course 1":
            self.open_course1_window(course)
        elif course["title"] == "Course 2":
            self.open_course2_window(course)
        elif course["title"] == "Course 3":
            self.open_course3_window(course)
        elif course["title"] == "Course 4":
            self.open_course4_window(course)
        elif course["title"] == "Course 5":
            self.open_course5_window(course)
        elif course["title"] == "Course 6":
            self.open_course6_window(course)

    def open_course1_window(self, course):
        Course1App(self.logo_image, self.left_logo_image, course["teacher"], self.student_name, course["assignment"])

    def open_course2_window(self, course):
        Course2App(self.logo_image, self.left_logo_image, course["teacher"], self.student_name, course["assignment"])

    def open_course3_window(self, course):
        Course3App(self.logo_image, self.left_logo_image, course["teacher"], self.student_name, course["assignment"])

    def open_course4_window(self, course):
        Course4App(self.logo_image, self.left_logo_image, course["teacher"], self.student_name, course["assignment"])

    def open_course5_window(self, course):
        Course5App(self.logo_image, self.left_logo_image, course["teacher"], self.student_name, course["assignment"])

    def open_course6_window(self, course):
        Course6App(self.logo_image, self.left_logo_image, course["teacher"], self.student_name, course["assignment"])

if __name__ == "__main__":
    app = CoursesApp()
    app.mainloop()

'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CoursesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Courses Application")
        self.geometry("800x600")
        
        # Create top canvas for logo and dashboard options
        self.top_canvas = tk.Canvas(self, bg='black', height=100)
        self.top_canvas.pack(side=tk.TOP, fill=tk.X)
        
        # Right logo
        logo_path = r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\right.jpeg"
        logo = Image.open(logo_path)
        logo = logo.resize((100, 100), Image.LANCZOS)
        self.logo_image = ImageTk.PhotoImage(logo)

        # Left logo
        left_logo_path = r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\left.jpeg"
        left_logo = Image.open(left_logo_path)
        left_logo = left_logo.resize((100, 100), Image.LANCZOS)
        self.left_logo_image = ImageTk.PhotoImage(left_logo)
        
        # Place the logos on the canvas
        left_logo_label = tk.Label(self.top_canvas, image=self.left_logo_image, bg='black')
        left_logo_label.image = self.left_logo_image
        left_logo_label.place(relx=0.1, rely=0.5, anchor='center')
        
        right_logo_label = tk.Label(self.top_canvas, image=self.logo_image, bg='black')
        right_logo_label.image = self.logo_image
        right_logo_label.place(relx=0.9, rely=0.5, anchor='center')
        
        # Add the "MY COURSES" label in the middle of the top canvas
        courses_label = tk.Label(self.top_canvas, text="MY COURSES", bg='black', fg='white', font=('Arial', 24, 'bold'))
        courses_label.place(relx=0.5, rely=0.5, anchor='center')
        
        # Sidebar button
        sidebar_btn = tk.Button(self.top_canvas, text="Menu", bg='white', font=('Arial', 10), command=self.toggle_sidebar)
        sidebar_btn.place(relx=0.9, rely=0.95, anchor='center')  # Adjusted to place below right logo and smaller
        
        # Sidebar frame
        self.sidebar_frame = tk.Frame(self, bg='black', width=200)  # Changed bg to black
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar_frame.pack_propagate(False)
        
        sidebar_buttons = ["Profile", "Grades", "Logout", "Support"]
        for btn_text in sidebar_buttons:
            btn = tk.Button(self.sidebar_frame, text=btn_text, bg='black', fg='white', font=('Arial', 12))  # Changed bg to black and fg to white
            btn.pack(fill=tk.X, pady=10, padx=10)  # Adjusted padding for vertical spacing
        
        self.sidebar_visible = True
        
        # Main content frame for courses
        self.courses_frame = tk.Frame(self, bg='white')  # Change bg to white
        self.courses_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Sample courses data
        courses = [
            {"title": "Course 1", "description": "Description for course 1", "teacher": "Teacher A", "assignment": "Assignment 1", "timetable_image": "https://example.com/timetable.png"},
            {"title": "Course 2", "description": "Description for course 2", "teacher": "Teacher B", "assignment": "Assignment 2", "timetable_image": "https://example.com/timetable.png"},
            {"title": "Course 3", "description": "Description for course 3", "teacher": "Teacher C", "assignment": "Assignment 3", "timetable_image": "https://example.com/timetable.png"},
            {"title": "Course 4", "description": "Description for course 4", "teacher": "Teacher D", "assignment": "Assignment 4", "timetable_image": "https://example.com/timetable.png"},
            {"title": "Course 5", "description": "Description for course 5", "teacher": "Teacher E", "assignment": "Assignment 5", "timetable_image": "https://example.com/timetable.png"},
            {"title": "Course 6", "description": "Description for course 6", "teacher": "Teacher F", "assignment": "Assignment 6", "timetable_image": "https://example.com/timetable.png"}
        ]
        
        self.student_name = "Student Name"  # Sample student name
        
        # Create course cards
        self.create_course_cards(self.courses_frame, courses)
        
        # Bind the window resize event to the on_resize method
        self.bind("<Configure>", self.on_resize)
    
    def toggle_sidebar(self):
        if self.sidebar_visible:
            self.sidebar_frame.pack_forget()
            self.courses_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        else:
            self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
            self.courses_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        self.sidebar_visible = not self.sidebar_visible
    
    def create_course_cards(self, parent, courses):
        self.course_cards = []
        
        for i, course in enumerate(courses):
            card = tk.Frame(parent, bg='goldenrod2', bd=2, relief=tk.RAISED)
            card.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="nsew")
            
            # Left side image for time table
            timetable_url = course.get(r"C:\Users\Kumari\OneDrive\Desktop\coding\bootcamp\qwerty.png", "")
            if timetable_url:
                timetable_image = Image.open(timetable_url)
                timetable_image = timetable_image.resize((100, 100), Image.LANCZOS)
                timetable_image = ImageTk.PhotoImage(timetable_image)
                timetable_label = tk.Label(card, image=timetable_image, bg='goldenrod2')
                timetable_label.image = timetable_image
                timetable_label.pack(side=tk.LEFT, padx=10)
            
            # Right side content
            content_frame = tk.Frame(card, bg='goldenrod2')
            content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
            
            title_label = tk.Label(content_frame, text=course["title"], bg='goldenrod2', font=('Arial', 14, 'bold'))
            title_label.pack(pady=5)
            
            desc_label = tk.Label(content_frame, text=course["description"], bg='goldenrod2', font=('Arial', 10))
            desc_label.pack(pady=5)
            
            assignment_label = tk.Label(content_frame, text=f"Assignment: {course['assignment']}", bg='goldenrod2', font=('Arial', 10))
            assignment_label.pack(pady=5)
            
            timetable_label = tk.Label(content_frame, text="Time Table", bg='goldenrod2', font=('Arial', 10))
            timetable_label.pack(pady=5)
            
            open_btn = tk.Button(content_frame, text="Get Started", font=('Arial', 12), bg='blue', fg='white', padx=10, pady=5, command=lambda c=course: self.open_course(c))
            open_btn.pack(pady=5)
            
            self.course_cards.append(card)
        
        for i in range(len(courses)//2 + len(courses)%2):
            parent.grid_rowconfigure(i, weight=1)
        for i in range(2):  # Assume a max of 2 columns for simplicity
            parent.grid_columnconfigure(i, weight=1)
    
    def on_resize(self, event):
        width = self.courses_frame.winfo_width()
        if width < 400:
            columns = 1
        elif width < 800:
            columns = 2
        else:
            columns = 3
        
        for index, card in enumerate(self.course_cards):
            card.grid_forget()
            card.grid(row=index//columns, column=index%columns, padx=10, pady=10, sticky="nsew")
        
        for i in range(len(self.course_cards)//columns + len(self.course_cards)%columns):
            self.courses_frame.grid_rowconfigure(i, weight=1)
        for i in range(columns):
            self.courses_frame.grid_columnconfigure(i, weight=1)
    
    def open_course(self, course):
        print(f"Opening {course['title']}: {course['description']}")
        
        if course["title"] == "Course 1":
            self.open_course1_window(course)
        elif course["title"] == "Course 2":
            self.open_course2_window(course)
        elif course["title"] == "Course 3":
            self.open_course3_window(course)
        elif course["title"] == "Course 4":
            self.open_course4_window(course)
        elif course["title"] == "Course 5":
            self.open_course5_window(course)
        elif course["title"] == "Course 6":
            self.open_course6_window(course)

    def open_course1_window(self, course):
        Course1App(self.logo_image, self.left_logo_image, course["teacher"], self.student_name, course["assignment"])

    def open_course2_window(self, course):
        Course2App(self.logo_image, self.left_logo_image, course["teacher"], self.student_name, course["assignment"])

    def open_course3_window(self, course):
        Course3App(self.logo_image, self.left_logo_image, course["teacher"], self.student_name, course["assignment"])

    def open_course4_window(self, course):
        Course4App(self.logo_image, self.left_logo_image, course["teacher"], self.student_name, course["assignment"])

    def open_course5_window(self, course):
        Course5App(self.logo_image, self.left_logo_image, course["teacher"], self.student_name, course["assignment"])

    def open_course6_window(self, course):
        Course6App(self.logo_image, self.left_logo_image, course["teacher"], self.student_name, course["assignment"])

if __name__ == "__main__":
    app = CoursesApp()
    app.mainloop()

'''
