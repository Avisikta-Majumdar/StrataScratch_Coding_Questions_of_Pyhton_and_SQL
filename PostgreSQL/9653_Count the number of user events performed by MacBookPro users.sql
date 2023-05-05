select event_name, count(*) as event_count from playbook_events
where device ilike 'macbook pro'
group by event_name
order by event_count desc;