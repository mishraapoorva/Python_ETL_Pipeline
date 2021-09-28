# Python_ETL_Pipeline

## Overview

You will be reading CSV files found in the input_files directory and loading the contents into a SQLite database.

## The Goal

The goal of the project is for each table to contain valid records from each CSV file at the end of the program, with rejection or cleanup actions recorded in the table "data_record_status" (read on). When you first run the project, you should see the console log an empty DataFrame for each table, representing the state of the SQLite database before the files are ingested. Once you finish, they should be populated with records from the CSV input files.

Using pandas, you will be reading each CSV file and validating the records, either rejecting them to be loaded into the database or sanitizing/normalizing the values. Afterwards, load the data into its respective table. You can view the schema diagram in "Database Schema.png".

If this seems like a straightforward challenge to you, or if you finish early, please show off! Show us what you would do to track changes, manage errors, anything you would do if you were owning this code for yourself. 

We're a small team; you would be the third developer. Our organization, both by our values and by necessity, puts a high onus on our engineers to own their own quality and best practices. We hope to see those values reflected in your code: we are looking for clean, easy-to-read, well organized code, with strong test coverage.

## The data_record_status table

Each rejection or value transformation should be recorded in the "data_record_status" table.

Each record should have a simple "action" describing the error, such as "REJECTED - NOT UNIQUE", "FIXED - WHITESPACE", "REJECTED - NOT A NUMBER", "REJECTED - INVALID DATE" etc. For simplicity, a formal type enum was not established.

Also, a more complete "description" about the record in question should be recorded, which should include info such as the relevant **input file**, the **row number** where an issue was found, and any relevant info about an invalid or normalized **value** if possible. This was left as a freeform string for simplicity as well.

## Notes

You can read more info about each file's columns and needed validation in "Input File Documentation.md".
