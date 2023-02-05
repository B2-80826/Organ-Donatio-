# Organ-Donation-
Organdonation: A web-based platform for connecting organ donors &amp; recipients. Built with Flask, MySQL, pymysql, CSS, &amp; HTML. Users can register as donors, add organs, &amp; search for available organs. Improving the organ donation process &amp; saving lives
 


#Introduction
This project aims to create a platform for connecting organ donors with recipients. The backend is built using Flask and the database is managed using MySQL. The connection between Flask and MySQL is established using pymysql. The frontend is designed using CSS and HTML.

# Getting Started
Clone the repository to your local machine.
Set up a virtual environment using python3 -m venv venv and activate it using source venv/bin/activate.
Install the required packages using pip install -r requirements.txt.
Set up the database by running the SQL script provided in the repository.
Run the application using python app.py.
Visit http://localhost:5000 to view the application in the browser.

# Database Setup

Create the database and tables using the following SQL commands:

i)CREATE DATABASE organdonation;

II)CREATE TABLE user (
  id INT,
  name VARCHAR(255),
  email VARCHAR(255),
  password VARCHAR(255)
);

III)CREATE TABLE donor_info (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  age INT,
  email VARCHAR(255),
  mobile_number VARCHAR(15),
  blood_group VARCHAR(10),
  address VARCHAR(255),
  gender ENUM('male', 'female', 'other'),
  organs_donated SET('Pancreas', 'Corneas', 'Kidneys', 'Heart', 'Lungs', 'Liver')
);

# Tools and Technologies

1.The project was built using PyCharm and MySQL Workbench.

2.PyMySQL was used as the Object Relational Mapping (ORM) tool.


# Features
User registration and login.
Ability to list available organs for donation.
Ability to register as a donor and add organs for donation.
Ability to search for available organs based on various criteria.
Secure handling of sensitive information.


# Contributions
If you're interested in contributing to the project, please take a look at the contribution guidelines. We welcome any bug fixes, enhancements, or new features.

# License
This project is released under the MIT License.

# Acknowledgments
Flask documentation: flask.palletsprojects.com
PyMySQL documentation: pymysql.readthedocs.io
