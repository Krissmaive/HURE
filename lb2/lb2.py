def analyze_log_file(log_file_path):
    from collections import defaultdict
    import re

    response_codes = defaultdict(int)

    try:
        with open(log_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                match = re.search(r'"\s(\d{3})\s', line)
                if match:
                    code = match.group(1)
                    response_codes[code] += 1

    except FileNotFoundError:
        print(f"Помилка: файл '{log_file_path}' не знайдено.")
    except IOError:
        print(f"Помилка: не вдалося прочитати файл '{log_file_path}'.")

    return dict(response_codes)

# Приклад виклику
if __name__ == "__main__":
    result = analyze_log_file("apache_logs.txt")
    print("Статистика кодів відповідей HTTP:")
    for code, count in result.items():
        print(f"{code}: {count} разів")
