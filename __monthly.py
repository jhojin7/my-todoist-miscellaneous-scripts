import datetime
from TdistClass import TD
from TdistMyUtils import *
td = TD()

'''monthly cleanup'''
# find today and previous month for fname
today = datetime.date.today()
prevmonth = today - datetime.timedelta(days=30)
fname = prevmonth.strftime("%Y-%m") + ".json"
print(today,fname)

# all active task in inbox
old_str = "created after: 1 mar 2022 & created before: 1 april 2022 & #inbox"
filter_str = f"created after: {prevmonth.strftime('%Y-%m')}-1 & created before: {today.strftime('%Y-%m')}-1 & #inbox"
print(filter_str)
active = td.filter(filter_str)

# all completed task
completed = td.send_request('completed/get_all',{})['items']

# filter out completed tasks from other projects
print(len(completed))
for obj in completed:
    if obj['project_id'] != 2243803466: #inbox
        completed.pop(completed.index(obj))
monthly = active + completed

print(f"{len(monthly)} = {len(active)}+{len(completed)}")

# save data to json file
with open(fname,'w',encoding='utf-8') as f:
    json.dump({
        'metadata':{
            'fname':fname,
            'written':str(today),
            'count': f"monthly {len(monthly)} = active {len(active)} + completed {len(completed)}"
        },
        'active':active,
        'completed':completed
    },f,ensure_ascii=False,indent=4)
    f.close()