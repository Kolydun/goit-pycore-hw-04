def total_salary(path: str) -> tuple[float, float]:
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as salary:
            for line in salary:
                line = line.strip()
                if not line:
                    continue
                parts = line.rsplit(",", 1)
                if len(parts) != 2:
                    continue
                try:
                    amount = float(parts[1])
                except ValueError:
                    continue
                total += amount
                count += 1
    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
        print(f"Помилка читання файлу: {e}")
        return (0, 0)
    average = total / count if count > 0 else 0
    return (int(total), int(average))

total, average = total_salary("goit-pycore-hw-04/task_1/salary")
print(total, average)
