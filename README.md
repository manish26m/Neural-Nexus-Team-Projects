# Neural Nexus 
## 📚 Futurense Database Schema


<img src="https://github.com/yashvisharma1204/Neural-Nexus/assets/150244397/c183e77b-f278-4c8d-a968-4532639bb9e1" alt="Futureense Database Schema" width="600" height="600">

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
