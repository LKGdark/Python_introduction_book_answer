current_users=['Adfsa','Fsda','Darkcool','sdasdf','dwdas','safdgv']
new_user=['Fsda','seddv','fceadf','darkcool']
current_users_lower=[]
for user in current_users:
    current_users_lower.append(user.lower())
for user in new_user:
    if user.lower() not in current_users_lower:
        print(f"{user} not in current_user,can use it!\n")
    else :
        print(f"You can't use {user},beacuse it is used!\n")