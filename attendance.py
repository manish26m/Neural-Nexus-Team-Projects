import tkinter as tk
import mysql.connector
from PIL import Image, ImageTk
import subprocess
username = "root"
password = "Tiya1221"

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
with open("log.txt", "r") as file:
    user = file.read()
# 1st subject
cursor = my_db.cursor()
query="SELECT (COUNT(CASE WHEN status = 'Present' THEN 1 END) / COUNT(status)) * 100 from Attendance where sid = (select sid from student where email=%s) and cid = 36;"
cursor.execute(query,(user,))
tables = cursor.fetchall()

for i in tables:
    one = int(i[0])

# 2nd subject
cursor = my_db.cursor()
query="SELECT (COUNT(CASE WHEN status = 'Present' THEN 1 END) / COUNT(status)) * 100 from Attendance where sid = (select sid from student where email=%s) and cid = 37;"
cursor.execute(query,(user,))
tables = cursor.fetchall()

for i in tables:
    two = int(i[0])

# 3rd subject
cursor = my_db.cursor()
query="SELECT (COUNT(CASE WHEN status = 'Present' THEN 1 END) / COUNT(status)) * 100 from Attendance where sid = (select sid from student where email=%s) and cid = 38;"
cursor.execute(query,(user,))
tables = cursor.fetchall()

for i in tables:
    three = int(i[0])

# 4th subject
cursor = my_db.cursor()
query="SELECT (COUNT(CASE WHEN status = 'Present' THEN 1 END) / COUNT(status)) * 100 from Attendance where sid = (select sid from student where email=%s) and cid = 39;"
cursor.execute(query,(user,))
tables = cursor.fetchall()

for i in tables:
    four = int(i[0])

# 5th subject
cursor = my_db.cursor()
query="SELECT (COUNT(CASE WHEN status = 'Present' THEN 1 END) / COUNT(status)) * 100 from Attendance where sid = (select sid from student where email=%s) and cid = 40;"
cursor.execute(query,(user,))
tables = cursor.fetchall()

for i in tables:
    five = int(i[0])

cursor = my_db.cursor()
query="SELECT (COUNT(CASE WHEN status = 'Present' THEN 1 END) / COUNT(status)) * 100 from Attendance where sid = (select sid from student where email=%s) and cid = 41;"
cursor.execute(query,(user,))
tables = cursor.fetchall()

for i in tables:
    six = int(i[0])

# total
total_percent = (one + two + three + four + five+six)/6


def grade():
    root.destroy()
    subprocess.run(["python", "grade.py"])
def course():
    subprocess.run(["python", "course_page.py"])
    root.destroy()
def home():
    root.destroy()
    subprocess.run(["python", "main.py"])

def assignment():
    root.destroy()
    subprocess.run(["python", "Assignment/main1.py"])

def exams():
    root.destroy()
    subprocess.run(["python", "exam.py"])
root = tk.Tk()
root.title("Attendance")
root.geometry("1378x700")  # Set the geometry of the window

# Sidebar Frane
sidebar = tk.Frame(root, width=360, bg="gray16")
sidebar.place(x=0, y=105, height=800, width=150)  

# Create a frame for the header with black background
header = tk.Frame(root, bg="black", width=1378, height=120)
header.pack()

# Create a label inside the header frame
header_label = tk.Label(header, text="Attendance", fg="white", bg="black", font=("Georgia", 24, "bold"))
header_label.place(relx=0.5, rely=0.5, anchor="center")


# Image label
pil_image = Image.open("background2.jpeg")
pil_image = pil_image.resize((100, 100))
lpu_image = Image.open("background3.jpeg")
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


# Buttons
button1 = tk.Button(sidebar, text="Home", bg="black", fg="white", font=('Helvetica',12),command=home, height=2, width=10)
button1.pack(pady=35)

button2 = tk.Button(sidebar, text="Courses", bg="black", fg="white", font=('Helvetica',12), command = course,height=2, width=10)
button2.pack(pady=35)

button3 = tk.Button(sidebar, text="Assignment", bg="black", fg="white", font=('Helvetica',12), command=assignment,height=2, width=10)
button3.pack(pady=35)

button4 = tk.Button(sidebar, text="Grades", bg="black", fg="white", font=('Helvetica',12), command=grade,height=2, width=10)
button4.pack(pady=35)

button5 = tk.Button(sidebar, text="Exams", bg="black", fg="white", command=exams,height=2, width=10)
button5.pack(pady=35)

# Create subject frame
maths = tk.Frame(root, width=900, height=80, bg="goldenrod2")
maths.place(x=200, y=125)
physics = tk.Frame(root, width=900, height=80, bg="goldenrod2")
physics.place(x=200, y=215)
chem = tk.Frame(root, width=900, height=80, bg="goldenrod2")
chem.place(x=200, y=305)
bio = tk.Frame(root, width=900, height=80, bg="goldenrod2")
bio.place(x=200, y=395)
cs = tk.Frame(root, width=900, height=80, bg="goldenrod2")
cs.place(x=200, y=485)
se=tk.Frame(root,width=900,height=80, bg='goldenrod2')
se.place(x=200, y=575)


# Subject name
maths_label = tk.Label(maths, text="Mathematics", font=("Times", 16), bg="goldenrod2")
maths_label.place(x=50, y=10)
physics_label = tk.Label(physics, text="DSA", font=("Times", 16), bg="goldenrod2")
physics_label.place(x=50, y=10)
chem_label = tk.Label(chem, text="DBMS", font=("Times", 16), bg="goldenrod2")
chem_label.place(x=50, y=10)
bio_label = tk.Label(bio, text="Data Networking and Communication", font=("Times", 16), bg="goldenrod2")
bio_label.place(x=50, y=10)
cs_label = tk.Label(cs, text="Python", font=("Times", 16), bg="goldenrod2")
cs_label.place(x=50, y=10)
se_label = tk.Label(se, text="Software Engineering", font=("Times", 16), bg="goldenrod2", fg='black')
se_label.place(x=50, y=10)

# Subject Timings
maths_timing = tk.Label(maths, text="9:00 - 10:00 AM",font=("Times", 16), bg="goldenrod2")
maths_timing.place(x=1200, y=10)
physics_timing = tk.Label(physics, text="9:00 - 10:00 AM",font=("Times", 16), bg="goldenrod2")
physics_timing.place(x=1200, y=10)
chem_timing = tk.Label(chem, text="9:00 - 10:00 AM", font=("Times", 16), bg="goldenrod2")
chem_timing.place(x=1200, y=10)
bio_timing = tk.Label(bio, text="9:00 - 10:00 AM", font=("Times", 16), bg="goldenrod2")
bio_timing.place(x=1200, y=10)
cs_timing = tk.Label(cs, text="9:00 - 10:00 AM", font=("Times", 16), bg="goldenrod2")
cs_timing.place(x=1200, y=10)
se_timing = tk.Label(se, text="9:00 - 10:00 AM", font=("Times", 16), bg="goldenrod2")
se_timing.place(x=1200, y=10)

# Attendance
maths_att = tk.Label(maths, text="Attendance", font=("Times", 16), bg="goldenrod2")
maths_att.place(x=600, y=10)
physics_att = tk.Label(physics, text="Attendance", font=("Times", 16), bg="goldenrod2")
physics_att.place(x=600, y=10)
chem_att = tk.Label(chem, text="Attendance", font=("Times", 16), bg="goldenrod2")
chem_att.place(x=600, y=10)
bio_att = tk.Label(bio, text="Attendance", font=("Times", 16), bg="goldenrod2")
bio_att.place(x=600, y=10)
cs_att = tk.Label(cs, text="Attendance",font=("Times", 16),  bg="goldenrod2")
cs_att.place(x=600, y=10)
se_att = tk.Label(se, text="Attendance",font=("Times", 16),  bg="goldenrod2")
se_att.place(x=600,y=10)

# Attendance percentage
maths_att = tk.Label(maths, text=str(one), font=("Times", 16), bg="goldenrod2")
maths_att.place(x=625, y=55)
physics_att = tk.Label(physics, text=str(two), font=("Times", 16), bg="goldenrod2")
physics_att.place(x=625, y=55)
chem_att = tk.Label(chem, text=str(three), font=("Times", 16), bg="goldenrod2")
chem_att.place(x=625, y=55)
bio_att = tk.Label(bio, text=str(four), font=("Times", 16), bg="goldenrod2")
bio_att.place(x=625, y=55)
cs_att = tk.Label(cs, text=str(five),font=("Times", 16),  bg="goldenrod2")
cs_att.place(x=625, y=55)
total_att = tk.Label(se, text=str(six), font=("Times", 16), bg="goldenrod2")
total_att.place(x = 625, y = 55)


root.mainloop()
