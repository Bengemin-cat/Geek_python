-- 1) Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.
	SELECT * from users WHERE EXISTS (SELECT 1 from orders o WHERE users.id = user_id);
-- 2) Выведите список товаров products и разделов catalogs, который соответствует товару.
	SELECT p.name, c.name from products p join catalogs c on c.id = p.catalog_id;
/*3) (по желанию) Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name).
	 Поля from, to и label содержат английские названия городов, поле name — русское. Выведите список рейсов flights с русскими названиями городов.*/
	create table flights( id serial primary key, `from` varchar(100) not null, `to` varchar(100) not null);
	create table cities( id serial primary key, label varchar(100) not null, name varchar(100) not null);
	insert into cities (label,name) values ('moscow','Москва'),('novgorod','Новгород'),('irkutsk','Иркутск'),('omsk','Омск'),('kazan','Казань');
	insert into flights (`from`,`to`) values ('moscow','omsk'),('novgorod','kazan'),('irkutsk','moscow'),('omsk','irkutsk'),('moscow','kazan');
	select c.name as`from`,c_to.name as `to` from flights as f join cities as c on c.label = `from`join cities as c_to on c_to.label = `to` order by f.id;




