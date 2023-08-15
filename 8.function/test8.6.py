def city_country(city,country):
    """指出某个国家的城市"""
    full_name = f"{city} , {country}"
    return full_name.title()

print(f"{city_country('beijing','China')}")
print(f"{city_country('tianjing','China')}")
print(f"{city_country('guangzhou','China')}")