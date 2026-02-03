users={"admin":{"role":"admin","messages":0}}

def add_user(name, role="user"):
    users[name]={"role":role,"messages":0}

def log_message(user="admin"):
    if user in users: users[user]["messages"]+=1

def get_report():
    return users
