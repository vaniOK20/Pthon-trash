import json

def tabulate_json(input_json, indent=2):
    try:
        # Завантажуємо JSON з файлу
        with open(input_json, 'r') as file:
            data = json.load(file)

        # Перетворюємо у відформатований рядок із відступами
        formatted_json = json.dumps(data, indent=indent)

        # Зберігаємо результат у новий файл
        output_json = input_json.replace('.json', '_formatted.json')
        with open(output_json, 'w') as file:
            file.write(formatted_json)

        return f"Табульований JSON збережено у файлі: {output_json}"
    except Exception as e:
        return f"Виникла помилка: {e}"

# Приклад використання
input_json_file = 'model2.json'  # Замініть це ім'ям вашого JSON файлу
result = tabulate_json(input_json_file)
print(result)