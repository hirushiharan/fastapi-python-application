CREATE TABLE [User] (
    user_id INT IDENTITY(1,1) PRIMARY KEY,
    role_id INT FOREIGN KEY REFERENCES Lookup(lookup_id), 
    email VARCHAR(255) UNIQUE, 
    first_name VARCHAR(255), 
    last_name VARCHAR(255), 
    user_image VARCHAR(255),
    hashed_password VARCHAR(255), 
    is_temp_password BIT, 
    is_active BIT, 
    created_by VARCHAR(255), 
    created_on DATETIME, 
    updated_by VARCHAR(255), 
    updated_on DATETIME
);


INSERT INTO [User] (
    role_id, 
    email, 
    first_name, 
    last_name, 
    user_image, 
    hashed_password, 
    is_temp_password, 
    is_active, 
    created_by, 
    created_on, 
    updated_by, 
    updated_on
) VALUES (
    (SELECT lookup_id FROM Lookup WHERE category = 'UserRole' AND display_value = 'Admin'),
    'admin@example.com',
    'Admin',
    'User',
    NULL,
    '$2b$12$g7Y.yQIULLh5i4lPFh6Nr.8SCDah7yHTBhfcrbz/1kOeHfqEKsyHO',
    0,
    1,
    'system',
    GETDATE(),
    'system',
    GETDATE()
);

SELECT * FROM [User];
