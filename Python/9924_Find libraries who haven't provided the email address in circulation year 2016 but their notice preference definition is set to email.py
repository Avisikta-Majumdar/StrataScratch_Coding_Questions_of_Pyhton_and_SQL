import pandas as pd
df = library_usage [ ( library_usage.circulation_active_year==2016 ) & (library_usage.provided_email_address==False) & 
                    ( library_usage.notice_preference_definition=='email')].drop_duplicates( subset='home_library_code')
df.home_library_code.head()
