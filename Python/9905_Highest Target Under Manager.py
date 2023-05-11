import pandas as pd 
salesforce_employees=salesforce_employees[salesforce_employees.manager_id==13][['first_name', 'target']]
salesforce_employees [ salesforce_employees.target==salesforce_employees.target.max() ].head( 10 )