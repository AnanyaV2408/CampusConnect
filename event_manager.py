
class EventManager:

    def __init__(self):
        self.__users = []
        self.__events = []

    # User management

    def add_user(self, user):
        self.__users.append(user)

    def find_user(self, email):
        for user in self.__users:
            if user.email == email:
                return user
        return None

    def view_users(self):
        return self.__users.copy()

    # Event management

    def add_event(self, event):
        self.__events.append(event)

    def find_event(self, event_id):
        for event in self.__events:
            if event.event_id == event_id:
                return event
        return None

    def remove_event(self, event):
        if event in self.__events:
            self.__events.remove(event)
            return True
        return False

    def view_events(self):
        return self.__events.copy()

    # Registration management

    def register_student(self, student, event_id):
        event = self.find_event(event_id)

        if event is None:
            print("Event not found!")
            return

        student.register_event(event)

    def cancel_registration(self, student, event_id):
        event = self.find_event(event_id)

        if event is None:
            print("Event not found!")
            return

        student.cancel_registration(event)

    # Statistics

    def display_statistics(self):
        print("\n========== CAMPUS STATISTICS ==========")
        print(f"Total Users: {len(self.__users)}")
        print(f"Total Events: {len(self.__events)}")

        total_registrations = sum(
            len(event.registered_students)
            for event in self.__events
        )

        print(f"Total Registrations: {total_registrations}")
        print("=======================================")
