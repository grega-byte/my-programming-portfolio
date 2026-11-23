# MySQL Relational Database Assignment

## 1. Project Name

MySQL Relational Database Assignment

## 2. Overview

This coursework project contains a MySQL database dump for a recruitment scenario, an entity relationship diagram, assignment PDFs, and stored-procedure exercises Q1–Q11.

## 3. Features

- Defines and populates tables for candidates, skills, hospitals, positions, and interviews.
- Includes stored procedures for looking up records, joining related tables, counting offers or positions, and querying interviews.
- Includes the ER diagram and PDF assignment materials supplied with the project.

## 4. Technologies Used

- MySQL 8.0 SQL dump (generated with MySQL 8.0.43)

## 5. Key Concepts Demonstrated

- Relational tables with primary and foreign keys
- Joins across related tables
- Stored procedures and input parameters
- Filtering, sorting, grouping, and aggregate queries

## 6. How to Run

Use a MySQL 8.0 compatible server. Create and select an empty database, then import `mysql_database_dump.sql`. The dump drops and recreates its tables, so use an empty database or back up existing data first. After importing the dump, execute the scripts in `COMP20240_Stored_Procedures/` against the same database to create the Q1–Q11 procedures.

## 7. Project Structure

- `mysql_database_dump.sql` — schema, sample data, and routines from the database dump.
- `COMP20240_Stored_Procedures/` — separate SQL scripts for procedures Q1–Q11.
- `ER_Diagram.pdf` — entity relationship diagram.
- `mysql_assignment_documentation.pdf` — submitted assignment PDF.
- `MySQLassignment20240-26-27.pdf` — assignment brief PDF.
