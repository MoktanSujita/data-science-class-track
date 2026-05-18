import pandas as pd

# labels = ['anish', 'sanam', 'kriti']
# my_list = [1,4,5]
# print(pd.Series(labels))
# print(pd.Series(data=my_list))
# familiarity_with_python = {'anish':1, 'sanam':4, 'kriti':5}
# print(familiarity_with_python)
# print("familiarity with python")
# print(pd.Series(data=labels, index = my_list))
# print(pd.Series(familiarity_with_python))

# jan_sales = pd.Series([1200,900,700,1100], index=['USA', 'Canada', 'Italy', 'Korea'])
# feb_sales = pd.Series([200,90,7000,100], index=['Japan', 'Canada', 'Italy','england'])
# print(jan_sales + feb_sales)

time = pd.Series(['2026-05-17'])
print(pd.to_datetime(time))

