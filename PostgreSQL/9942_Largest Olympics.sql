select games, count(distinct id) 
from olympics_athletes_events
group by games
order by 2 desc
limit 1;