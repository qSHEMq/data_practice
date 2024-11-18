def process_numbers(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    averages = []
    for line in lines:
        numbers = [float(num) for num in line.strip().split()]
        positive_numbers = [num for num in numbers if num > 0]
        if positive_numbers:
            average = sum(positive_numbers) / len(positive_numbers)
            averages.append(average)

    max_val = max(averages)
    min_val = min(averages)

    with open("output2.txt", "w", encoding="utf-8") as outfile:
        for average in averages:
            outfile.write(f"{average:.2f}\n")

        outfile.write("-----------\n")
        outfile.write(f"max_val: {max_val:.2f}\n")
        outfile.write(f"min_val: {min_val:.2f}\n")


process_numbers("./data/second_task.txt")
