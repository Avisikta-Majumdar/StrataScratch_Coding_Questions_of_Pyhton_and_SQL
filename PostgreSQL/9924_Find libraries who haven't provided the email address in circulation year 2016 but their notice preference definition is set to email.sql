 SELECT distinct(home_library_code) FROM library_usage
where (provided_email_address is False) and ( (circulation_active_year=2016 ))
      and ( notice_preference_definition like 'email');