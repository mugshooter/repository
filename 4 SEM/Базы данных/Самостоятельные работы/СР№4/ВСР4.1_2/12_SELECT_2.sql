INSERT INTO NewBook (BookID, Title, AuthorID, Genre, PublishDate)
SELECT BookID, Title, AuthorID, Genre, PublishDate
FROM Book
WHERE YEAR(PublishDate) > 2000;
