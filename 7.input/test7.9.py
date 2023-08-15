sandwich_orders = ["aaa","bbb","aaa","ccc","aaa","ddd","eee"]
finished_sandwiches = []
while sandwich_orders :
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
finished_sandwiches.reverse()
print(f"finshed sandwiches : {finished_sandwiches}")

print("\naaa sold down!\n")
while 'aaa' in finished_sandwiches :
    finished_sandwiches.remove('aaa')

print(f"finshed sandwiches : {finished_sandwiches}")