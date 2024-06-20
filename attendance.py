import tkinter as tk
import mysql.connector
from PIL import Image, ImageTk

username = "root"
password = "vaibhav"

my_db = mysql.connector.connect(
    host="localhost",
    user=username,
    passwd=password,
    database="futurense"
)

# variables to store attendance
one = 0
two = 0
three = 0
four = 0
five = 0

# 1st subject
cursor = my_db.cursor()
cursor.execute("select (Count('Present')/count('status')) * 100 from attendance where sid = 1 and cid = 1;")
tables = cursor.fetchall()

for i in tables:
    one = int(i[0])

# 2nd subject
cursor = my_db.cursor()
cursor.execute("select (Count('Present')/count('status')) * 100 from attendance where sid = 1 and cid = 2;")
tables = cursor.fetchall()

for i in tables:
    two = int(i[0])

# 3rd subject
cursor = my_db.cursor()
cursor.execute("select (Count('Present')/count('status')) * 100 from attendance where sid = 1 and cid = 3;")
tables = cursor.fetchall()

for i in tables:
    three = int(i[0])

# 4th subject
cursor = my_db.cursor()
cursor.execute("select (Count('Present')/count('status')) * 100 from attendance where sid = 1 and cid = 4;")
tables = cursor.fetchall()

for i in tables:
    four = int(i[0])

# 5th subject
cursor = my_db.cursor()
cursor.execute("select (Count('Present')/count('status')) * 100 from attendance where sid = 1 and cid = 5;")
tables = cursor.fetchall()

for i in tables:
    five = int(i[0])

# total
total_percent = (one + two + three + four + five)/5

# Student name
student = ""
cursor = my_db.cursor()
cursor.execute("SELECT s.sname FROM student s JOIN attendance a ON a.sid = s.sid WHERE a.sid = 1;")
tables = cursor.fetchall()

student = set()
for i in tables:
    student.add(i)
    
for i in student:
    student = i[0]
    
root = tk.Tk()
root.title("Attendance")
root.geometry("1920x1080")

# Header structure
# Header Frame
header = tk.Frame(root, bg="black", width=1920, height=105)
header.pack()

# Image label
pil_image = Image.open("logo.png")
pil_image = pil_image.resize((100, 100))
lpu_image = Image.open("lpu.png")
lpu_image = lpu_image.resize((200, 100))

tk_image = ImageTk.PhotoImage(pil_image)
lpu_image = ImageTk.PhotoImage(lpu_image)

image_label = tk.Label(header, image=tk_image, bg="black")
image_label.image = tk_image
image_label.place(x=0, y=0)

lpu_label = tk.Label(header, image=lpu_image, bg="black")
lpu_label.image = tk_image
lpu_label.place(x = 1325, y = 0)

# Attendance heading
attendance_label = tk.Label(header, text="Attendance", bg="black", fg="white", font=("Times", 20))
attendance_label.place(x = 800, y = 20)
name_label = tk.Label(header, text=student, bg="black", fg="white", font=("Times", 15))
name_label.place(x = 815, y = 60)

# Sidebar Frane
sidebar = tk.Frame(root, width=100, bg="black")
sidebar.place(x=0, y=105, height=800, width=100)  

# Buttons
button1 = tk.Button(sidebar, text="Home", bg="black", fg="white")
button1.pack(pady=15)

button2 = tk.Button(sidebar, text="Show Courses", bg="black", fg="white")
button2.pack(pady=15)

button3 = tk.Button(sidebar, text="Show Assignment", bg="black", fg="white")
button3.pack(pady=15)

button4 = tk.Button(sidebar, text="Show Grades", bg="black", fg="white")
button4.pack(pady=15)

button5 = tk.Button(sidebar, text="Show Exams", bg="black", fg="white")
button5.pack(pady=15)

# Create subject frame
maths = tk.Frame(root, width=1920, height=100, bg="orange")
maths.place(x=100, y=125)
physics = tk.Frame(root, width=1920, height=100, bg="orange")
physics.place(x=100, y=250)
chem = tk.Frame(root, width=1920, height=100, bg="orange")
chem.place(x=100, y=375)
bio = tk.Frame(root, width=1920, height=100, bg="orange")
bio.place(x=100, y=500)
cs = tk.Frame(root, width=1920, height=100, bg="orange")
cs.place(x=100, y=625)
total = tk.Frame(root, width=1920, height=100, bg="orange")
total.place(x=100, y=750)

# Subject name
maths_label = tk.Label(maths, text="Maths", font=("Times", 16), bg="orange")
maths_label.place(x=50, y=10)
physics_label = tk.Label(physics, text="Physics", font=("Times", 16), bg="orange")
physics_label.place(x=50, y=10)
chem_label = tk.Label(chem, text="Chemistry", font=("Times", 16), bg="orange")
chem_label.place(x=50, y=10)
bio_label = tk.Label(bio, text="Biology", font=("Times", 16), bg="orange")
bio_label.place(x=50, y=10)
cs_label = tk.Label(cs, text="Computer Science", font=("Times", 16), bg="orange")
cs_label.place(x=50, y=10)
total_label = tk.Label(total, text="Total", font=("Times", 16), bg="orange")
total_label.place(x=50, y=10)

# Subject Timings
maths_timing = tk.Label(maths, text="9:00 - 10:00 AM",font=("Times", 16), bg="orange")
maths_timing.place(x=1200, y=10)
physics_timing = tk.Label(physics, text="9:00 - 10:00 AM",font=("Times", 16), bg="orange")
physics_timing.place(x=1200, y=10)
chem_timing = tk.Label(chem, text="9:00 - 10:00 AM", font=("Times", 16), bg="orange")
chem_timing.place(x=1200, y=10)
bio_timing = tk.Label(bio, text="9:00 - 10:00 AM", font=("Times", 16), bg="orange")
bio_timing.place(x=1200, y=10)
cs_timing = tk.Label(cs, text="9:00 - 10:00 AM", font=("Times", 16), bg="orange")
cs_timing.place(x=1200, y=10)

# Attendance
maths_att = tk.Label(maths, text="Attendance", font=("Times", 16), bg="orange")
maths_att.place(x=600, y=10)
physics_att = tk.Label(physics, text="Attendance", font=("Times", 16), bg="orange")
physics_att.place(x=600, y=10)
chem_att = tk.Label(chem, text="Attendance", font=("Times", 16), bg="orange")
chem_att.place(x=600, y=10)
bio_att = tk.Label(bio, text="Attendance", font=("Times", 16), bg="orange")
bio_att.place(x=600, y=10)
cs_att = tk.Label(cs, text="Attendance",font=("Times", 16),  bg="orange")
cs_att.place(x=600, y=10)
total_att = tk.Label(total, text="Attendance",font=("Times", 16),  bg="orange")
total_att.place(x=600, y=10)

# Attendance percentage
maths_att = tk.Label(maths, text=str(one), font=("Times", 16), bg="orange")
maths_att.place(x=625, y=55)
physics_att = tk.Label(physics, text=str(two), font=("Times", 16), bg="orange")
physics_att.place(x=625, y=55)
chem_att = tk.Label(chem, text=str(three), font=("Times", 16), bg="orange")
chem_att.place(x=625, y=55)
bio_att = tk.Label(bio, text=str(four), font=("Times", 16), bg="orange")
bio_att.place(x=625, y=55)
cs_att = tk.Label(cs, text=str(five),font=("Times", 16),  bg="orange")
cs_att.place(x=625, y=55)
total_att = tk.Label(total, text=str(total_percent), font=("Times", 16), bg="orange")
total_att.place(x = 625, y = 55)


root.mainloop()