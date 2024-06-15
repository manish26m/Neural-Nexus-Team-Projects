# Neural Nexus 
## 📚 Futurense Database Schema

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/39e58570-f4ad-4ab7-a29f-4e54a1e0aa37/eda06363-14da-4a5d-8add-3fc7dbacefca/Untitled.png)

This document describes the entities, their attributes, and the relationships in the Futurense database schema.

### Entities and Attributes

#### 👨‍🎓 Student
- **🆔 sid**: Primary Key
- **📝 sname**
- **📞 phonenumber**: Multivalued
- **📧 email**
- **🏠 address**
- **🎂 age**: Derived
- **⚥ gender**

#### 👨‍🏫 Teacher
- **🆔 tid**: Primary Key
- **📝 tname**
- **📞 phonenumber**: Multivalued
- **📧 email**
- **🏠 address**
- **⚥ gender**
- **🎂 age**: Derived

#### 📘 Course
- **🆔 cid**: Primary Key
- **📚 cname**
- **🆔 sid**: Foreign Key
- **🆔 tid**: Foreign Key

#### ✍️ Exams
- **🆔 eid**: Primary Key
- **📝 ename**
- **🆔 sid**: Foreign Key
- **🆔 cid**: Foreign Key
- **🆔 gid**: Foreign Key

#### 🏅 Grade
- **🆔 gid**: Primary Key
- **🆔 cid**: Foreign Key
- **🆔 eid**: Foreign Key
- **🆔 sid**: Foreign Key
- **📝 grades**

### Relationships

#### 🤝 Enrolls
- **👨‍🎓 Student** to **📘 Course**: Many-to-Many

#### 🧑‍🏫 Teaches
- **👨‍🏫 Teacher** to **📘 Course**: One-to-Many

#### 📝 Takes
- **👨‍🎓 Student** to **✍️ Exams**: Many-to-Many

#### 📖 Includes
- **📘 Course** to **✍️ Exams**: One-to-Many

#### 📊 Has
- **✍️ Exams** to **🏅 Grade**: One-to-Many

#### 🎓 Receives
- **👨‍🎓 Student** to **🏅 Grade**: One-to-Many
