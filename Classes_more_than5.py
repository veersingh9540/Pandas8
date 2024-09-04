import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
  res = {}
  clas_list= []
  for i in range(len(courses)):
    clas = courses['class'][i]
    student = courses['student'][i]
    if clas not in res:
      res[clas] = []
    res[clas].append(student)

  for key, value in res.items():
    if len(value) >= 5:
      clas_list.append([key, len(value)])
  DF = pd.DataFrame(clas_list, columns=["class", 'count'])
  return DF[['class']] 

  # df = courses.groupby(['class']).nunique().reset_index()

  # return df[['class']][df['student']>=5]
    