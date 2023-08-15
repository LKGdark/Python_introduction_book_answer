def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name']  = last
    return user_info

user_profile = build_profile(
    'Zhu','Junnan',
    location = 'HeBei',
    favourite_food = 'Yuxiangrousi',
    height = '181cm',
)

print(user_profile)