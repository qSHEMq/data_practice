import csv


def read_csv(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(
                {
                    "product_id": int(row["product_id"]),
                    "name": row["name"],
                    "price": float(row["price"]),
                    "quantity": int(row["quantity"]),
                    "category": row["category"],
                    "description": row["description"],
                    "production_date": row["production_date"],
                    "expiration_date": row["expiration_date"],
                    "rating": float(row["rating"]),
                    "status": row["status"],
                }
            )
    return data


data = read_csv("data/fourth_task.txt")

# Удаляем столбец description
modified_data = []
for item in data:
    item.pop("description")  # удаляем ключ description
    modified_data.append(item)

# Среднее арифметическое по столбцу rating
avg_rating = sum(item["rating"] for item in data) / len(data)

# Максимум по столбцу rating
max_rating = max(item["rating"] for item in data)

# Минимум по столбцу price
min_price = min(item["price"] for item in data)

# Фильтрация по status
filtered_data = [item for item in modified_data if item["status"] != "On Backorder"]

# Записываем числовые результаты в текстовый файл
with open("output4.txt", "w", encoding="utf-8") as f:
    f.write(f"{avg_rating}\n")
    f.write(f"{max_rating}\n")
    f.write(f"{min_price}\n")

# Записываем отфильтрованные данные в новый CSV файл
if filtered_data:
    fieldnames = filtered_data[0].keys()
    with open("modified_data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_data)
