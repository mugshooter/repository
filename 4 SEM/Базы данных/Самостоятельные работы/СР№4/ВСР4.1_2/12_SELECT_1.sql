CREATE TABLE NewBook (
    BookID INT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    AuthorID INT NOT NULL,
    Genre VARCHAR(100),
    PublishDate DATE
);
