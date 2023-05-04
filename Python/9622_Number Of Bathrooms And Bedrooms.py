import pandas as pd
import numpy as np
airbnb_search_details.head()
city_grp = airbnb_search_details.groupby(['city','property_type'])
l=[]
for i, dd in city_grp:
    l.append([i[0], i[1],  np.mean(dd.bedrooms.values), np.mean(dd.bathrooms.values) ])
    
df = pd.DataFrame(l , columns=['city', 'property_type', 'n_bedrooms_avg', 'n_bathrooms_avg'])
