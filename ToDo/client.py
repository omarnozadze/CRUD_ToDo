import requests

class TaskClient:
    BASE_URL = "http://127.0.0.1:8000/tasks/"

    def create_task(self, **task):
        return requests.post(f"{TaskClient.BASE_URL}", json=task).json()

    def get_task(self, task_id):
        return requests.get(f"{TaskClient.BASE_URL}{task_id}").json()

    def get_all_tasks(self):
        return requests.get(f"{TaskClient.BASE_URL}").json()

    def update_task(self, task_id, **task):
        return requests.put(f"{TaskClient.BASE_URL}{task_id}", json=task).json()

    def delete_task(self, task_id):
        return requests.delete(f"{TaskClient.BASE_URL}{task_id}").json()

client = TaskClient()

class UserInput:
    client = TaskClient()


    def prompt(self):
        print("1. Create")
        print("2. Get all tasks")
        print("3. Update task")
        print("4. Delete task")
        user_input = input("Which operation do you want? Choose a number: ")

        if user_input == "1":
            self.create_task()
        if user_input == "2":
            self.get_all_tasks()
        if user_input == "3":
            self.update_task()
        if user_input == "4":
            self.get_all_tasks()
            

    def create_task(self):
        all_tasks = self.client.get_all_tasks()
        if all_tasks:
            last_task = all_tasks[-1]
            task_id = last_task['id'] + 1
        else:
            task_id = 1
        title = input("Enter the task title: ")
        if len(title) == 0:
            raise TypeError
        completed = input("Is the task completed? (Y/N): ").lower()
        if completed == "y":
            completed = True
        elif completed == "n":
             completed = False
        else:
            raise ValueError
        task = {"id": task_id, "title": title, "completed": completed}
        self.client.create_task(**task)
        print("Task created successfully!")

    def get_all_tasks(self):
        return requests.get(f"{TaskClient.BASE_URL}").json()
        

    def update_task(self):
        task_id = int(input("Enter the ID of the task you want to update: "))
        print (self.client.get_task(task_id))
        title = input("Enter the new task title: ")
        completed = input("Is the task completed? (Y/N): ").lower()
        if completed == "y":
            completed = True
        else:
            completed = False

        task = {"id": task_id, "title": title, "completed": completed}
        client.update_task(task_id, **task)
        print("Task updated successfully!")

    def delete_task(self):
        task_id = int(input("Enter the ID of the task you want to delete: "))
        task = self.client.get_task(task_id)
        if task:
            self.client.delete_task(task_id)
            print(f"Task with ID {task_id} deleted successfully!")
        else:
            print("Task not found.")

        


    

       

user_input = UserInput()
user_input.prompt()
user_input.delete_task()


#print(user_input.get_all_tasks())




# client.create_task(id=22, title="Walk the dog", completed=False)
# print(client.get_all_tasks())
# print(client.update_task(20, id=20, title="Walk the dog again", completed=False))
# print(client.delete_task(19))