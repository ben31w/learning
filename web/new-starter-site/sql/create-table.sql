CREATE TABLE FormSubmissions(
	submission_id INT NOT NULL AUTO_INCREMENT,
	fname VARCHAR(20),
    lname VARCHAR(20),
    message VARCHAR(1000),
    found_through VARCHAR(10), # might change to enum/restrictive values.
    
    PRIMARY KEY(submission_id)
);