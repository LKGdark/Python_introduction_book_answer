while True:
    print("Please input two number,and I will add them then return for you.")
    print("press 'q' to Exit")
    first_num = input('first number:')
    if first_num == 'q':
        break
    second_num = input('second number:')
    if second_num == 'q':
        break
    try:
        sum_number = int(first_num) + int(second_num)
    except ValueError:
        print("请输入两个数字而不是其他符号。")
    else:
        print(f"They add number sum equal {sum_number}")
    print('---------------------------\n')
