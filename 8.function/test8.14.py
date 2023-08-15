def make_car(manufacturer,model,**kwargs):
    """将一辆车的信息存入字典中并返回该字典"""
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

car1 = make_car('BMW','AKE101',color = 'red',size = '111')
print(car1)