#1
import pandas as pd
import numpy as np
list = [1, 2, 3, 4, 5]
series_from_list = pd.Series(list)
df_from_list = pd.DataFrame([list], columns=['A', 'B', 'C', 'D', 'E'])
np_array = np.array([10, 20, 30, 40, 50])
series_from_np = pd.Series(np_array)
dict_data = {'Имя': ['Lucrezia', 'Antonio', 'Francesco'], 'Лет': [22, 33, 31]}
df_from_dict = pd.DataFrame(dict_data)
print(series_from_list)
print(df_from_list)
print(series_from_np)
print(df_from_dict)

#2
series_1 = pd.Series([1, 2, 3, 4, 5])
series_2 = pd.Series([4, 5, 6, 7, 8])
unique_to_series1 = series_1[~series_1.isin(series_2)]
unique_to_series2 = series_2[~series_2.isin(series_1)]
print("Не пересекающиеся элементы в первой Series:")
print(unique_to_series_1)
print("Не пересекающиеся элементы во второй Series:")
print(unique_to_series_2)

#3
import matplotlib.pyplot as plt
series = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
value_counts = series.value_counts()
plt.bar(value_counts.index, value_counts.values)
plt.xlabel('Уникальные элементы')
plt.ylabel('Частота')
plt.title('Частота уникальных элементов в Series')
plt.show()

#4
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
df_concat_vertical = pd.concat([df1, df2], ignore_index=True)
print(df_concat_vertical)

#5
df = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y1': [1, 4, 9, 16, 25],
    'Y2': [1, 8, 27, 64, 125]
plt.plot(df['X'], df['Y1'], label='Y1 = X^2')
plt.plot(df['X'], df['Y2'], label='Y2 = X^3')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Зависимость Y от X')
plt.legend()
plt.show()
