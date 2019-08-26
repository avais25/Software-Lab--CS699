To run the script use the command :-

bash masterscript.sh 

this script will start the server and start the homepage of the website inn firefox after 3 secons so that the server is properly started.

If firefox does not start use url after the server start:-

 127.0.0.1:8000/homepage/

*Run with internet connection to properly load images and fonts.



One of  Saved userid and password to directly login:-
usename: avais
password:qwertyuiop

Description of website:-
It is a Movie Ticket booking website named (watchIt!).
In the first page we get two option to 1. Login , 2. Register

Register:- If we choose register it will ask for username and password . It checks if username already exist or not and shows proper error or success messege. 

Login:- If we choose to login we have to enter username and password. If shows proper error messege for all invalid entries. After successful login it redirects to Booking page.

Booking:- It shows username of the logged in user at the top. It cantains name of several movies of which we can buy ticket. We have to enter number of tickets we want to buy and press Book Now button.
For security reasons a person cannot  directly open 127.0.0.1:8000/homepage/loginhome/ to reach page. He have to login first.

**THIS PAGE IS COMPLELY DYNAMIC AND NOT HARDCODED**

Once detail of a movie and its image url is added to Movies tables in database through http://127.0.0.1:8000/admin/ , it automatically show up in this page.

Booking Status:- If there is insufficient number of seats it will display proper error messege(booking is atomic , it will not partially book tickets). Else, it will show the total price with success messege. 
It will also update the database accordingly.

Logout:- It will properly logout the user  from the website.

If we try to access Booking page without logging in we will be redirected to Home page.



Template used:-
- I have used the CSS file from internet and completely edited it according to my need.

Descriptiopn of directory structure and its utility:-
The name of project is mysite.
The project use a single app named homepage.
All the  template use a single css file which is in the static folder.
The template folder contains all the html file used in website.
The database contain two tables , one for storing Details of movies and other for user information.
views.py contains the logic behind execution of website.


