# Futurense LMS
## Index:
1. [Database](#Database-Schema-for-Futurense)
2. [Project overview and Instructions](#Project-Overview) -- Check this for instructions 

# Database Schema for Futurense
## Tables and Attributes

### student
- `sid` (INT, Primary Key)
- `sname` (VARCHAR(50), NOT NULL)
- `phonenumber` (INT, NOT NULL)
- `age` (INT(2), NOT NULL)
- `gender` (ENUM("Male","Female","Others"))
- `email` (VARCHAR(50), UNIQUE)
- `address` (VARCHAR(100), NOT NULL)
- `password` (VARCHAR(100), NOT NULL)

### teacher
- `tid` (INT, Primary Key)
- `tname` (VARCHAR(50), NOT NULL)
- `phonenumber` (INT, NOT NULL)
- `age` (INT(2), NOT NULL)
- `gender` (ENUM("Male","Female","Others"))
- `email` (VARCHAR(50), UNIQUE)
- `address` (VARCHAR(100), NOT NULL)

### course
- `cid` (INT, Primary Key)
- `cname` (VARCHAR(100), NOT NULL)
- `tid` (INT, Foreign Key)

### Exams
- `eid` (INT, Primary Key)
- `ename` (VARCHAR(255), NOT NULL)
- `sid` (INT, Foreign Key)
- `cid` (INT, Foreign Key)

### Grade
- `gid` (INT, Primary Key)
- `cid` (INT, Foreign Key)
- `eid` (INT, Foreign Key)
- `sid` (INT, Foreign Key)
- `grades` (CHAR(1))

### Assignment
- `aid` (INT, AUTO_INCREMENT, Primary Key)
- `assignment_name` (VARCHAR(100), NOT NULL)
- `description` (TEXT)
- `deadline` (DATE)
- `cid` (INT, NOT NULL, Foreign Key)
- `tid` (INT, NOT NULL, Foreign Key)

### Attendance
- `atid` (INT, AUTO_INCREMENT, Primary Key)
- `sid` (INT, NOT NULL, Foreign Key)
- `cid` (INT, NOT NULL, Foreign Key)
- `attendance_date` (DATE, NOT NULL)
- `status` (ENUM('Present', 'Absent'), NOT NULL)

### student_course
- `sc_id` (INT, AUTO_INCREMENT, Primary Key)
- `sid` (INT, NOT NULL, Foreign Key)
- `cid` (INT, NOT NULL, Foreign Key)

## Relationships

### student - attendance
- A student can have multiple attendance records.
- Each attendance record belongs to one student.
- **One-to-Many (1:N)**

### teacher - course
- A teacher can teach multiple courses.
- Each course is taught by one teacher.
- **One-to-Many (1:N)**

### course - exams
- A course can have multiple exams.
- Each exam belongs to one course.
- **One-to-Many (1:N)**

### student - exams
- A student can take multiple exams.
- Each exam record is for one student.
- **One-to-Many (1:N)**

### course - grade
- A course can have multiple grades.
- Each grade is for one course.
- **One-to-Many (1:N)**

### exams - grade
- An exam can have multiple grades.
- Each grade is for one exam.
- **One-to-Many (1:N)**

### student - grade
- A student can have multiple grades.
- Each grade is for one student.
- **One-to-Many (1:N)**

### course - assignment
- A course can have multiple assignments.
- Each assignment is for one course.
- **One-to-Many (1:N)**

### teacher - assignment
- A teacher can assign multiple assignments.
- Each assignment is given by one teacher.
- **One-to-Many (1:N)**

## ER diagram
![ER diagram (2)](https://github.com/yashvisharma1204/Neural-Nexus/assets/137611141/e1f9ed1f-1cad-4d2f-bfeb-ec6ba507e940)

---
# Project Overview

## Technologies Used
- Python
- MySQL Connectivity
- Tkinter

## Python Pages

### [project.py](project.py)
The login page through which mainpage is attached

### [main.py](main.py)
Contains the main page or dashboard.

## Steps to Access the Application

1. **Clone the repository**
   ```bash
   git clone https://github.com/yashvisharma1204/Neural-Nexus
   ```
   
2. **Save the `lms.sql` file in your MySQL Workbench**
   - Open MySQL Workbench.
   - Open the `lms.sql` file and execute it to set up the database schema.

3. **Configure MySQL Connection**
   - Open `main.py` and `project.py`.
   - Locate the MySQL connection function and add your MySQL Workbench username and password.

4. **Run the Application**
   - Run `project.py` using the command:
     ```bash
     python project.py
     ```

5. **Login**
   - Use the following credentials to login:
     - **Email:** `ravi@example.com`
     - **Password:** `password123`
   - For testing Forgot password write the asked credentials the `OTP` will be generated in command line.
   - Enter it and password wil be changed

6. **Navigate the Application**
   - Once logged in, it will take **5-10 secs** for dasboard to open
   - Then, you will see the main page with buttons.
   - Click on the "Profile" button to toggle the profile view.

That's what has been done so far in the project.
***Currently the attendance and course page is being added by [Vaibhav](@vaibhavtamang12) and [Punit](@punitkumar4871) respectively.***
