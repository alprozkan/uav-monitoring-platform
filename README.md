# UAV Monitoring Platform

This repository contains the code for the UAV Monitoring Platform, which allows users to manage drone tasks and retrieve images captured during task execution.

## Setup Instructions

### Backend

1. **Navigate to the Backend Directory**:

  
   cd uav-monitoring-backend
 

Create and Activate Virtual Environment:
python -m venv venv
venv\Scripts\activate

Install Dependencies:


pip install -r requirements.txt

Set Up the Database:

    Update config.py with your actual database credentials.

    Initialize the database:

    

    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade

Seed the Database:



python seed.py

Run the Flask Application:



    flask run

Frontend

    Navigate to the Frontend Directory:

    

cd uav-monitoring-frontend

Install Dependencies:



npm install

Run the Vue.js Application:



    npm run serve

Notes

    Remember to update config.py with your actual database username and password.

