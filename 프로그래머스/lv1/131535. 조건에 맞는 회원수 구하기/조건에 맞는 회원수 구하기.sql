select count(user_id) as "USERS" from user_info
where (age between 20 and 29) and (joined like "2021%");
