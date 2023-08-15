cihuibiao={
    'upper':"将字符串全大写输出",
    'lower':"将字符串全小写输出",
    'title':"将字符串首字母按大写输出",
    'range':"提供一个顺序排列的字符列表",
    'append':"尾插列表",
}

for key,value in cihuibiao.items():
    print(f"{key}:{value}")

cihuibiao['keys'] = "提取字典中的key，生成一个临时列表"
cihuibiao['values'] = "提取字典中的value，生成一个临时列表"
cihuibiao['items'] = "提取字典中的key，和value生成两个临时列表"
cihuibiao['get'] = "检查字典中是否有第一个key"
cihuibiao['remove'] = "删除字典中的指定元素"

print("\n\n")

for key,value in cihuibiao.items():
    print(f"{key}:{value}")

