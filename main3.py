import requests

def update_student(student_id, updated_data):
    url = f"http://127.0.0.1/students/{student_id}"
    response = requests.put(url, json=updated_data)
    return response.json()

#  использования функции
if __name__ == "__main__":
    student_id = 4
    updated_data = {"name": "Новый Студент", "age": 23, "major": "Химия"}
    response = update_student(student_id, updated_data)
    print(response)
