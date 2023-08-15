def city_country_mix(city,country,population=''):
    if population:
        mix = f'{city},{country},{population}'
    else:
        mix = f'{city},{country}'
    return mix.title()