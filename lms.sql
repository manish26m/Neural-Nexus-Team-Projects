create database futurense;
use futurense;

create table student(
sid int primary key auto_increment,
sname varchar(50) not null,
phonenumber int not null,
age int(2) not null,
gender enum("Male","Female","Others"),
email varchar(50) unique,
address varchar(100) not null,
password varchar(100) not null
);

create table teacher(
tid int primary key auto_increment,
tname varchar(50) not null,
phonenumber int not null,
age int(2) not null,
gender enum("Male","Female","Others"),
email varchar(50) unique,
address varchar(100) not null

);
CREATE TABLE course (
    cid INT AUTO_INCREMENT PRIMARY KEY,
    cname VARCHAR(100) NOT NULL,
    tid INT,
    sid INT,
    FOREIGN KEY (tid) REFERENCES teacher(tid),
    FOREIGN KEY (sid) REFERENCES student(sid)
);
CREATE TABLE Grade (
    gid INT PRIMARY KEY,
    cid INT,
    eid INT,
    sid INT,
    grades CHAR(1), -- Assuming grades are represented by a single character (A, B, C, etc.)
    FOREIGN KEY (cid) REFERENCES Course(cid),
    FOREIGN KEY (eid) REFERENCES Exams(eid),
    FOREIGN KEY (sid) REFERENCES Student(sid)
);
CREATE TABLE Exams (
    eid INT PRIMARY KEY,
    ename VARCHAR(255) NOT NULL,
    sid INT,
    cid INT,
    FOREIGN KEY (sid) REFERENCES Student(sid),
    FOREIGN KEY (cid) REFERENCES Course(cid)
);


CREATE TABLE Assignment (
    aid INT AUTO_INCREMENT PRIMARY KEY,
    assignment_name VARCHAR(100) NOT NULL,
    description TEXT,
    deadline DATE,
    cid INT NOT NULL,
    tid INT NOT NULL,
    FOREIGN KEY (cid) REFERENCES Course(cid),
    FOREIGN KEY (tid) REFERENCES Teacher(tid)
);

CREATE TABLE Attendance (
    atid INT AUTO_INCREMENT PRIMARY KEY,
    sid INT NOT NULL,
    cid INT NOT NULL,
    attendance_date DATE NOT NULL,
    status ENUM('Present', 'Absent') NOT NULL,
    FOREIGN KEY (sid) REFERENCES student(sid),
    FOREIGN KEY (cid) REFERENCES course(cid)
);

INSERT INTO student (sname, phonenumber, age, gender, email, address, password) VALUES
('Ravi Kumar', '9876543210', 21, 'Male', 'ravi@example.com', 'Delhi, India', 'password123'),
('Sita Sharma', '8765432109', 22, 'Female', 'sita@example.com', 'Mumbai, India', 'password123'),
('Arjun Singh', '7654321098', 23, 'Male', 'arjun@example.com', 'Chennai, India', 'password123'),
('Priya Patel', '6543210987', 20, 'Female', 'priya@example.com', 'Kolkata, India', 'password123'),
('Vijay Rao', '5432109876', 21, 'Male', 'vijay@example.com', 'Hyderabad, India', 'password123'),
('Anita Das', '4321098765', 22, 'Female', 'anita@example.com', 'Pune, India', 'password123'),
('Amit Joshi', '3210987654', 23, 'Male', 'amit@example.com', 'Ahmedabad, India', 'password123'),
('Meena Reddy', '2109876543', 20, 'Female', 'meena@example.com', 'Bangalore, India', 'password123'),
('Rajesh Mehta', '1098765432', 21, 'Male', 'rajesh@example.com', 'Surat, India', 'password123'),
('Neha Gupta', '0987654321', 22, 'Female', 'neha@example.com', 'Jaipur, India', 'password123');

INSERT INTO teacher (tname, phonenumber, age, gender, email, address) VALUES
('Dr. Ashok Verma', '9988776655', 45, 'Male', 'ashok@example.com', 'Delhi, India'),
('Prof. Sunita Kapoor', '8877665544', 40, 'Female', 'sunita@example.com', 'Mumbai, India'),
('Dr. Rajan Iyer', '7766554433', 50, 'Male', 'rajan@example.com', 'Chennai, India'),
('Prof. Kavita Sharma', '6655443322', 38, 'Female', 'kavita@example.com', 'Kolkata, India'),
('Dr. Mohan Patel', '5544332211', 42, 'Male', 'mohan@example.com', 'Hyderabad, India');

INSERT INTO course (cname, tid, sid) VALUES
('Mathematics', 1, 1),
('Physics', 2, 2),
('Chemistry', 3, 3),
('Biology', 4, 4),
('Computer Science', 5, 5),
('Mathematics', 1, 6),
('Physics', 2, 7),
('Chemistry', 3, 8),
('Biology', 4, 9),
('Computer Science', 5, 10);

INSERT INTO Attendance (sid, cid, attendance_date, status) VALUES
(1, 1, '2024-06-01', 'Present'),
(2, 2, '2024-06-01', 'Absent'),
(3, 3, '2024-06-01', 'Present'),
(4, 4, '2024-06-01', 'Present'),
(5, 5, '2024-06-01', 'Absent'),
(6, 1, '2024-06-02', 'Present'),
(7, 2, '2024-06-02', 'Present'),
(8, 3, '2024-06-02', 'Absent'),
(9, 4, '2024-06-02', 'Present'),
(10, 5, '2024-06-02', 'Present');
