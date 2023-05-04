import pandas as pd
result = lyft_drivers[ (lyft_drivers.yearly_salary<=30_000) | (lyft_drivers.yearly_salary>=70_000)  ]
result.head( result.shape[0] )
