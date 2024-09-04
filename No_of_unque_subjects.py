import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
  res = {}
  result = []
  for i in range(len(teacher)):
    teacher_id = teacher['teacher_id'][i]
    subject_id = teacher['subject_id'][i]
    if teacher_id not in res:
      res[teacher_id] = set()
    res[teacher_id].add(subject_id)

  for key, value in res.items():
    result.append([key, len(value)])
  return pd.DataFrame(result, columns= ['teacher_id', 'cnt'])

#   DF = teacher.groupby(['teacher_id'])['subject_id'].nunique().reset_index()
#   return pd.DataFrame(DF).rename(columns = {'subject_id': 'cnt'})




    