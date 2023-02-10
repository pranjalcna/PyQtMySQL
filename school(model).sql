drop database school;
create database school;

use school;


-- Create the students table
CREATE TABLE students (
  student_id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL
);

-- Insert sample data into the students table
INSERT INTO students (first_name, last_name, email)
VALUES
  ('John', 'Doe', 'johndoe@example.com'),
  ('Jane', 'Doe', 'janedoe@example.com'),
  ('Jim', 'Smith', 'jimsmith@example.com');


-- Create the courses table
CREATE TABLE courses (
  course_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  description VARCHAR(200) NOT NULL
);

-- Insert sample data into the courses table
INSERT INTO courses (name, description)
VALUES
  ('Introduction to Database Management', 'Learn the basics of managing databases'),
  ('Advanced SQL', 'Learn to write complex SQL queries'),
  ('Data Visualization', 'Learn to create visual representations of data');


-- Create the enrollments table
CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Insert sample data into the enrollments table
INSERT INTO enrollments (student_id, course_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 3),
  (3, 1);

