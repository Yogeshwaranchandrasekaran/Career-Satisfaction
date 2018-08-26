
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv('survey_results_public.csv')
schema_df = pd.read_csv('survey_results_schema.csv')


# In[4]:



chosen_columns = ['Professional', 'ProgramHobby', 'University', 'EmploymentStatus',
                  'FormalEducation', 'MajorUndergrad', 'YearsProgram', 'YearsCodedJob',
                  'DeveloperType', 'CareerSatisfaction']


# In[5]:


column_definitions = schema_df[schema_df['Column'].isin(chosen_columns)]


# In[6]:


for ix, row in column_definitions.iterrows():
    print(row['Column'])
    print(row['Question'], '\n')


# In[7]:


data = df[chosen_columns]


# In[8]:



data.columns = ['professional', 'program_hobby', 'university' ,'employment_status',
                'formal_education', 'major_undergrad', 'years_program', 'years_coded_job',
                'developer_type', 'career_satisfaction']


# In[9]:



data = data.dropna()
data.head(5)


# In[10]:


for column in data.columns:
    print(column)
    print(data[column].unique(), '\n')


# In[27]:



data['years_program_int'] = data['years_program'].map(lambda resp: int(resp.split(" ")[0]) if not resp == 'Less than a year' else 0)
data['years_coded_int'] = data['years_coded_job'].map(lambda resp: int(resp.split(" ")[0]) if not resp == 'Less than a year' else 0)

data['hobby'] = data['program_hobby'].map(lambda resp: resp.split(",")[0])

data['type_count'] = data['developer_type'].map(lambda resp: len(resp.split(';')))


# In[28]:


len(data[data['years_coded_int'] > data['years_program_int']])


# In[29]:



data.groupby(['hobby'])['hobby'].count()


# In[30]:



data.groupby(['program_hobby'])['career_satisfaction'].mean()


# In[31]:



data.groupby(['developer_type'])['career_satisfaction'].mean()


# In[32]:



data.groupby(['type_count'])['career_satisfaction'].agg(['count', 'mean'])


# In[33]:


sns.regplot(x='type_count', y='career_satisfaction', data=data, x_estimator=pd.np.mean)


# In[34]:



(
    data[data['type_count'] == 1]
    .groupby('developer_type')['career_satisfaction']
    .mean()
    .sort_values(ascending=False)
)


# In[35]:



(
    data
    .groupby('university')['career_satisfaction']
    .mean()
    .sort_values(ascending=False)
)


# In[36]:



(
    data
    .groupby('employment_status')['career_satisfaction']
    .mean()
    .sort_values(ascending=False)
)


# In[37]:



(
    data
    .groupby('formal_education')['career_satisfaction']
    .mean()
    .sort_values(ascending=False)
)


# In[38]:



(
    data
    .groupby('major_undergrad')['career_satisfaction']
    .mean()
    .sort_values(ascending=False)
)

