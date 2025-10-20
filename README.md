# Hostel_room_management

Project Overview
This project is a small console-based program made in Python using Object-Oriented Programming (OOP). It helps to manage hostel rooms and student allocations. Students can be added, rooms can be viewed, and vacant rooms can be assigned automatically. No database is used — all data is stored in lists temporarily while the program runs.

Main Features
	1	Add new student
	2	Automatically assign available room
	3	View all students
	4	View all rooms (with current status)
	5	Vacate a room
	6	Add new room

Classes Used
1. Student Class
	•	Attributes: name, roll_no, room_no
	•	Method: display_info() to show student details
2. Room Class
	•	Attributes: room_no, capacity, is_available, student_name
	•	Methods:
	◦	assign_room() – to assign a student
	◦	vacate_room() – to empty the room
	◦	display_info() – to show room details
3. Hostel Class
	•	Attributes: students, rooms (both stored in lists)
	•	Methods:
	◦	add_student()
	◦	add_room()
	◦	find_available_room()
	◦	show_all_students()
	◦	show_all_rooms()
	◦	vacate_room()

OOP Concepts Used
	•	Class and Object: Real-world entities like Student, Room, Hostel are made as classes.
	•	Encapsulation: Each class has its own data and functions.
	•	Composition: Hostel class uses both Room and Student objects.
	•	Abstraction: Only required details are shown to the user.

Conclusion
This project shows basic OOP concepts in a simple and clear way. It is easy to understand. It is a good example of using classes and objects for real-world management systems.
