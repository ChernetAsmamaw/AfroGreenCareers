# AfroGreenCareers

## Overview

- AfroGreenCareers is a web platform that will provide access to internships and job listings in the sustainability and wildlife conservation fields for the African youth. It will support job creation, wildlife conservation, and regional integration, with the ultimate goal of creating better socio-economic opportunities for the people of Africa. This project is aligned with the corporate goal of promoting sustainable development in Africa and supports the business strategy of creating socio-economic impact through technology and innovation.



## Technologies Used

- AfroGreenCareers is built using `Django`, a high-level Python web framework known for its scalability and robustness. The project also utilizes `HTML`  and `Bootstrap` for front-end development, and incorporates a relational database management system `SQLite3` to handle data storage efficiently. The project is hosted on `varcel` and the source code is stored on `GitHub`.


## Features

AfroGreenCareers has the following features currently implemented:
- **Landing Page**: Users can view listings on the platform and filter th opportunities based on prefrence, however, inorder to apply to any of these opportunities one has to create an account.
- **User Authentication**: In order to access the full functionality of the platform, users must create an account. This is done by providing a username, email, and password. Users can also log in and log out of their accounts.
The registration also has the option of registering as an applicant or a recruiter. Based on the type of account created, the user will have access to different features of the platform.
- **Applicant Features**: Applicants can view all the opportunities on the platform,they can filter based on prefrence and apply to them. They can view the applications they made. They can also update their profile information on their Resume page.
- **Recruiter Features**: Recruiters can post opportunities on the platform. They can view the applications they received for the opportunities they posted. They can update the content of the opportunities they posted. They can also update their profile information on their Company page.
- **Admin Features**: The admin has access to all the features of the platform. They can view all the opportunities on the platform, they can filter based on prefrence and apply to them. They can view the applications they made. They can also update their profile information on their Resume page. They can post opportunities on the platform. They can view the applications they received for the opportunities they posted. They can update the content of the opportunities they posted. They can also update their profile information on their Company page. They can also view all the users on the platform and update their information.


## Installation Guide

To be able to run this project on your local machine, you need to have the following installed on your machine:
- First, you need to get the source code on your local machine. To do this, you can either download the zip file or clone the repository using the following command in your terminal:
    -````git clone https://github.com/ChernetAsmamaw/AfroGreenCareers```
- Then, you need to create a virtual environment and install the dependencies in the requirements.txt file. To do this, run the following commands in your terminal:
    - ```python3 -m venv venv```
    - ```source venv/bin/activate```
    - ```pip install -r requirements.txt```
- Then, you need to create a .env file in the root directory of the project and add the following environment variables:
    - ```SECRET_KEY```
    - ```EMAIL_HOST_USER```
    - ```EMAIL_HOST_PASSWORD```
    - ```DATABASE_URL```
- Then, you need to run the following commands in your terminal to create the database and run the migrations:
    - ```python manage.py makemigrations```
    - ```python manage.py migrate```
- Then, you need to create a superuser to be able to access the admin page. To do this, run the following command in your terminal:
    - ```python manage.py createsuperuser```
- Finally, you need to run the following command in your terminal to start the server:
    - ```python manage.py runserver```
