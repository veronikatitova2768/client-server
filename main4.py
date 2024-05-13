import requests

def delete_student(student_id):
    url = f"http://127.0.0.1/students/{student_id}"
    response = requests.delete(url)
    return response.json()

# использования функции
if __name__ == "__main__":
    student_id = 4
    response = delete_student(student_id)
    print(response)
