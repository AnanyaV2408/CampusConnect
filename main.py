
from student import Student
from organizer import Organizer
from admin import Admin
from event import Event
from event_manager import EventManager

campus = EventManager()

# Default admin
campus.add_user(Admin("ADM001", "Admin", "admin@campus.com", "admin123"))

# Sample events
samples = [
    Event("EVT001", "Tech Symposium", "Technical", "15-11-2026",
          "AB1 Auditorium", "Annual technical fest", 100),
    Event("EVT002", "Dance Showcase", "Cultural", "18-11-2026",
          "Main Auditorium", "College dance competition", 50),
    Event("EVT003", "Hackathon 2026", "Technical", "20-11-2026",
          "Computer Lab", "Coding challenge", 80),
    Event("EVT004", "Sports Meet", "Sports", "25-11-2026",
          "College Ground", "Annual sports competition", 150)
]

for event in samples:
    campus.add_event(event)


def register():
    print("\n1. Student\n2. Organizer")
    role = input("Choose role: ")

    if role not in ["1", "2"]:
        print("Invalid choice!")
        return

    name = input("Name: ").strip()
    email = input("Email: ").strip()
    password = input("Password: ")

    if not name or not email or not password or campus.find_user(email):
        print("Invalid details or email already exists!")
        return

    uid = f"USR{len(campus.view_users()) + 1:03d}"
    user = Student(uid, name, email, password) if role == "1" else Organizer(uid, name, email, password)
    campus.add_user(user)
    print("Account created successfully!")


def student_menu(user):
    while True:
        user.display_dashboard()
        choice = input("Choice: ")

        if choice == "1":
            for event in campus.view_events():
                event.display_event()
        elif choice == "2":
            campus.register_student(user, input("Event ID: "))
        elif choice == "3":
            campus.cancel_registration(user, input("Event ID: "))
        elif choice == "4":
            user.view_registrations()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")


def organizer_menu(user):
    while True:
        user.display_dashboard()
        choice = input("Choice: ")

        if choice == "1":
            name = input("Event name: ")
            category = input("Category: ")
            date = input("Date: ")
            venue = input("Venue: ")
            desc = input("Description: ")

            try:
                capacity = int(input("Capacity: "))
                if capacity <= 0 or not all([name, category, date, venue, desc]):
                    raise ValueError

                eid = f"EVT{len(campus.view_events()) + 1:03d}"
                event = Event(eid, name, category, date, venue, desc, capacity)
                user.create_event(event)
                campus.add_event(event)

            except ValueError:
                print("Invalid event details or capacity!")

        elif choice == "2":
            user.view_created_events()

        elif choice == "3":
            event = campus.find_event(input("Event ID: "))
            if event and event in user.get_created_events():
                user.update_event(event, input("New name: ") or None,
                                  input("New date: ") or None,
                                  input("New venue: ") or None)
            else:
                print("Event not found!")

        elif choice == "4":
            event = campus.find_event(input("Event ID: "))
            if event and user.delete_event(event):
                campus.remove_event(event)

        elif choice == "5":
            for event in user.get_created_events():
                print(f"\n{event.name}:")
                for student in event.registered_students:
                    print(student.name)

        elif choice == "6":
            break
        else:
            print("Invalid choice!")


def admin_menu(user):
    while True:
        user.display_dashboard()
        choice = input("Choice: ")

        if choice == "1":
            user.view_all_users(campus.view_users())
        elif choice == "2":
            user.view_all_events(campus.view_events())
        elif choice == "3":
            campus.display_statistics()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")


def login():
    email = input("Email: ").strip()
    user = campus.find_user(email)

    if user and user.check_password(input("Password: ")):
        print(f"\nWelcome, {user.name}!")

        if isinstance(user, Student):
            student_menu(user)
        elif isinstance(user, Organizer):
            organizer_menu(user)
        elif isinstance(user, Admin):
            admin_menu(user)
    else:
        print("Invalid login details!")


def main():
    while True:
        print("\n========== CAMPUSCONNECT ==========")
        print("1. Login (Student / Organizer / Admin)")
        print("2. Register Account")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            print("Thank you for using CampusConnect!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()



