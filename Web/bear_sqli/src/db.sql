SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

DROP DATABASE IF EXISTS `ctftraining`;
CREATE DATABASE ctftraining;
USE ctftraining;

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL DEFAULT 'e10adc3949ba59abbe56e057f20f883e',
  `flag` varchar(50) NOT NULL DEFAULT 'catctf{test}',
  PRIMARY KEY (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

INSERT users (username,password,flag) VALUES ('admin','21232f297a57a5a743894a0e4a801fc3','远在天边，近在眼前~');
INSERT users (username,password,flag) VALUES ('guest','084e0343a0486ff05530df6c705c8bb4','catctf{test}');

SET FOREIGN_KEY_CHECKS = 1;
