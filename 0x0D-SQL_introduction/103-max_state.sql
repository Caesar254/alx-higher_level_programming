--MySQL script that displays the max temperature of each state in order of state name.



SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
