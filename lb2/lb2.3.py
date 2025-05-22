def filter_ips(input_file_path, output_file_path, allowed_ips):
    from collections import defaultdict
    import re

    ip_counts = defaultdict(int)

    try:
        with open(input_file_path, 'r', encoding='utf-8') as infile:
            for line in infile:
                match = re.match(r'^(\d{1,3}(?:\.\d{1,3}){3})', line)
                if match:
                    ip = match.group(1)
                    if ip in allowed_ips:
                        ip_counts[ip] += 1

    except FileNotFoundError:
        print(f"Помилка: вхідний файл '{input_file_path}' не знайдено.")
        return
    except IOError:
        print(f"Помилка: не вдалося прочитати файл '{input_file_path}'.")
        return

    try:
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            for ip, count in ip_counts.items():
                outfile.write(f"{ip} - {count}\n")

    except IOError:
        print(f"Помилка: не вдалося записати у файл '{output_file_path}'.")

# Виклик
if __name__ == "__main__":
    allowed_ips = ["127.0.0.1", "192.168.1.1", "10.0.0.2"]
    filter_ips("input_file_path.txt", "allowed_ip_report.txt", allowed_ips)
