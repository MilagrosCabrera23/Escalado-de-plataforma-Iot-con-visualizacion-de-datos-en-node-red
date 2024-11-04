CREATE DATABASE evidencia2; 

USE evidencia2; 

CREATE TABLE `datos_sensor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `temperature` float DEFAULT NULL,
  `humidity` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) 
INSERT INTO `datos_sensor` VALUES (1,'2024-10-04 04:18:37',24,40),(2,'2024-10-04 14:57:58',23,62.5),(3,'2024-10-04 14:58:13',23,62.5),(4,'2024-10-04 15:00:04',-30.1,0);

SELECT * FROM datos_sensor;