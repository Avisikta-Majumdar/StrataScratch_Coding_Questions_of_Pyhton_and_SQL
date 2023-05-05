select host_id, guest_id from airbnb_hosts host 
inner join airbnb_guests guest on host.nationality=guest.nationality
and host.gender=guest.gender
limit 12;