# Intro-to-Python-Final-Project



Library Management System (Flask)
A web-based Library Management System built using Flask, SQLite, and Bootstrap.
The system allows librarians and administrators to manage books and users, while members can browse, borrow, and return books.
________________________________________
Features
Book Management
•	Add new books (title, author, publication year, language, ISBN)
•	Edit and delete book information
•	Automatically track book availability
•	Search books by title, author, language, and year
User Management
•	User registration and login
•	Role-based access:
o	Member
o	Librarian
o	Admin
•	Admin dashboard to create, edit, and delete users
 Loans (Check Out / Return)
•	Users can check out available books
•	Users can return borrowed books
•	Book availability updates automatically
•	Track active loans and loan history
 Loan History
•	Members can view their own loan history
•	Admins/Librarians can view system-wide loan history
 Authentication & Authorization
•	Secure login system
•	Role-based access control
•	Protected routes for admin and librarian actions
 User Interface
•	Clean and responsive UI using Bootstrap 5
•	Reusable base layout
•	Flash messages for feedback
•	Image support on homepage
________________________________________
 Technologies Used
•	Python 3
•	Flask
•	Flask-SQLAlchemy
•	Flask-Login
•	Flask-Migrate
•	SQLite
•	HTML / CSS
•	Bootstrap 5


Database Schema (Summary)
User
•	id
•	full_name
•	email
•	password_hash
•	role
•	created_at
Book
•	id
•	title
•	author
•	publication_year
•	language
•	isbn
•	is_available
Loan
•	id
•	user_id
•	book_id
•	checked_out_at
•	returned_at
