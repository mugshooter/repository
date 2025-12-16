CREATE TABLE BookInLib (
    LibraryID INT,
    BookID INT,
    StatusID INT,
    CONSTRAINT pk_LibraryBook PRIMARY KEY (LibraryID, BookID),
    FOREIGN KEY (LibraryID) REFERENCES Library(LibraryID),
    FOREIGN KEY (BookID) REFERENCES Book(BookID),
    FOREIGN KEY (StatusID) REFERENCES BookStatus(StatusID)
);
