select artist,count(*) from spotify_worldwide_daily_song_ranking
group by artist
order  by count(*) desc;