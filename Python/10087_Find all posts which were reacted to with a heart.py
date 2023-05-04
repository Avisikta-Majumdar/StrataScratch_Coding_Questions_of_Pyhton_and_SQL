import pandas as pd
facebook_reactions = facebook_reactions[facebook_reactions.reaction=='heart']
df = facebook_reactions.merge( facebook_posts , on='post_id', suffixes=('', '_y') )[ ['post_id', 'poster',	'post_text'	,'post_keywords', 'post_date']]
df.drop_duplicates( inplace=True )
df.head()
