def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计， 直到没有来打印的设计为止
    打印每个设计后， 都将其移到列表 completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

