import pandas as pd
import numpy as np

# df =pd.DataFrame(np.random.randint(0,50,size=(4,4)),
#                    columns=['Player', 'Enemy','Tree','House'],
#                    index=['x_position','y_position','scale','Rotation'])

# df['new']= df['Player'] + df['Enemy']
# print(df)
# assigned = df.drop('new', axis=1)
# print(assigned)

# print(df.loc['x_position'] + df.loc['y_position']) #sum of all the values of x_position and y_position
# print(df.iloc[0:2]) #x_position and y_position
# print(df['Player']>3)
# # print(df.drop('new' ,axis=1, inplace=True)) #by default data cannot be replaced so inplace is required to completely change the original data
# # print(df)

#array = np.array([0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15])

array = (np.arange(16).reshape(4,4))
df =pd.DataFrame(array,
                   columns=['Player', 'Enemy','Tree','House'],
                   index=['x_position','y_position','scale','Rotation'])
# print(df)
# print(df.loc['scale'])
# print(df.loc['scale','Tree'])
# print(df.loc['Rotation','Tree'])
# print(df.loc['y_position','Tree'])
# print(df.loc['y_position','Enemy'])
# print(df.loc['scale','Enemy'])
# print(df.loc['scale','Tree'])
# print(df.iloc[1:2])

#print(df.loc[['y_position','scale'],['Enemy','Tree']])
#print(df.loc[0])
#print(df.iloc[1])
print(df.iloc[:,0])   #[from :kati samma],[column]
print(df.iloc[[1,2],[1,2]]) #[kun,kun row],[kun,kun column]
