import json
from TdistClass import TD
td = TD()

def write_tasks_from_filter(filter_str,fname)->None:
### FIND ALL TASKS BEFORE MARCH 2022 and remove them ###
    filtered_tasks = td.filter(filter_str)

    print(len(filtered_tasks))
    for t in filtered_tasks[:3]+filtered_tasks[-3:]:
        print(t['created'], t['content'][:20])

    with open(fname,'w',encoding='utf-8') as f:
        lines = []
        for task in filtered_tasks:
            lines.append(task)
        if len(lines) == len(filtered_tasks):
            json.dump(lines,f,ensure_ascii=False,indent=4)
            f.close()
        else:
            print("len(lines) == len(filtered_tasks) doens't match")


# ARCHIVED TASKS (SYNCapi)
def tasks_from_project(project_id)->list:
# GET ARCHIVED TASKS FROM ARCHIVED TASKS
    params = {"sync_token":"*","project_id":project_id}
    tasks = td.send_request('projects/get_data',params)['items']
    return tasks

def tasks_from_archived_projects()->list:
# GET ALL TASKS FROM ALL ARCHIVED PROJECTS
    # GET ARCHIVED PROJS
    params = {"sync_token":"*"}
    archived_projects = td.send_request('projects/get_archived',params)

    archived_tasks = []
    for project in archived_projects:
        print('Archived Project: ',project['id'],project['name'])
        archived_tasks += tasks_from_project(project['id'])
    # len(archived_tasks) # 543 // 494 for last3
    print(f"archived_projects:{len(archived_projects)}, archived_tasks:{len(archived_tasks)}")
    return archived_tasks

def delete_tasks(tasks:list)->str:
# DELETE MULTIPLE TASKS
    try:
        for task in tasks:
            td.delete_task(task['id'])
        return f">>> {len(tasks)} of tasks deleted"
    except Exception as e:
        return e