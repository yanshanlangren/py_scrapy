-- dev.news definition

CREATE TABLE `news` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `source` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `content` text,
  `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `additional_data` varchar(255) DEFAULT NULL,
  `authors` varchar(255) DEFAULT NULL,
  `images` varchar(255) DEFAULT NULL,
  `keywords` varchar(255) DEFAULT NULL,
  `meta_description` varchar(255) DEFAULT NULL,
  `publish_date` datetime DEFAULT NULL,
  `tags` varchar(255) DEFAULT NULL,
  `canonical_link` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=340 DEFAULT CHARSET=utf8;