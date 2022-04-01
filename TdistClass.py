import os
import json
import dotenv
import requests
from todoist_api_python.api import TodoistAPI

class TD():
    def __init__(self):
        dotenv.load_dotenv()
        self.URL = 'https://api.todoist.com/sync/v8' 
        self.TOKEN = os.getenv('TOKEN')
        self.RESTapi = TodoistAPI(self.TOKEN)

    def filter(self, filter_str:str)->list:
    # RESTapi
        try:
            filtered_tasks = self.RESTapi.get_tasks(filter=filter_str)
            # return filtered_tasks
            return [obj.to_dict() for obj in filtered_tasks]
        except Exception as error:
            print(error)
            return None

    def send_request(self,endpoint:str,params)-> list:
    # SYNC api
        headers = {"Authorization": f"Bearer {self.TOKEN}"}
        r = requests.get(f"{self.URL}/{endpoint}",headers=headers,params=params)

        # Task.to_dict()
        ### tasks == Task()
        ### project == dict
        objs =  json.loads(r.text)
        return objs

    def delete_task(self, task_id:int):
    # REST
        try:
            is_success = self.RESTapi.delete_task(task_id)
            print(f"Deleting {task_id}... {is_success}")
        except Exception as e:
            print(e)




