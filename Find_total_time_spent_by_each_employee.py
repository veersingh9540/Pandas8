import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
  res = []
  for i in range(len(employees)):
    total_time = employees['out_time'][i] - employees['in_time'][i]
    res.append([employees['event_day'][i],employees['emp_id'][i],total_time])

  res_df = pd.DataFrame(res, columns= ['day', 'emp_id', 'total_time']).groupby(['day','emp_id']).sum().reset_index()


  return res_df