rivers = {
    'Nile':'Uganda',
    'Amazon River':'Reru',
    'The Yangtze River':'China',
    'Yellow River':'China',
    }

for river,nation in rivers.items():
    print(f"{river} runs through {nation}")

print('\n')
for river in rivers.keys():
    print(river)

print('\n')
for nation in rivers.values():
    print(nation)