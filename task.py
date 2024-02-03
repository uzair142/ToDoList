import json
import requests
import uuid  # For generating unique IDs

def add_task():
    add_task_input = input("Do you want to add a task? (yes/no): ").lower()

    if add_task_input == 'yes':
        task = input("Enter the task: ")

        # Generate a unique ID for the task
        task_id = str(uuid.uuid4())

        task_data = {
            'id': task_id,
            'task': task,
            'completionStatus': "a"
        }

        send_task_to_azure_function(task_data)
        print(f"Task with ID '{task_id}' added successfully!")
    else:
        print("No task added.")

def send_task_to_azure_function(task_data):
    azure_function_url = "https://apprenticeshipp.azurewebsites.net/api/UpdateToDoList?code=AdbUS9OuaFk-sRm9WxXfoKlLjMhcskAiVBvfMA3h9i3LAzFufpqhuw=="  

    try:
        response = requests.post(azure_function_url, json=task_data)
        response.raise_for_status()
        print(f"Azure Function response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send task to Azure Function. Error: {str(e)}")

if __name__ == "__main__":
    add_task()
