#3.4
Dinner_attend=['Grandfather','Grandfather','Mother','Father','Sister']
print(f'Attend name: {Dinner_attend}\n')

#3.5

Change_name=Dinner_attend.pop(0)
print(f"{Change_name} was no time to attend this party\n")
Dinner_attend.append('Grandmother')
print(f'Attend name: {Dinner_attend}\n')

#3.6

Dinner_attend.append('Brother')
Dinner_attend.insert(0,'Adswa')
Dinner_attend.insert(3,'Dgsrdf')
print(f'Attend name: {Dinner_attend}\n')

#3.7

print(f"Sorry,not {Dinner_attend.pop(-1)}\n")
print(f"Sorry,not {Dinner_attend.pop(-1)}\n")
print(f"Sorry,not {Dinner_attend.pop(-1)}\n")
print(f"Sorry,not {Dinner_attend.pop(-1)}\n")
print(f"Sorry,not {Dinner_attend.pop(-1)}\n")
print(f"Sorry,not {Dinner_attend.pop(-1)}\n")
print(f"You alaways did {Dinner_attend[0]}\n")
print(f"You alaways did {Dinner_attend[1]}\n")
del Dinner_attend[0]
del Dinner_attend[0]
print(Dinner_attend)
print(f"the party num is {len(Dinner_attend)}")

