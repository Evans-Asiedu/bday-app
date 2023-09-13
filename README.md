# CS50 WEB PROGRAMMING FINAL PROJECT: HEALTHCARE
#### video Demo: https://youtu.be/EoFyklnoAcI

### Description:
This Web application is called Healthcare. Users, both Doctors and Patients can sign up to the application. 
Doctors are given the opportunity to make post about dieting and exercises which is beneficial to peoples health.
Patients on the other hand have the opportunity to view post made by doctors
and also book appointment with a Doctor if they want to.

### Features:
* Home Page: It displays list of posts that have been by doctors concerning exercises and dieting.<br />
  <br/>

* Login/Logout/Register: It allows the user to register, login if registered and logout when needed
  <br />
  <br/>
* SideBar: It contains items such All, Doctors, Exercises and Dieting that are links to different pages
  <br /><br />
* Dropdown Menu Item: It contains items such username of the user, appointment, favourite post and logout.
  Appointment allows user to see list of appointment booked, favourite post allows user to see list of post
  that the user have liked and logout allow user to log out from the site. <br />
  <br />
* Make a Post Button: It allows Doctors registered on the system to create a post concerning dieting or exercise.
  Basically, when the make a post button is clicked, a form is presented to user that allows the user to
  give information about a particular exercise or diet that the user want to educate those on the system about. <br />
  <br />
* Book Appointment Button: It allows a user to book an appointment with a Doctor on the platform.
  When the button is clicked, the User is given a form to select the date and type of procedure
  he or she wants to see the doctor for.
  <br/><br/>


### Distinctiveness and Complexity:
* The healthcare web application is not similar to anything we've already created. It's not a social media app nor an e-commerce. 
It's not similar to other years projects either. It's distinctiveness lies in the objective of the application as stated under the
description, the main purpose of the app is to help Patients/Clients and Doctors connect in an easy way where Clients have
the opportunity to read health related post made by Doctors specifically on dieting and exercise. In addition, Clients have
the opportunity to book appointment with a Doctor knowing well the area of speciality of Doctors on the system.
For the complexity, Django is used to build the models and the views which deals with the backend. On the frontend, javascript
file is used to make the web application more interactive like toggling the sidebar and allowing users to like or unlike a post.
Also, custom css and bootstrap css are used to make the template responsive to different screen sizes. The templates
and views in conjunction with codes in other files are carefully written to create a project which is unique and easy to use.


### Folder and Files Information:
views.py file contains all the backend code. The main functions are:
* login_view: It handles the user login
* logout_view: It handles the user logout
* register: It handles the registering of new users unto the system
* index: It retrieves all post information made by Doctors
* doctors: It retrieves information of list of Doctors that have been stored
* exercises: It retrieves information about post specifically on exercise 
* dieting: It retrieves information about posts specifically on dieting
* bookappointment: It handles user booking doctor's appointment
* appointment: It retrieves list of appointment booked by the user
* create_post: It handles the creating of new post
* favourite_post: it retrieves list of posts tagged by user as favourite
* like_post: It handles the liking or unliking of a post
* Class BookAppointmentForm: It helps to create the book appointment form
* Class CreatePostForm: It helps to create the make a post form

Models.py file contain the models. The different models are
* CustomUser: It inherits django default user model and add extra information about user such as image, about, is_doctor
* Post: It contains information about post such as title, image, content, category and publication date
* Like: It helps to track which post has been liked by a user. Thus, it contains information such as user, post
* Appointment: It helps to track doctor's appointment booked by a client. Thus, it contains information such as 
client, doctor, category and appointment_date

Templates folder: contains the following HTML templates
* appointmentform.html: HTML template for displaying form for booking Doctor's appointment
* appointments.html: HTML template for displaying list of appointment booked by user
* create_post.html: HTML template for displaying form that allows Doctors to create post about dieting or exercise
* doctors.html: HTML template for displaying list of Doctors registered on the system
* index.html: HTML template for display the home page which shows list of posts made by doctors
* layout.html: HTML template which lay out the structure view of the system which also inherited by other templates
* login.html: HTML template for displaying the login page to allow users to log in.
* register.html: HTML template for displaying the register page to allow new user to sign up to the system

Static folder: contains front end (css/js) files as listed below
* index.js for toggling the sidebar view and also contains function for handling like and unlike post
* Css files (sidebar.css, styles.css) illustrate the techniques that are used in the designing of various 
templates such card and buttons, besides using bootstrap for responsive design.

Migrations: for saving sql data

### Technologies Used:
The project is created using;
* Django framework - A web development environment. it follows the model-view-controller (MVC) pattern and provides tools, tmeplates and libraries to build dynamic application<br/>
* db.sqlite3 - Is a default SQLite database file used by django for storing data.<br/>
* tempus_dominus - A datetime picker library for bootstrap for web development. It provides simply user interface for selecting date and time values in forms, enhancing user experience by facilitating date and time input through interactive calenders and time selectors <br/>

### How to run the application
* Install project dependencies by running pip install -r requirements.txt
* Make and apply migrations by running python manage.py makemigrations
  and python manage.py migrate
* create superuser with python manage.py createsuperuser. This step is optional
* Go to website address and register an account