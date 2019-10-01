import hashlib

from models.task_list import TaskList


class Dev:
    def __init__(self, email, password, first_name, second_name, age, task={}):
        self.task = {}
        self.task_to_do = TaskList({})
        self.task_in_progress = TaskList({})
        self.task_resolve = TaskList({})
        self.task_Default = TaskList({})
        self.email = email
        self.password = password
        self.first_name = first_name
        self.second_name = second_name
        self.age = age  # TODO Rework, list_of_tasks shuld be [to do, in progress, done, resolve, Default=To do]
        self.uid = hashlib.sha224(bytes(str(self), 'utf-8')).hexdigest()[:10]
        if task:
            if isinstance(task, dict):
                for t in task:
                    self.task[t.uid] = t
                    self.task_to_do.add_task(t)
            else:
                self.task[task.uid] = task
                self.task_to_do.add_task = task

    # def __str__(self):
    #     tasks = ''
    #     for i in self.task.values():
    #         tasks += str(i.name)
    #     return f'Developer mail: {self.email}, first name:{self.first_name}, second name: {self.second_name}, ' \
    #            f'age: {self.age}, {tasks} '

    def change_email(self, email):
        return self.email == email

    def check_password(self, my_password):
        return self.password == my_password

    def add_task(self, task):
        self.task[task.uid] = task

    def remove_task(self, task):
        if isinstance(task, list):
            for t in task:
                del self.task[t]
        else:
            del self.task[task]

    def show_all_dev_task(self):
        if isinstance(self.task, list):
            for i in self.task:
                return

    def show_accepted_task(self):
        pass
