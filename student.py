
from user import User


class Student(User):

    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.__registered_events = []

    def register_event(self, event):
        if event in self.__registered_events:
            print("You are already registered for this event!")
            return

        if event.register_student(self):
            self.__registered_events.append(event)
            print(f"Successfully registered for {event.name}!")
    
    def cancel_registration(self, event):
        if event in self.__registered_events:
            event.remove_student(self)
            self.__registered_events.remove(event)
            print(f"Registration cancelled for {event.name}.")
        else:
            print("You are not registered for this event.")

    def view_registrations(self):
        if not self.__registered_events:
            print("You have no registered events.")
            return

        print("\n--- MY REGISTERED EVENTS ---")
        for event in self.__registered_events:
            print(f"{event.name} | {event.date} | {event.venue}")

    def display_dashboard(self):
        print(f"\nWELCOME, {self.name.upper()}!")
        print("\n========== STUDENT DASHBOARD ==========")
        print("1. View Events")
        print("2. Register for Event")
        print("3. Cancel Registration")
        print("4. My Registrations")
        print("5. Logout")
