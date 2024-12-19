import re
import matplotlib.pyplot as plt

file_path = 'data.txt'

dates = []
temperatures = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        match = re.search(r'(\d{4}-\d{2}-\d{2}): Temperature = (\d+)°C', line)
        if match:
            temp = int(match.group(2)) 
            if temp >= 13: 
                dates.append(match.group(1))
                temperatures.append(temp)


if temperatures:
    max_temp = max(temperatures)
    max_temp_index = temperatures.index(max_temp)
    max_temp_date = dates[max_temp_index]
    print(f"Самая высокая температура: {max_temp}°C, дата: {max_temp_date}")
else:
    print("Данные о температурах отсутствуют после фильтрации.")

plt.figure(figsize=(10, 6))
plt.plot(dates, temperatures, marker='o', linestyle='-', color='b', label='Temperature')
plt.title('Температура по дням (без значений ниже 13°C)', fontsize=16)
plt.xlabel('Дата', fontsize=12)
plt.ylabel('Температура (°C)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('filtered_temperature_plot.png')
plt.show()



#-2
plt.figure(figsize=(10, 6))
plt.hist(temperatures, bins=10, color='skyblue', edgecolor='black')
plt.title('Распределение температур', fontsize=16)
plt.xlabel('Температура (°C)', fontsize=12)
plt.ylabel('Частота', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('temperature_histogram.png')
plt.show()

