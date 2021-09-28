PRAGMA foreign_keys = ON;

CREATE TABLE orgs (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	sourced_id varchar(256) NOT NULL,
	name varchar(30) NOT NULL
);

CREATE TABLE academic_sessions (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	sourced_id varchar(256) NOT NULL,
	name varchar(30) NOT NULL,
	start_date DATE NOT NULL,
	end_date DATE NOT NULL
);

CREATE TABLE users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	sourced_id varchar(256) NOT NULL,
	role_name varchar(30) NOT NULL,
	first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	email_address varchar(320) NOT NULL,
    org_id integer NOT NULL,
	CONSTRAINT fk_org_id
		FOREIGN KEY(org_id)
		REFERENCES orgs(id),
	CONSTRAINT sourced_id_org_id_unique
		UNIQUE(sourced_id, org_id)
);

CREATE TABLE courses (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	sourced_id varchar(256) NOT NULL,
	name varchar(30) NOT NULL,
	course_code varchar(128) NOT NULL,
	course_credit DECIMAL NOT NULL,
	org_id integer NOT NULL,
	CONSTRAINT fk_org_id
		FOREIGN KEY(org_id)
		REFERENCES orgs(id),
	CONSTRAINT sourced_id_org_id_unique
		UNIQUE(sourced_id, org_id)
);

CREATE TABLE classes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    sourced_id varchar(256) NOT NULL,
	name varchar(30) NOT NULL,
    class_code varchar(30) NOT NULL,
	course_id integer NOT NULL,
	org_id integer NOT NULL,
	academic_session_id integer NOT NULL,
	CONSTRAINT fk_org_id
		FOREIGN KEY(org_id)
		REFERENCES orgs(id),
    CONSTRAINT fk_course_id
		FOREIGN KEY(course_id)
		REFERENCES courses(id),
	CONSTRAINT fk_academic_session_id
		FOREIGN KEY(academic_session_id)
		REFERENCES academic_sessions(id),
    CONSTRAINT sourced_id_org_id_unique
        UNIQUE(sourced_id, org_id)
);

CREATE TABLE data_record_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action varchar(30) NOT NULL,
    description varchar(256) NOT NULL
);