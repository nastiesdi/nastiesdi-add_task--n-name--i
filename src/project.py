from src.task import Task
from src.main_class import MainClass
from reformat import str_

class Project(MainClass):
    def __init__(self, name_project, task=[], dev=None):
        super().__init__()
        self.name_project = name_project
        self.task = task
        self.dev = dev

    def __str__(self):
        return f'Name project: {self.name_project}'

    def add_task_to_project(self, task):
        # self.task = Project.task
        if isinstance(task, list):
            for i in task:
                self.task.append(i)
        else:
            self.task.append(task)  # rabotaet

    def print_all_task(self):
        if isinstance(self, Project):
            tasks = [r.name for r in self.task]
        return f'All task for project {self.name_project}: \n' + str_(list(zip(self.get_len_str(self.task), tasks))).create_list_vision()

