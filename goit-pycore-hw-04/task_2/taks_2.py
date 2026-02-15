def get_cats_info(path: str) -> list[dict]:
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 3:
                    continue
                cat_id, name, age_str = parts
                try:
                    age = int(age_str)
                except ValueError:
                    continue
                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })
    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
        print(f"Помилка читання файлу: {e}")
        return []
    return cats

cats = get_cats_info("goit-pycore-hw-04/task_2/cats_info")
print(cats)