-- Пусть задан некоторый пользователь. 
-- Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем.
-- select from_user_id ,to_user_id from messages m where from_user_id in

select  to_user_id from messages m where 'approved' = (select status from friend_requests fr 
where  initiator_user_id = from_user_id and target_user_id = to_user_id limit 1) and from_user_id = 113 group by to_user_id
limit 1
-- Подсчитать общее количество лайков, которые получили 10 самых молодых пользователей.


	SELECT COUNT(user_id) FROM (
	SELECT user_id, (SELECT birthday 
                     FROM profiles as P 
					 WHERE P.user_id = L.user_id) as birthday
	FROM likes as L
    ORDER BY birthday DESC 
    LIMIT 10
) AS T;

--Определить кто больше поставил лайков (всего) - мужчины или женщины?

SELECT sex FROM (
SELECT sex, COUNT((SELECT COUNT(*) FROM likes as L where L.user_id = P.user_id)) as gender_likes_count FROM profiles as P
WHERE sex = 'm'
GROUP BY sex
UNION ALL
SELECT sex, COUNT((SELECT COUNT(*) FROM likes as L where L.user_id = P.user_id)) FROM profiles as P
WHERE sex = 'f'
GROUP BY sex
) AS T
GROUP BY sex
ORDER BY MAX(gender_likes_count) DESC
LIMIT 1;


-- Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети.
 
SELECT (SELECT fullname FROM users where id = user_id) fullname,  SUM(T.rnk) AS rnk
FROM(
	SELECT from_user_id as user_id, COUNT(*) as rnk  FROM messages -- Неактивные пользователи мало отправляют сообщения
	GROUP BY from_user_id
	UNION ALL
	SELECT user_id, COUNT(*)  FROM likes -- Неактивные пользователи мало лайкуют
	GROUP BY user_id
	UNION ALL
	SELECT user_id, COUNT(*)  FROM friendship -- И друзей у таких пользователей мало
	GROUP BY user_id
	UNION ALL
	SELECT friend_id, COUNT(*)  FROM friendship 
	GROUP BY friend_id
	UNION ALL
	SELECT user_id, COUNT(*)  FROM communities_users
	GROUP BY user_id
) AS T
GROUP BY fullname
ORDER BY rnk
LIMIT 10;









