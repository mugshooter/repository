CREATE TABLE Элементы (
    ElementsID INT PRIMARY KEY AUTO_INCREMENT,
    ElemID INT NOT NULL,
    Comment TEXT,
    FOREIGN KEY (ElemID) REFERENCES Элемент(ElemID)
);
