def read_file():
    with open("./data/third_task.txt", encoding="utf-8") as file:
        lines = file.readlines()
        table = []
        for line in lines:
            words = line.strip().split(" ")
            table.append(words)
    return table


def fill_na(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == "N/A":
                table[i][j] = (float(table[i][j - 1]) + float(table[i][j + 1])) / 2
            else:
                table[i][j] = float(table[i][j])


def filter_and_sum(table):
    results = []
    for row in table:
        # Фильтруем значения: положительные и корень > 50
        filtered_row = [x for x in row if x > 0 and (x**0.5) > 50]
        # Считаем сумму отфильтрованных значений
        row_sum = sum(filtered_row)
        results.append(row_sum)
    return results


def write_results(results):
    with open("output3.txt", "w", encoding="utf-8") as file:
        for i, sum_value in enumerate(results, 1):
            file.write(f"Сумма в строке {i}: {sum_value}\n")


table = read_file()
fill_na(table)
results = filter_and_sum(table)
print("Суммы по строкам после фильтрации:", results)

write_results(results)
