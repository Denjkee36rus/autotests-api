import json

json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)


read_data = {
    "name": "Мария",
    "age": 25,
    "is_student": True
}
json_string = json.dumps(read_data, indent= 2)


with open("json_example.json", "r", encoding="utf-8") as file:
    data = json.load(file)


with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(read_data, file, indent= 2, ensure_ascii= False)

