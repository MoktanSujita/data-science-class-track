import pandas as pd

data = pd.read_csv("Salaries.csv")


#highest basepay
# highest_basepay = data["BasePay"].max()
# print("Highest BasePay:", highest_basepay)


# #average basepay
# average_basepay = data["BasePay"].mean()
# print("Average BasePay:", average_basepay)

# #highest total pay
# highest_total_pay = data["TotalPay"].max()
# print("Highest Total pay:", highest_basepay)

# #highest overtime pay
# highest_overtime_pay= data["OvertimePay"].max()
# print("Highest Overtime Pay:", highest_overtime_pay)

# top_paid = data.loc[data["TotalPay"].idxmax()]
# print(f'{top_paid} \n {top_paid["EmployeeName"]} is the top paid employee')

# print(data.head().to_csv)
# print(data.describe()) #max, min 

# print(data.describe().to_csv('describe.csv'))
# print(data.columns)
# print(data['BasePay'])
print(data.iloc[data['EmployeeName']=='SANAM MARIKHU'])
# print(data['BasePay'].iloc[148651])
# print(data['BasePay'].fillna(data['BasePay'].mean()))
# print(data['BasePay'].isnull())
# print(data['BasePay'].isnull().sum())

