Introduction
This project was developed to build and track gym workouts anywhere. It addresses the need to create a gym workout through a web app, which can then be accessed anywhere. The idea originated from my first graduation in Physical Education, when I remembered that most gyms in my area still use paper cards to schedule workouts. The result is an application that can create workouts online and be used in any gym.

Distinctiveness and Complexity
Distinctiveness
This project is unique because it offers the ability to create and manage a new workout for every single day of the week. Unlike traditional workout tracking methods, which typically offer static routines, this web app allows users to customize their workout plans on a daily basis. The app supports dynamic workout combinations, allowing users to view their training plan for any specific day of the week, enhancing flexibility and personalization. This approach is different from other workout apps because it’s tailored to the specific needs of each user, based on the day-to-day progress of their physical training.

Complexity
The complexity of this project lies in the following aspects:
The home_view and myTraining_view dynamically filter workout details based on the current day of the week or user input. This involves querying the database for user-specific workouts, extracting distinct muscle groups and exercises, and rendering them dynamically. The logic ensures accurate data retrieval while maintaining performance.
Retrieving and filtering workout details efficiently for each user and day of the week posed performance challenges, especially with large datasets. To address this, the setWorkout_view includes logic to validate and avoid duplicate workout entries. When a user attempts to create or update a workout, the application checks if a WorkoutDetail already exists for the specified user, day of the week, and exercise. This logic ensures data consistency and avoids redundant entries.
By using foreign key relationships, the application dynamically renders muscle groups and exercises based on the logged-in user's workout plan. This dynamic filtering and rendering streamline the user experience, making the interface intuitive.
The Exercise model includes a youtube_embed field, allowing admins add YouTube videos for each exercise to explain how to do each one correcty to the users. This integration provides visual guidance, enhancing the educational value of the application.
This project demonstrates expertise in managing complex relationships between users, muscle groups, exercises, and workout details, while prioritizing ease of use and interactivity. Features like dynamic day-based filtering and intuitive error handling showcase these elements.
These technical challenges required a strong understanding of code optimization, database design, and seamless integration of external resources.

Project Structure
The project structure is organized as follows:
models.py: Defines the tables and logic for interacting with the database.
views.py: Contains the logic for each functionality of the app.
templates/: Contains HTML files for page rendering.
static/: Stores static CSS files.

How to Run the Application
Before running the application, make sure you have the following items installed:
Python 3.10.12 or later
Django 3.2.12 or later

Steps to Run
Start the server:
python3 manage.py runserver

Access the application in your browser at:
http://127.0.0.1:8000/

To test and input new exercises, access:
http://127.0.0.1:8000/admin

Login with:
Username: adm
Password: adm
