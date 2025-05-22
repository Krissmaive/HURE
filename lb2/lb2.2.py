import hashlib

def generate_file_hashes(*file_paths):
    hashes = {}

    for path in file_paths:
        try:
            with open(path, "rb") as file:
                file_data = file.read()
                sha256_hash = hashlib.sha256(file_data).hexdigest()
                hashes[path] = sha256_hash
        except FileNotFoundError:
            print(f"Помилка: файл '{path}' не знайдено.")
        except IOError:
            print(f"Помилка: не вдалося прочитати файл '{path}'.")

    return hashes

# Виклик функції з двома файлами
if __name__ == "__main__":
    result = generate_file_hashes("file1.txt", "log.txt")

    print("SHA-256 хеші файлів:")
    for file, hash_val in result.items():
        print(f"{file}: {hash_val}")
