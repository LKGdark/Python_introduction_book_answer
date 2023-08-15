zhangkaijing = {
    'first_name' : 'zhang',
    'second_name' : 'kaijing',
    'location' : 'tufe',
}

bifujian = {
    'first_name' : 'bi',
    'second_name' : 'fujian',
    'location' : 'beijing',
}

zhaoliying = {
    'first_name' : 'zhao',
    'second_name' : 'liying',
    'location' : 'shanghai',
 }

people = [zhangkaijing,bifujian,zhaoliying]

for peo in people:
    name = f"{peo['first_name']}_{peo['second_name']}"
    print(f"This people name is {name}")
    print(f"This people locate in {peo['location']}\n")

