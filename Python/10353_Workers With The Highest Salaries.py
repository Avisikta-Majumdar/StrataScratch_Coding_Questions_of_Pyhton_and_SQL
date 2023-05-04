import pandas as pd
df = worker.merge( title, left_on='worker_id', right_on= 'worker_ref_id')
val  = df[df.salary== max(worker.salary)].worker_title.values
result = pd.DataFrame( {'best_paid_title': val})
result.head()
