sandwich_orders = ["aaa","bbb","ccc","ddd","eee"]
finished_sandwiches = []
while sandwich_orders :
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
finished_sandwiches.reverse()
print(f"finshed sandwiches : {finished_sandwiches}")