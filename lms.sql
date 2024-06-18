create database futurense;
use futurense;
create table student(
sid int primary key,
sname varchar(50) not null,
phonenumber int not null,
age int(2) not null,
gender enum("Male","Female","Others"),
email varchar(50) unique,
address varchar(100) not null,
password varchar(100) not null
);

create table teacher(
tid int primary key ,
tname varchar(50) not null,
phonenumber int not null,
age int(2) not null,
gender enum("Male","Female","Others"),
email varchar(50) unique,
address varchar(100) not null

);
CREATE TABLE course (
    cid INT PRIMARY KEY,
    cname VARCHAR(100) NOT NULL,
    tid INT,
    FOREIGN KEY (tid) REFERENCES teacher(tid)
);
CREATE TABLE Exams (
    eid INT  PRIMARY KEY,
    ename VARCHAR(255) NOT NULL,
    sid INT,
    cid INT,
    FOREIGN KEY (sid) REFERENCES Student(sid),
    FOREIGN KEY (cid) REFERENCES Course(cid)
);
CREATE TABLE Grade (
    gid INT  PRIMARY KEY,
    cid INT,
    eid INT,
    sid INT,
    grades CHAR(1), -- Assuming grades are represented by a single character (A, B, C, etc.)
    FOREIGN KEY (cid) REFERENCES Course(cid),
    FOREIGN KEY (eid) REFERENCES Exams(eid),
    FOREIGN KEY (sid) REFERENCES Student(sid)
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

CREATE TABLE student_course(
     sc_id INT AUTO_INCREMENT PRIMARY KEY,
	 sid INT NOT NULL,
	 cid INT NOT NULL,
     FOREIGN KEY (sid) REFERENCES student(sid),
	 FOREIGN KEY (cid) REFERENCES course(cid)
);

INSERT INTO student (sid,sname, phonenumber, age, gender, email, address, password) VALUES
(1,'Ravi Kumar', '987654321', 21, 'Male', 'ravi@example.com', 'Delhi, India', 'password123'),
(2,'Sita Sharma', '876543210', 22, 'Female', 'sita@example.com', 'Mumbai, India', 'password123'),
(3,'Arjun Singh', '765432109', 23, 'Male', 'arjun@example.com', 'Chennai, India', 'password123'),
(4,'Priya Patel', '654321098', 20, 'Female', 'priya@example.com', 'Kolkata, India', 'password123'),
(5,'Vijay Rao', '543210987', 21, 'Male', 'vijay@example.com', 'Hyderabad, India', 'password123'),
(6,'Anita Das', '432109876', 22, 'Female', 'anita@example.com', 'Pune, India', 'password123'),
(7,'Amit Joshi', '321098765', 23, 'Male', 'amit@example.com', 'Ahmedabad, India', 'password123'),
(8,'Meena Reddy', '210987653', 20, 'Female', 'meena@example.com', 'Bangalore, India', 'password123'),
(9,'Rajesh Mehta', '109876432', 21, 'Male', 'rajesh@example.com', 'Surat, India', 'password123'),
(10,'Neha Gupta', '098765421', 22, 'Female', 'neha@example.com', 'Jaipur, India', 'password123');

INSERT INTO teacher (tid,tname, phonenumber, age, gender, email, address) VALUES
(12,'Dr. Ashok Verma', '988776655', 45, 'Male', 'ashok@example.com', 'Delhi, India'),
(13,'Prof. Sunita Kapoor', '877665544', 40, 'Female', 'sunita@example.com', 'Mumbai, India'),
(14,'Dr. Rajan Iyer', '776654433', 50, 'Male', 'rajan@example.com', 'Chennai, India'),
(15,'Prof. Kavita Sharma', '655443322', 38, 'Female', 'kavita@example.com', 'Kolkata, India'),
(16,'Dr. Mohan Patel', '554432211', 42, 'Male', 'mohan@example.com', 'Hyderabad, India'),
(17,'mr. pramod vishwakarma','554432211',36,'Male','pramod@gmail.com','Chandigarh,India');

INSERT INTO course (cid,cname, tid) VALUES
(36,'Mathematics', 12),
(37,'DSA', 13),
(38,'DBMS', 14),
(39,'Data Networking and Communication', 15),
(40,'Software Engineering', 16),
(41,'Python',17);


INSERT INTO Attendance (sid, cid, attendance_date, status) VALUES
(1, 36, '2024-06-01', 'Present'),
(2, 36, '2024-06-01', 'Absent'),
(3, 36, '2024-06-01', 'Present'),
(4, 36, '2024-06-01', 'Present'),
(5, 36, '2024-06-01', 'Absent'),
(6, 36, '2024-06-02', 'Present'),
(7, 36, '2024-06-02', 'Present'),
(8, 36, '2024-06-02', 'Absent'),
(9, 36, '2024-06-02', 'Present'),
(10, 36, '2024-06-02', 'Present'),
(1, 37, '2024-06-01', 'Present'),
(2, 37, '2024-06-01', 'Absent'),
(3, 37, '2024-06-01', 'Present'),
(4, 37, '2024-06-01', 'Present'),
(5, 37, '2024-06-01', 'Absent'),
(6, 37, '2024-06-02', 'Present'),
(7, 37, '2024-06-02', 'Present'),
(8, 37, '2024-06-02', 'Absent'),
(9, 37, '2024-06-02', 'Present'),
(10,37, '2024-06-02', 'Present'),
(1, 38, '2024-06-01', 'Present'),
(2, 38, '2024-06-01', 'Absent'),
(3, 38, '2024-06-01', 'Present'),
(4, 38, '2024-06-01', 'Present'),
(5, 38, '2024-06-01', 'Absent'),
(6, 38, '2024-06-02', 'Present'),
(7, 38, '2024-06-02', 'Present'),
(8, 38, '2024-06-02', 'Absent'),
(9, 38, '2024-06-02', 'Present'),
(10,38, '2024-06-02', 'Present'),
(1, 39, '2024-06-01', 'Present'),
(2, 39, '2024-06-01', 'Absent'),
(3, 39, '2024-06-01', 'Present'),
(4, 39, '2024-06-01', 'Present'),
(5, 39, '2024-06-01', 'Absent'),
(6, 39, '2024-06-02', 'Present'),
(7, 39, '2024-06-02', 'Present'),
(8, 39, '2024-06-02', 'Absent'),
(9, 39, '2024-06-02', 'Present'),
(10,39, '2024-06-02', 'Present'),
(1, 40, '2024-06-01', 'Present'),
(2,  40, '2024-06-01', 'Absent'),
(3,  40, '2024-06-01', 'Present'),
(4,  40, '2024-06-01', 'Present'),
(5,  40, '2024-06-01', 'Absent'),
(6,  40, '2024-06-02', 'Present'),
(7,  40, '2024-06-02', 'Present'),
(8,  40, '2024-06-02', 'Absent'),
(9,  40, '2024-06-02', 'Present'),
(10,  40, '2024-06-02', 'Present'),
(1, 41, '2024-06-01', 'Present'),
(2, 41, '2024-06-01', 'Absent'),
(3, 41, '2024-06-01', 'Present'),
(4, 41, '2024-06-01', 'Present'),
(5, 41, '2024-06-01', 'Absent'),
(6, 41, '2024-06-02', 'Present'),
(7, 41, '2024-06-02', 'Present'),
(8, 41, '2024-06-02', 'Absent'),
(9, 41, '2024-06-02', 'Present'),
(10, 41, '2024-06-02', 'Present');


INSERT INTO Exams (eid,ename, sid, cid) VALUES
(61,'Midterm Mathematics', 1,36),
(62,'Midterm Mathematics', 2, 36),
(63,'Midterm Mathematics', 3, 36),
(64,'Midterm Mathematics', 4, 36),
(65,'Midterm Mathematics', 5, 36),
(66,'Midterm Mathematics', 6, 36),
(67,'Midterm Mathematics', 7, 36),
(68,'Midterm Mathematics', 8, 36),
(69,'Midterm Mathematics', 9, 36),
(70,'Midterm Mathematics', 10, 36),
(71,'Midterm DSA', 1, 37),
(72,'Midterm DSA', 2, 37),
(73,'Midterm DSA', 3, 37),
(74,'Midterm DSA', 4, 37),
(75,'Midterm DSA', 5, 37),
(76,'Midterm DSA', 6, 37),
(77,'Midterm DSA', 7, 37),
(78,'Midterm DSA', 8, 37),
(79,'Midterm DSA', 9, 37),
(80,'Midterm DSA', 10, 37),
(81,'Midterm DBMS', 1, 38),
(82,'Midterm DBMS', 2, 38),
(83,'Midterm DBMS', 3, 38),
(84,'Midterm DBMS', 4, 38),
(85,'Midterm DBMS', 5, 38),
(86,'Midterm DBMS', 6, 38),
(87,'Midterm DBMS', 7, 38),
(88,'Midterm DBMS', 8, 38),
(89,'Midterm DBMS', 9, 38),
(90,'Midterm DBMS', 10, 38),
(91,'Data Networking and Communication', 1, 39),
(92,'Data Networking and Communication', 2, 39),
(93,'Data Networking and Communication', 3, 39),
(94,'Data Networking and Communication', 4, 39),
(95,'Data Networking and Communication', 5, 39),
(96,'Data Networking and Communication', 6, 39),
(97,'Data Networking and Communication', 7, 39),
(98,'Data Networking and Communication', 8, 39),
(99,'Data Networking and Communication', 9, 39),
(100,'Data Networking and Communication', 10, 39),
(101,'Software Engineering', 1, 40),
(102,'Software Engineering', 2, 40),
(103,'Software Engineering', 3, 40),
(104,'Software Engineering', 4, 40),
(105,'Software Engineering', 5, 40),
(106,'Software Engineering', 6, 40),
(107,'Software Engineering', 7, 40),
(108,'Software Engineering', 8, 40),
(109,'Software Engineering', 9, 40),
(110,'Software Engineering', 10, 40),
(111,'Python',1,41),
(112,'Python',2,41),
(113,'Python',3,41),
(114,'Python',4,41),
(115,'Python',5,41),
(116,'Python',6,41),
(117,'Python',7,41),
(118,'Python',8,41),
(119,'Python',9,41),
(120,'Python',10,41);

-- Insert data into Grade
INSERT INTO Grade (gid,cid, eid, sid, grades) VALUES
(1,36, 61, 1, 'A'),
(2,36, 62, 2, 'B'),
(3,36, 63, 3, 'A'),
(4,36, 64, 4, 'C'),
(5,36, 65, 5, 'B'),
(6,36, 66, 6, 'A'),
(7,36, 67, 7, 'B'),
(8,36, 68, 8, 'A'),
(9,36, 69, 9, 'C'),
(10,36, 70, 10, 'B'),
(11,37, 71, 1, 'A'),
(12,37, 72, 2, 'B'),
(13,37, 73, 3, 'A'),
(14,37, 74, 4, 'C'),
(15,37, 75, 5, 'B'),
(16,37, 76, 6, 'A'),
(17,37, 77, 7, 'B'),
(18,37, 78, 8, 'A'),
(19,37, 79, 9, 'C'),
(20,37, 80, 10, 'B'),
(21,38, 81, 1, 'A'),
(22,38, 82, 2, 'B'),
(23,38, 83, 3, 'A'),
(24,38, 84, 4, 'C'),
(25,38, 85, 5, 'B'),
(26,38, 86, 6, 'A'),
(27,38, 87, 7, 'B'),
(28,38, 88, 8, 'A'),
(29,38, 89, 9, 'C'),
(30,38, 90, 10, 'B'),
(31,39, 91, 1, 'A'),
(32,39, 92, 2, 'B'),
(33,39, 93, 3, 'A'),
(34,39, 94, 4, 'C'),
(35,39, 95, 5, 'B'),
(36,39, 96, 6, 'A'),
(37,39, 97, 7, 'B'),
(38,39, 98, 8, 'A'),
(39,39, 99, 9, 'C'),
(40,39, 100, 10, 'B'),
(41,40, 101, 1, 'A'),
(42,40, 102, 2, 'B'),
(43,40, 103, 3, 'A'),
(44,40, 104, 4, 'C'),
(45,40, 105, 5, 'B'),
(46,40, 106, 6, 'A'),
(47,40, 107, 7, 'B'),
(48,40, 108, 8, 'A'),
(49,40, 109, 9, 'C'),
(50,40, 110, 10, 'B'),
(51,41, 111, 1, 'A'),
(52,41, 112, 2, 'B'),
(53,41, 113, 3, 'A'),
(54,41, 114, 4, 'C'),
(55,41, 115, 5, 'B'),
(56,41, 116, 6, 'A'),
(57,41, 117, 7, 'B'),
(58,41, 118, 8, 'A'),
(59,41, 119, 9, 'C'),
(60,41, 120, 10, 'B');

-- Insert data into Assignment
INSERT INTO Assignment (assignment_name, description, deadline, cid, tid) VALUES
('Math Assignment 1', 'Algebra problems', '2024-07-01', 36, 12),
('dsa Assignment 1', 'dsa problems', '2024-07-01', 37, 13),
('dbms Assignment 1', 'dbms problems', '2024-07-01', 38, 14),
('dc Assignment 1', 'dc questions', '2024-07-01', 39, 15),
('software Assignment 1', 'Programming in Python', '2024-07-01', 40, 16),
('Python Assignment 1','Python problem','2024-07-01',41,17);


INSERT INTO student_course(sid,cid) VALUES
( 1,36),
(2, 36),
( 3, 36),
( 4, 36),
(5,36),
(6,36),
(7,36),
(8,36),
(9,36),
(10,36),
(1,37),
(2,37),
(3,37),
(4,37),
(5,37),
(6,37),
(7,37),
(8,37),
(9,37),
(10,37),
(1,38),
(2,38),
(3,38),
(4,38),
(5,38),
(6,38),
(7,38),
(8,38),
(9,38),
(10,38),
(1,39),
(2,39),
(3,39),
(4,39),
(5,39),
(6,39),
(7,39),
(8,39),
(9,39),
(10,39),
(1,40),
(2,40),
(3,40),
(4,40),
(5,40),
(6,40),
(7,40),
(8,40),
(9,40),
(10,40),
(1,41),
(2,41),
(3,41),
(4,41),
(5,41),
(6,41),
(7,41),
(8,41),
(9,41),
(10,41);
-- dont add auto- increment in table which are taking reference --
