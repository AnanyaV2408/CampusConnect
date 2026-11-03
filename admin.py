
from user import User


class Admin(User):

    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)

    def view_all_users(self, users):
        print("\n--- ALL REGISTERED USERS ---")

        if not users:
            print("No users found.")
            return

        for user in users:
            print(f"{user.user_id} | {user.name} | {user.email} | {type(user).__name__}")

    def view_all_events(self, events):
        print("\n--- ALL CAMPUS EVENTS ---")

        if not events:
            print("No events available.")
            return

        for event in events:
            print(f"{event.event_id} | {event.name} | {event.date}")

    def display_dashboard(self):
        print(f"\nWELCOME, ADMIN {self.name.upper()}!")
        print("\n========== ADMIN DASHBOARD ==========")
        print("1. View All Users")
        print("2. View All Events")
        print("3. View System Statistics")
        print("4. Logout")
