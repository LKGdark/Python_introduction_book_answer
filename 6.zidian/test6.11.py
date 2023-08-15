cities = {
    'Beijing':{
        'nation': 'China',
        'number': 100_000_888,
    },
    'Tianjing':{
        'nation': 'China',
        'number': 50_000_888,
    },
    'Hebei':{
        'nation': 'China',
        'number': 40_000_888,
    },
}

for country,nn in cities.items():
    print(f'{country}:')
    print(f"{nn}\n")