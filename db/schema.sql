CREATE TABLE IF NOT EXISTS `user` (
    `id` INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `email` VARCHAR(200) NOT NULL,
    `password` VARCHAR(200) NOT NULL,
    `genre` VARCHAR(50) NOT NULL -- ('Horror', 'Science Fiction', 'Romance', 'Animation', 'Humor')
);

CREATE TABLE IF NOT EXISTS `movie` (
    `id` INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `title` VARCHAR(50) NOT NULL,
    `description` VARCHAR(200) NOT NULL,
    `date` DATE NOT NULL,
    `language` VARCHAR(10) NOT NULL,
    `genre` ENUM ('Horror', 'Science Fiction', 'Romance', 'Animation', 'Humor') NOT NULL,
    `trailer` VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS `liked_movie` (
    `id_user` INT NOT NULL,
    `id_movie` INT NOT NULL,
PRIMARY KEY(`id_user`, `id_movie`)
);

CREATE TABLE IF NOT EXISTS `seen_movie` (
    `id_user` INT NOT NULL,
    `id_movie` INT NOT NULL,
PRIMARY KEY(`id_user`, `id_movie`)
);

CREATE TABLE IF NOT EXISTS `playlist` (
    `id_user` INT NOT NULL,
    `id_playlist` INT AUTO_INCREMENT NOT NULL,
    `title` VARCHAR(255) NOT NULL,
PRIMARY KEY(`id_user`, `id_playlist`)
);

CREATE TABLE IF NOT EXISTS `playlist_videos` (
    `id_playlist` INT NOT NULL,
    `id_movie` INT NOT NULL,
PRIMARY KEY(`id_playlist`, `id_movie`)
);

INSERT INTO `movie` (`title`, `description`, `date`, `language`, `genre`, `trailer`)
    VALUES ('Sausage Party', "Une petite saucisse s'embraque dans une dangereuse quête pour découvrir les origines de son existence...", '2016-11-30', 'English', 'Humor', 'https://www.youtube.com/watch?v=WVAcTZKTgmc'),
    ('BLOP', "Une petite saucisse s'embraque dans une dangereuse quête pour découvrir les origines de son existence...", '2016-11-30', 'English', 'Humor', 'https://www.youtube.com/watch?v=WVAcTZKTgmc'),
    ('Inception', "Dom Cobb est un voleur expérimenté: sa spécialité consiste à s'approprier les secrets les plus précieux d'un individu pendant qu'il rêve.", '2010-07-21', 'English', 'Science Fiction', 'https://www.youtube.com/watch?v=YoHD9XEInc0');

INSERT INTO `user` (email, password, genre) VALUES
("test@gmail.com", "blop", "Humor");