
from user import User


class Organizer(User):

    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.__created_events = []

    def create_event(self, event):
        self.__created_events.append(event)
        print(f"Event '{event.name}' created successfully!")

    def view_created_events(self):
        if not self.__created_events:
            print("You haven't created any events yet.")
            return

        print("\n--- MY EVENTS ---")
        for event in self.__created_events:
            print(f"{event.event_id} | {event.name} | {event.date}")

    def update_event(self, event, name=None, date=None, venue=None):
        if event not in self.__created_events:
            print("You can only update your own events.")
            return

        if name:
            event.name = name
        if date:
            event.date = date
        if venue:
            event.venue = venue

        print("Event updated successfully!")

    def delete_event(self, event):
        if event not in self.__created_events:
            print("You can only delete your own events.")
            return False

        self.__created_events.remove(event)
        print(f"Event '{event.name}' deleted successfully!")
        return True

    def display_dashboard(self):
        print(f"\nWELCOME, ORGANIZER {self.name.upper()}!")
        print("\n========== ORGANIZER DASHBOARD ==========")
        print("1. Create Event")
        print("2. View My Events")
        print("3. Update Event")
        print("4. Delete Event")
        print("5. View Registrations")
        print("6. Logout")

    def get_created_events(self):
        return self.__created_events.copy()