Description of the app:-


- I have made app for the Django website.
- This is a Movie Ticket booking app called "WatchIt.".
- User have to Register or Login to use the app.
- On start, user have two option 1. Login 2. Register
- If user Choose register:-
	-A registeration form will come up.
	-It checks weather that user name is alredy registered or not and give proper error messege
	-It checks weather "Password" and "confirm password" are same or not annd give proper error messege.
	-On proper registeration it redirect you to another page showing "Success" messege.
	-On pressing back button it will redirect you to home page.
-If user Choose to login:-
	-A login form will come up.
	-For incorrect credentials it will show error messege "Incorrect password" or "User not registered"
	-On Successful login it Redirect you to booking page.
	-There is a counter to show number of in inncorrect login attempts , login button gets deactivated once counter reach 0.
-Booking Page:-
	-It shows the name of movies and their details as stored in database.
	-This page is partially Hardcoded for now and there is no option to add more movie details to database for now.
	-Database gets populated on creation of app.
	-It shows number of seats available.
	-If we try to book more than available seats , it will show Error messege.
	-If we put any other value instead of Positive Numeric value , it will show error messege  and not book ticket.
	-On successful registeration it updates the database with the number of seats remaining.
	-It shows the total price to the ticket.
	-On pressing Back button it will redirect you to home page.

How to run :-
Install the watchit.apk file in the android phone.


Restriction:-
The app is made on Android 4.4 KitKat, may not work on lower android versions.
The app is tested on Nexus 5x device on android studio.

