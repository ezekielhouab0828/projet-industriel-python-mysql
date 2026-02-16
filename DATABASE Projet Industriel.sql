CREATE DATABASE projet_industriel;
USE projet_industriel;

CREATE TABLE machines (
    id_machine INT PRIMARY KEY,
    type_machine VARCHAR(50),
    localisation VARCHAR(50)
);

CREATE TABLE mesures (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    id_machine INT,
    temperature FLOAT,
    vibration FLOAT,
    pression FLOAT,
    courant FLOAT,
    anom_temp BOOLEAN,
    anom_vib BOOLEAN,
    anom_press BOOLEAN,
    anom_courant BOOLEAN,
    FOREIGN KEY (id_machine) REFERENCES machines(id_machine)
);

INSERT INTO machines VALUES
(1, 'Compresseur', 'Zone A'),
(2, 'Pompe', 'Zone B'),
(3, 'Moteur électrique', 'Zone C'),
(4, 'Moteur électrique', 'Zone D');