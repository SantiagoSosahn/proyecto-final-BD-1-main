-- DROP TABLE IF EXISTS TicTacToe
CREATE DATABASE TicTacToe;
USE TicTacToe;

CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    var_name VARCHAR(30) NOT NULL,
    var_userName VARCHAR (20),
    char_email CHAR(30) NOT NULL,
    char_password CHAR(20) NOT NULL,
    bit_admin BIT DEFAULT 0 NOT NULL,
    id_binnacle_fk INT,

    FOREIGN KEY (id_binnacle_fk) REFERENCES Binnacle(id) 
);

CREATE TABLE Score(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_game_fk INT NOT NULL,

    FOREIGN KEY (id_game_fk) REFERENCES Game(id)
);

CREATE TABLE Game(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dat_date DATE NOT NULL,
    tim_time TIME NOT NULL,
    last_movement TIMESTAMP NOT NULL, 
    bit_win BIT DEFAULT 0 NOT NULL,
    bit_gameOver BIT DEFAULT 0 NOT NULL,
    bit_pause BIT DEFAULT 0 NOT NULL
);

CREATE TABLE Binnacle(
    id INT PRIMARY KEY AUTOINCREMENT,
    dat_date DATE NOT NULL,
    tim_time TIME NOT NULL,
    id_activity_fk INT,

    FOREIGN KEY (id_activity_fk) REFERENCES Activity(id),
);

CREATE TABLE Activity(
    id INT PRIMARY KEY AUTOINCREMENT,
    tex_description TEXT
);