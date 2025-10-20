# Hostel Room Management System

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.room_no = None

    def display_info(self):
        print(f"Room {self.room_no} assigned to {self.name} [ID: {self.roll_no}] ")


class Room:
    def __init__(self, room_no, capacity):
        self.capacity = capacity
        self.is_available = True
        self.room_no = room_no
        self.student_name = None
    
    def assign_room(self, student_name):
        if self.is_available:
            self.is_available = False
            self.student_name = student_name
            print(f"Room {self.room_no} assigned to {student_name}")
        else:
            print(f"Room {self.room_no} is already occupied.")

    def vacate_room(self):
        if not self.is_available:
            print(f"Room {self.room_no} vacated by {self.student_name}")
            self.is_available = True
            self.student_name = None
        else:
            print(f"Room {self.room_no} is already empty.")

    def display_info(self):
        status = "Available" if self.is_available else f"Occupied by {self.student_name}"
        print(f"Room No: {self.room_no}, Capacity: {self.capacity}, Status: {status}")


class Hostel:
    def __init__(self):
        self.students = []    # list to store student objects
        self.rooms = []       # list to store room objects

        # adding some default rooms
        self.add_room(Room(101, 1))
        self.add_room(Room(102, 1))
        self.add_room(Room(103, 1))

    def add_student(self, student):
        room = self.find_available_room()
        if room:
            room.assign_room(student.name)
            student.room_no = room.room_no
            self.students.append(student)
        else:
            print("No available rooms right now.")

    def add_room(self, room):
        self.rooms.append(room)
        print(f"Room {room.room_no} added successfully!")

    def find_available_room(self):
        for room in self.rooms:
            if room.is_available:
                return room
        return None

    def show_all_students(self):
        if not self.students:
            print("No students found yet.")
        else:
            print("\n--- Student List ---")
            for s in self.students:
                s.display_info()

    def show_all_rooms(self):
        if not self.rooms:
            print("No rooms added yet.")
        else:
            print("\n--- Room List ---")
            for r in self.rooms:
                r.display_info()

    def vacate_room(self, room_no):
        for room in self.rooms:
            if room.room_no == room_no:
                room.vacate_room()
                return
        print("Invalid room number.")


# main program
obj1 = Hostel()

while True:
    print("\n--- Hostel Room Management System ---")
    print("1. Add Student")
    print("2. View All Rooms")
    print("3. View All Students")
    print("4. Vacate a Room")
    print("5. Add New Room")
    print("6. Exit")
     
    number = int(input("Enter choice: "))
    match number:
        case 1:
            name = input("Enter name of Student: ")
            roll_no = input("Enter ID of Student: ")
            obj = Student(name, roll_no)
            obj1.add_student(obj)
            
        case 2:
            obj1.show_all_rooms()

        case 3:
            obj1.show_all_students()
        
        case 4:
            room_no = int(input("Enter room number to vacate: "))
            obj1.vacate_room(room_no)

        case 5:
            room_no = int(input("Enter new room number: "))
            capacity = int(input("Enter room capacity: "))
            obj1.add_room(Room(room_no, capacity))
        
        case 6:
            print("Program Exit.")
            break
        
        case _:
            print("Invalid choice, try again!")
