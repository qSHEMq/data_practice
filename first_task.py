def analyze_text(filename):
    with open(filename, encoding="utf-8") as file:
        lines = file.readlines()
        words = []

        for line in lines:
            line1 = (
                line.replace("'", "")
                .replace('"', "")
                .replace("?", "")
                .replace("!", "")
                .replace(",", "")
                .replace(".", "")
                .replace("-", " ")
                .lower()
                .strip()
            )
            words += line1.split()

    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1

    sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    long_words = [word for word in words if len(word) > 4]
    total_words = len(words)
    long_words_count = len(long_words)
    long_words_percentage = (long_words_count / total_words) * 100

    with open("output.txt", "w", encoding="utf-8") as outfile:
        for word, freq in sorted_freq:
            outfile.write(f"{word}:{freq}\n")

        outfile.write("-----------\n")
        outfile.write(f"Количество слов длиннее 4 символов: {long_words_count}\n")
        outfile.write(f"Доля слов длиннее 4 символов: {long_words_percentage:.2f}%\n")


analyze_text("./data/first_task.txt")
