# CampusConnect 🎓
### College Event Management System

CampusConnect is a Python-based, terminal-driven College Event Management System developed using Object-Oriented Programming (OOP) principles.

The application provides a centralized platform for students to explore and register for college events, organizers to manage events, and administrators to oversee the system.

---

## ✨ Features

### 1. Student Module
- View all available college events.
- Register for events.
- Cancel event registrations.
- View registered events.
- Check event details and availability.

### 2. Organizer Module
- Create new college events.
- View events created by them.
- Update event details.
- Delete their own events.
- View registered participants.

### 3. Admin Module
- View all registered users.
- View all available events.
- Monitor overall system statistics.
- Access administrative dashboard.

### 4. Additional Features
- Role-based login system.
- Unique user and event IDs.
- Event capacity management.
- Prevention of duplicate registrations.
- Input validation and exception handling.
- Preloaded sample events for demonstration.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| OOP | Application architecture |
| `abc` module | Abstraction |
| `input()` and `print()` | Terminal interface |
| Exception Handling | Error management |

No external libraries or frameworks are required.

---

## 🧩 Object-Oriented Programming Concepts

CampusConnect demonstrates the four fundamental pillars of OOP:

**1. Encapsulation**
- Private attributes are implemented using double underscores.
- Getter and setter methods provide controlled access to data.

**2. Inheritance**
- `Student`, `Organizer`, and `Admin` inherit from the abstract `User` class.
- Common attributes and methods are reused through inheritance.

**3. Polymorphism**
- Each user role implements its own `display_dashboard()` method.
- The same method behaves differently depending on the object.

**4. Abstraction**
- The `User` class is implemented as an abstract base class using `ABC`.
- The abstract `display_dashboard()` method is implemented by its child classes.

**Additional Concept – Composition**

- The `EventManager` manages collections of users and events.
- Students maintain their registered events.
- Organizers maintain the events they create.

---

## 📁 Project Structure

```text
CampusConnect/
│
├── main.py
├── user.py
├── student.py
├── organizer.py
├── admin.py
├── event.py
├── event_manager.py
├── data.json
└── README.md
```

### File Description

| File | Description |
|---|---|
| `main.py` | Main application and menu navigation |
| `user.py` | Abstract parent User class |
| `student.py` | Student operations |
| `organizer.py` | Event management operations |
| `admin.py` | Administrative operations |
| `event.py` | Event attributes and registration logic |
| `event_manager.py` | Central management of users and events |
| `data.json` | Reserved for data storage |

---

## 🚀 How to Run

**Prerequisites:** Python 3 installed on your system.

1. Clone the repository:

```bash
git clone https://github.com/AnanyaV2408/CampusConnect](https://github.com/AnanyaV2408/CampusConnect
```

2. Navigate to the project directory:

```bash
cd CampusConnect
```

3. Run the application:

```bash
python3 main.py
```

The application will start directly in the terminal.

---

## 🔐 Default Admin Credentials

For demonstration purposes:

- **Email:** admin@campus.com
- **Password:** admin123

Students and organizers can create their accounts through the registration menu.

---

## 🧪 Sample Events

The application includes four preloaded demonstration events:

| Event | Category |
|---|---|
| Tech Symposium | Technical |
| Dance Showcase | Cultural |
| Hackathon 2026 | Technical |
| Sports Meet | Sports |

These events allow users to explore the registration functionality immediately.

---

## 🎯 Project Objective

The primary objective of CampusConnect is to apply fundamental Object-Oriented Programming concepts to a practical real-world application.

The project focuses on modular programming, code reusability, role-based functionality, and effective management of college events.

---

**Developed as part of a Python Object-Oriented Programming Assessment.**
