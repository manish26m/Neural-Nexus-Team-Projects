# Futurense LMS
<img width="960" alt="image" src="https://github.com/yashvisharma1204/Neural-Nexus/assets/137611141/5bafb37c-1926-4263-9cc5-54ea86a829c9">

# Project Overview
Futurense LMS is a comprehensive Learning Management System designed to cater to the needs of both students and educators. This system provides a user-friendly interface for managing courses, assignments, grades, attendance, and exams. Students can easily log in, update passwords, and access a main dashboard where they can view their enrolled courses, submit assignments, check their grades, and monitor attendance records. Educators can manage their course content, create assignments, and track student progress. The LMS is built with a robust client-server architecture, using Tkinter for the client-side interface and MySQL for secure data storage and management. This ensures seamless interaction between the users and the system, providing a streamlined educational experience.
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
   - Open all `.py` files.
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
     
7. **Navigate to other section**
   - 
