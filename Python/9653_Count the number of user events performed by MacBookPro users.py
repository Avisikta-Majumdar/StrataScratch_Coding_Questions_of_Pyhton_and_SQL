import pandas as pd
df = playbook_events[ playbook_events.device=='macbook pro']
r = df.event_name.value_counts().to_dict()
v1 = r.keys()
v2=r.values()
result = pd.DataFrame( {"event_name": v1 , "event_count":v2} )
result.head(10)
