import datetime

from TdistClass import TD
from TdistMyUtils import *
td = TD()

'''before_march.json'''
# ### FIND ALL TASKS BEFORE MARCH 2022 and remove them ###
# write_tasks_from_filter("created before: Mar 1 2022","before_march.json")

'''tasks_archived_projects.json'''
# ### GET ALL TASKS FROM ALL ARCHIVED PROJECTS AND WRITE
# archived_tasks = tasks_from_archived_projects()
# print(len(archived_tasks))
# for t in archived_tasks[:3]+archived_tasks[-3:]:
#     print(t['date_added'], t['content'][:20])
# with open('tasks_archived_projects.json','w', encoding='utf-8') as f:
#     json.dump(archived_tasks,f,ensure_ascii=False,indent=4)
#     f.close()

'''delete_tasks'''
# to_delete = td.filter('created: -1 hours & #inbox')
# print(to_delete)

# fname = 'before_march'
# with open(f"./sorted_json/{fname}.json",'r',encoding='utf-8') as f:
#     to_delete = json.load(f)
# print(len(to_delete))
# ret = delete_tasks(to_delete)
# print(ret)