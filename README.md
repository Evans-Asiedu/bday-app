# CS50 WEB PROGRAMMING FINAL PROJECT: HEALTHCARE
#### video Demo: https://youtu.be/EoFyklnoAcI

### Description:
This Web application is called Healthcare. Users, both Doctors and patients can sign up to the application. Doctors are given the opportunity to make post about dieting and excercises which is beneficial to peoples health.
Patients on the other hand have the opportunity to view post made by doctors
and also book appointment with a Doctor if they want to.

### Features:
* Home Page: It displays list of postS that have been by doctors concerning exercises and dieting.<br />
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
  give information about a particular exercise or diet the user want to educate those on the system about. <br />
  <br />
* Book appointment Button: It allows a user to book an appointment with a Doctor on the platform.
  When the button is clicked, the User is given a form to select the date and type of procedure
  he or she wants to see the doctor for.
  <br/><br/>


### Distinctiveness and Complexity:
* The page is not similar to anything we have already created. It's not a social media app nor an e-commerce. It's not similar to other years projects either.
For the complexity, I used Django with more than one model (explained below) Moreover, the web application is responsive to different screen sizes both mobiles phones and computers


### Files Information:
views.py file contains all the backend code. The main functions are:
* login_view, logout_view, register
* index
* doctors, exercises, dieting
* bookappointment
* appointment
* create_post, favourite_post, like_post
* Class BookAppointmentForm
* Class CreatePostForm

Models.py The different models are
* CustomUser
* Post
* Like
* Appointment

Other files are:
* index.js contains function for handling like and unlike post as well as handling part of the sidebar functionality

* sidebar.css, styles.css for handling the css in this web application

* templates folder contains all the different html pages (8 html files including layout.html)

### Technologies Used:
The project is created using;
* Django framework - A web development environment. it follows the model-view-controller (MVC) pattern and provides tools, tmeplates and libraries to build dynamic application<br/>
* db.sqlite3 - is a default SQLite database file used by django for storing data.<br/>
* tempus_dominus - A datetime picker library for bootstrap for web development. It provides simply user interface for selecting date and time values in forms, enhancing user experience by facilitating date and time input through interactive calenders and time selectors <br/>

### How to run the application
* Install project dependencies by running pip install -r requirements.txt
* Make and apply migrations by running python manage.py makemigrations
  and python manage.py migrate
* create superuser with python manage.py createsuperuser. This step is optional
* Go to website address and register an account