# All Files
## "sourcedId"
* The "sourcedId" column in each CSV file corresponds to a "sourced_id" column in each database table. This simply represents the ID of the record in its raw state. 
* For example, a record in users.csv will have a value for column "orgSourcedId" that corresponds to the "sourcedId" of the file orgs.csv.
* The sourcedId value should be unique in each file, so records with non-unique sourcedIds are not valid.
* The sourcedId value should not be empty or null for any record.
## General cleanup/validation to look out for
* Look out for general issues with each column. Some columns may have a general pattern of an obvious mistake, such as extra literal quotes around values. Some values may need basic sanitation such as whitespace cleanup.

# academic_sessions.csv
## Required fields
The following records will be ingested into the database table "academic_sessions".
* sourcedId -> academic_sessions.sourced_id: The raw ID of the record
* title -> academic_sessions.name: The name of the record
* startDate -> academic_sessions.start_date: The starting date of the session
* endDate -> academic_sessions.end_date: The end date of the session
## Validation
* The sourcedId should not be empty (reject these records)
* The sourcedId should be unique (reject non-unique records)
* The start date should occur before the end date (reject these records)
* Normalize the start and end dates to format YYYY-MM-DD before ingesting to the database, and record that this action was taken in table data_record_status. Record instances of date normalization in data_record_status. Un-parsable dates should be rejected.

# orgs.csv
## Required fields
The following records will be ingested into the database table "orgs".
* sourcedId -> orgs.sourced_id: The raw ID of the record
* name -> orgs.name: The name of the record
## Validation
* The sourcedId should not be empty (reject these records)
* The sourcedId should be unique (reject non-unique records)

# users.csv
## Required fields
The following records will be ingested into the database table "users".
* sourcedId -> users.sourced_id: The raw ID of the record
* role -> users.role_name: A description of the user's role
* givenName -> users.first_name: First name
* familyName -> users.last_name: Last name
* email -> users.email_address: An email address
* orgSourcedId -> FK: References orgs.sourced_id. Use to get orgs.id
## Validation
* The sourcedId should not be empty (reject these records)
* The sourcedId should be unique (reject non-unique records)
* The email should be unique (reject non-unique records)
* The email should match an email pattern (reject invalid records)
* The orgSourcedId must reference a valid org (reject bad references)

# courses.csv
## Required fields
The following records will be ingested into the database table "courses".
* sourcedId -> courses.sourced_id: The raw ID of the record
* title -> courses.name: The name of the record
* courseCode -> courses.course_code: An internal course identifier
* courseCredit -> courses.course_credit: The number of credits offered of the course (decimal)
* orgSourcedId -> FK: References orgs.sourced_id. Use to get orgs.id
## Validation
* The sourcedId should not be empty (reject these records)
* The sourcedId should be unique (reject non-unique records)
* Course credit must be a decimal (clean up values to numbers if possible and reject others)
* orgSourcedId must reference an org (reject bad references)

# classes.csv
## Required fields
The following records will be ingested into the database table "classes".
* sourcedId -> classes.sourced_id: The raw ID of the record
* title -> classes.name: The name of the record
* classCode -> classes.class_code: An internal class identifier
* courseSourcedId -> FK: References courses.sourced_id. Use to get courses.id
* schoolSourcedId -> FK: References orgs.sourced_id. Use to get orgs.id
* termSourcedId -> FK: References academic_sessions.sourced_id. Use to get academic_sessions.id
