import requests
import csv
import os
from datetime import datetime
from datetime import timezone

# user_lst = []
# for i in user_lst:
user_names = ["Fayyaz-ur-Rehman1", "MDBhati", "zohaibsheikh007", "shanwaz-78", "uzairahmed2126", "MofiqueKhan", "mohammedasif9786", "Md-Yaseen-Dev", "Danish-chouhan", "sarfrajabbasi", "tidalu", "SuhailAhmed011", "Asrorboy07", "ravshanboymuminov", "armaanmajeed", "anwarmoazam", "saidali-ibn-zafar", "maaz-kang-92", "Muhammadkarim-98"]
users_last_activity = {}
def get_last_push(username):
    max_time = 0
    responce = requests.get(f'https://api.github.com/users/{username}/repos')
    product = responce.json()
    print(product)
    print(responce)
    for i in range(0,len(product)):
        date_time = datetime.fromisoformat(product[i]['pushed_at'][:-1]).astimezone(timezone.utc)
        if max_time == 0 or date_time>max_time:
            max_time = date_time
    return datetime.strftime(max_time,'%d-%m-%Y %H:%M:%S') if max_time!=0 else 0

for user_name in user_names:
    last_time = get_last_push(user_name)
    users_last_activity[user_name] = last_time
# print(users_last_activity)








