from tkinter import *
import mysql.connector
from datetime import datetime, date
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
from tkinter import messagebox

username = "root"
password = "Tiya1221"

# MySQL connection code
my_db = mysql.connector.connect(
    host="localhost",
    user=username,
    passwd=password,
    database="futurense"
)
cursor = my_db.cursor()
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

window = ThemedTk(theme='aqua')
window.geometry("1366x768")
window.title("Futurense")

# Load the background image
bg_image = Image.open("main_page/background.png")
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to display the background image
bg_label = Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Function to create a card button in the left column frame
def create_card_button(text, image_path, command, x, y):
    # Load image with LANCZOS resampling and resize to 250x150
    icon_image = Image.open(image_path)
    icon_image = icon_image.resize((250, 150), Image.LANCZOS)
    icon_photo = ImageTk.PhotoImage(icon_image)

    # Create button in the middle of the window
    button = Button(window, text=text, image=icon_photo, compound='top', command=command, borderwidth=0, width=250, height=180, font=('Georgia',12,'bold'))
    button.image = icon_photo  # keep a reference

    # Place button in the middle of the window
    button.place(x=x, y=y)

    return button

# Function definitions for button commands
def button_command():
    print("Button clicked")
create_card_button("Show Courses", "main_page/course.jpg", button_command, 100, 150)
create_card_button("Show Assignments", "main_page/assignment.jpg", button_command, 100, 450)
# Toggle function to show/hide the left column

left_column_width = 0.25 * 1366  # 25% of the window width
left_column_frame = Frame(window, width=left_column_width, bg='goldenrod2')
pic=Image.open('main_page/graduated.png')
pic=pic.resize((100,100),Image.LANCZOS)
profile_pic=ImageTk.PhotoImage(pic)
left_pic_label=Label(left_column_frame,image=profile_pic,bg='goldenrod2')
left_column_label = Label(left_column_frame, text="Profile", bg='goldenrod2',fg='white', font=('Georgia', 30,'bold'))
left_name_label = Label(left_column_frame, text="Name:", bg='goldenrod2',fg='white', font=('Georgia', 16,'bold'))
left_phone_label = Label(left_column_frame, text="Phone no.:", bg='goldenrod2',fg='white', font=('Georgia', 16,'bold'))
left_age_label = Label(left_column_frame, text="Age:", bg='goldenrod2',fg='white', font=('Georgia', 16,'bold'))
left_gender_label = Label(left_column_frame, text="Gender:", bg='goldenrod2',fg='white', font=('Georgia', 16,'bold'))
left_address_label = Label(left_column_frame, text="Address:", bg='goldenrod2',fg='white', font=('Georgia', 16,'bold'))

left_column_frame.place_forget()
left_column_visible = False

def toggle_left_column():
    global left_column_visible
    if left_column_visible:
        left_column_frame.place_forget()
        left_column_visible = False
    else:
        left_column_frame.place(x=0, y=100, relheight=1, anchor='nw')
        left_column_visible = True

        # Read the user_entry from the text file
        with open("logged_in_user.txt", "r") as file:
            user = file.read()

        # Fetch the student's information from the database
        query = "SELECT * FROM student WHERE email = %s"
        cursor.execute(query, (user,))
        result = cursor.fetchone()

        if result:
            # Display the student's information in the left column
            left_pic_label.place(x=100, y=70)
            left_name_label.config(text=f"Name: {result[1]}")  # Assuming the name is the second column in the database
            left_name_label.place(x=50, y=200, anchor='nw')
            left_phone_label.config(text=f"Phone no.: {result[2]}")  # Assuming the phone number is the third column in the database
            left_phone_label.place(x=50, y=270, anchor='nw')
            left_address_label.config(text=f"Address: {result[3]}")  # Assuming the address is the fourth column in the database
            left_address_label.place(x=50, y=340, anchor='nw')
            left_age_label.config(text=f"Age: {result[4]}")  # Assuming the age is the fifth column in the database
            left_age_label.place(x=50, y=410, anchor='nw')
            left_gender_label.config(text=f"Gender: {result[5]}")  # Assuming the gender is the sixth column in the database
            left_gender_label.place(x=50, y=480, anchor='nw')
        else:
            messagebox.showerror("Error", "Student not found")
# Load the account icon
icon_image = Image.open("main_page/account.png")
icon_image = icon_image.resize((50, 50), Image.LANCZOS)  # Resize the image to 50x50
icon_photo = ImageTk.PhotoImage(icon_image)

# Create a button with the icon for toggling left column visibility
toggle_button = Button(window, image=icon_photo, command=toggle_left_column, borderwidth=0)
toggle_button.place(x=1200, y=120)  # Place the button in the middle below the header

# Create card buttons directly on the window
create_card_button("Show Attendance", "main_page/attendance.jpg", button_command, 480, 300)
create_card_button("Show Grades", "main_page/grades.jpg", button_command, 850, 450)
create_card_button("Show Exams", "main_page/exams.jpg", button_command, 850, 150)
# Create a header frame
header_frame = Frame(window, height=120, bg='black')
header_frame.place(x=0, y=0, relwidth=1)

# Add label to the header frame
header_label = Label(header_frame, text="Learning Management System", bg='black', fg='white', font=('Georgia', 30,'bold'))
header_label.pack(pady=30)  # Adjust padding as necessary to center the text vertically

window.mainloop()
