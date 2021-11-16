USE dnd;

LOCK TABLES `campaign` WRITE;
/*!40000 ALTER TABLE `campaign` DISABLE KEYS */;

INSERT INTO `campaign` (`id`, `name`, `dndb_id`)
VALUES
	(1,'IYKWIM',1938481);

/*!40000 ALTER TABLE `campaign` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `character` WRITE;
/*!40000 ALTER TABLE `character` DISABLE KEYS */;

INSERT INTO `character` (`id`, `name`, `dndb_id`)
VALUES
	(1,'Aehyam Weesarth',48841293),
	(2,'Sarscov',48841603),
	(3,'Eluniss',48853773),
	(4,'Henk',48845859),
	(5,'Johno',54055260),
	(6,'Pjotr Vladimir',48850684),
	(7,'Paloma Pigéon',48842849),
	(8,'Takata Wakanda',48846746);

/*!40000 ALTER TABLE `character` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `character_player` WRITE;
/*!40000 ALTER TABLE `character_player` DISABLE KEYS */;

INSERT INTO `character_player` (`id`, `player_id`, `character_id`)
VALUES
	(1,1,1);

/*!40000 ALTER TABLE `character_player` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `player` WRITE;
/*!40000 ALTER TABLE `player` DISABLE KEYS */;

INSERT INTO `player` (`id`, `name`, `password`, `role`)
VALUES
	(1,'thijs','thijs','player');

/*!40000 ALTER TABLE `player` ENABLE KEYS */;
UNLOCK TABLES;
