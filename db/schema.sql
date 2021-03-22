CREATE TABLE IF NOT EXISTS `user` (
    `id` INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `email` VARCHAR(200) NOT NULL,
    `password` VARCHAR(200) NOT NULL,
    `genre` VARCHAR(50) DEFAULT 'NULL' -- ('Horror', 'Science Fiction', 'Romance', 'Animation', 'Humor')
);

CREATE TABLE IF NOT EXISTS `movie` (
    `id` INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `title` VARCHAR(50) NOT NULL,
    `description` VARCHAR(800) NOT NULL,
    `date` DATE NOT NULL,
    `language` VARCHAR(10) NOT NULL,
    `genre` ENUM ('Horror', 'Science Fiction', 'Romance', 'Animation', 'Humor') NOT NULL,
    `trailer` VARCHAR(100) NOT NULL,
    `rate` VARCHAR(4) NOT NULL,
    `during` VARCHAR(10) NOT NULL
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
);

INSERT INTO `movie` (`title`, `description`, `date`, `language`, `genre`, `trailer`, `rate`, `during`) VALUES
('Sausage Party', "Une petite saucisse s'embraque dans une dangereuse quête pour découvrir les origines de son existence...", '2016-11-30', 'English', 'Humor', 'https://www.youtube.com/watch?v=WVAcTZKTgmc', '6.6', '1H29MIN'),
('Inception', "Dom Cobb est un voleur expérimenté: sa spécialité consiste à s'approprier les secrets les plus précieux d'un individu pendant qu'il rêve.", '2010-07-21', 'English', 'Science Fiction', 'https://www.youtube.com/watch?v=YoHD9XEInc0&t=3s', '8.7', '2H28MIN'),
('Avengers End Game', "Thanos ayant anéanti la moitié de l’univers, les Avengers restants resserrent les rangs dans ce vingt-deuxième film des Studios Marvel, grande conclusion d’un des chapitres de l’Univers Cinématographique Marvel.", '2019-04-24', 'English', 'Science Fiction', 'https://www.youtube.com/watch?v=TcMBFSGVi1c', '8.4', '3H01MIN'),
('Deadpool 2', "L’insolent mercenaire de Marvel remet le masque! Plus grand, plus-mieux, et occasionnellement les fesses à l’air, il devra affronter un Super-Soldat dressé pour tuer, repenser l’amitié, la famille, et ce que signifie l’héroïsme – tout en bottant cinquante nuances de culs, car comme chacun sait, pour faire le Bien, il faut parfois se salir les doigts.", '2019-05-16', 'English', 'Humor', 'https://www.youtube.com/watch?v=WVAcTZKTgmc', '5.4', '2H00MIN'),
('Lion King', "Au fond de la savane africaine, tous les animaux célèbrent la naissance de Simba, leur futur roi. Les mois passent. Simba idolâtre son père, le roi Mufasa, qui prend à cœur de lui faire comprendre les enjeux de sa royale destinée. Mais tout le monde ne semble pas de cet avis. Scar, le frère de Mufasa, l'ancien héritier du trône, a ses propres plans. La bataille pour la prise de contrôle de la Terre des Lions est ravagée par la trahison, la tragédie et le drame, ce qui finit par entraîner l'exil de Simba. Avec l'aide de deux nouveaux amis, Timon et Pumbaa, le jeune lion va devoir trouver comment grandir et reprendre ce qui lui revient de droit…", '2019-07-17', 'English', 'Animation', 'https://www.youtube.com/watch?v=7TavVZMewpY', '4.1', '1H58MIN'),
('John Wick 3', "John Wick a transgressé une règle fondamentale : il a tué à l’intérieur même de l’Hôtel Continental. 'Excommunié', tous les services liés au Continental lui sont fermés et sa tête mise à prix. John se retrouve sans soutien, traqué par tous les plus dangereux tueurs du monde.", '2019-05-22', 'English', 'Horror', 'https://www.youtube.com/watch?v=pU8-7BX9uxs', '9.9', '2H12MIN'),
('Mission Impossible', "Les meilleures intentions finissent souvent par se retourner contre vous… Dans MISSION : IMPOSSIBLE – FALLOUT, Ethan Hunt accompagné de son équipe de l’IMF – Impossible Mission Force et de quelques fidèles alliées sont lancés dans une course contre la montre, suite au terrible échec d’une mission.", '2018-08-1', 'English', 'Romance', 'https://www.youtube.com/watch?v=wb49-oV0F78', '6.9', '2H28MIN'),
('Mad Max', "Hanté par un lourd passé, Mad Max estime que le meilleur moyen de survivre est de rester seul. Cependant, il se retrouve embarqué par une bande qui parcourt la Désolation à bord d'un véhicule militaire piloté par l'Imperator Furiosa. Ils fuient la Citadelle où sévit le terrible Immortan Joe qui s'est fait voler un objet irremplaçable. Enragé, ce Seigneur de guerre envoie ses hommes pour traquer les rebelles impitoyablement…", '2015-05-05', 'English', 'Horror', 'https://www.youtube.com/watch?v=hEJnMQG9ev8', '2.7', '2H00MIN'),
('A Star Is Born', "Star de country un peu oubliée, Jackson Maine découvre Ally, une jeune chanteuse très prometteuse. Tandis qu'ils tombent follement amoureux l'un de l'autre, Jack propulse Ally sur le devant de la scène et fait d'elle une artiste adulée par le public. Bientôt éclipsé par le succès de la jeune femme, il vit de plus en plus de mal son propre déclin…", '2018-10-03', 'English', 'Romance', 'https://www.youtube.com/watch?v=nSbzyEJ8X9E', '1.9', '2H16MIN'),
('Saw 6', "L'agent spécial Strahm est mort, et le détective Hoffman s'impose alors comme le légataire incontesté de l'héritage de Jigsaw. Cependant, tandis que le FBI se rapproche de plus en plus dangereusement de lui, Hoffman est obligé de commencer un nouveau jeu qui révélera enfin quel est le véritable grand dessein derrière les machinations de Jigsaw...", '2009-11-04', 'English', 'Horror', 'https://www.youtube.com/watch?v=XKxcf50t1xE', '7.0', '1H30MIN'),
('Là-Haut', "Des studios Disney-Pixar arrive la comédie d'aventure «Up», qui suit un vendeur de ballons de 78 ans, Carl Fredricksen, au moment où il réalise enfin le rêve de sa vie. Son désir de vivre une grande aventure le pousse à attacher des milliers de ballons à sa maison pour s'envoler vers les régions sauvages de l'Amérique du Sud. Mais il s'aperçoit trop tard de la présence d'un colis ayant la forme de son pire cauchemar : Russell, un jeune explorateur de 8 ans un peu trop optimiste, l'accompagnera dans son voyage.", '2009-07-29', 'English', 'Animation', 'https://www.youtube.com/watch?v=p-TdCD6DBfM', '9.8', '1H35MIN'),
('Ready Player One', "2045. Le monde est au bord du chaos. Les êtres humains se réfugient dans l'OASIS, univers virtuel mis au point par le brillant et excentrique James Halliday. Avant de disparaître, celui-ci a décidé de léguer son immense fortune à quiconque découvrira l'œuf de Pâques numérique qu'il a pris soin de dissimuler dans l'OASIS. L'appât du gain provoque une compétition planétaire. Mais lorsqu'un jeune garçon, Wade Watts, qui n'a pourtant pas le profil d'un héros, décide de participer à la chasse au trésor, il est plongé dans un monde parallèle à la fois mystérieux et inquiétant…", '2018-03-28', 'English', 'Science Fiction', 'https://www.youtube.com/watch?v=oYGkAMHCOC4', '8.0', '2H20MIN'),
('Les dents de la mer', "A quelques jours du début de la saison estivale, les habitants de la petite station balnéaire d'Amity sont mis en émoi par la découverte sur le littoral du corps atrocement mutilé d'une jeune vacancière. Pour Martin Brody, le chef de la police, il ne fait aucun doute que la jeune fille a été victime d'un requin. Il décide alors d'interdire l'accès des plages mais se heurte à l'hostilité du maire uniquement intéressé par l'afflux des touristes. Pendant ce temps, le requin continue à semer la terreur le long des côtes et à dévorer les baigneurs...", '1975-06-18', 'English', 'Humor', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', '6.0', '2H04MIN'),
('Aquaman', "Les origines d’un héros malgré lui, dont le destin est d’unir deux mondes opposés, la terre et la mer. Cette histoire épique est celle d’un homme ordinaire destiné à devenir le roi des Sept Mers.", '2015-12-19', 'English', 'Science Fiction', 'https://www.youtube.com/watch?v=WDkg3h8PCVU', '4.5', '2H24MIN');


