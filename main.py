import requests

def get_all_students():
    url = "http://127.0.0.1/students"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Ошибка при получении списка студентов:", response.status_code)
        return None

def get_student_by_id(student_id):
    url = f"http://127.0.0.1/students/{student_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print("Студент с указанным идентификатором не найден")
        return None
    else:
        print("Ошибка при получении информации о студенте:", response.status_code)
        return None

#  использования функций
if __name__ == "__main__":
    all_students = get_all_students()
    if all_students:
        print("Список всех студентов:")
        for student in all_students:
            print(student)

    student_id = 1
    student_info = get_student_by_id(student_id)
    if student_info:
        print(f"\nИнформация о студенте с ID {student_id}:")
        print(student_info)