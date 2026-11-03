
class Event:

    def __init__(self, event_id, name, category, date, venue,
                 description, capacity):

        self.__event_id = event_id
        self.__name = name
        self.__category = category
        self.__date = date
        self.__venue = venue
        self.__description = description
        self.__capacity = capacity
        self.__registered_students = []

    # Getters

    @property
    def event_id(self):
        return self.__event_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def category(self):
        return self.__category

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def venue(self):
        return self.__venue

    @venue.setter
    def venue(self, value):
        self.__venue = value

    @property
    def description(self):
        return self.__description

    @property
    def capacity(self):
        return self.__capacity

    @property
    def registered_students(self):
        return self.__registered_students.copy()

    # Registration methods

    def register_student(self, student):

        if student in self.__registered_students:
            print("Already registered!")
            return False

        if len(self.__registered_students) >= self.__capacity:
            print("Sorry! Event is full.")
            return False

        self.__registered_students.append(student)
        return True

    def remove_student(self, student):

        if student in self.__registered_students:
            self.__registered_students.remove(student)
            return True

        return False

    def display_event(self):

        print("\n------------------------------")
        print(f"Event ID: {self.__event_id}")
        print(f"Name: {self.__name}")
        print(f"Category: {self.__category}")
        print(f"Date: {self.__date}")
        print(f"Venue: {self.__venue}")
        print(f"Description: {self.__description}")
        print(f"Capacity: {len(self.__registered_students)}/{self.__capacity}")
        print("------------------------------")
 