print("Please input two number,and I will add them then return for you.")
first_num = input('first number:')
second_num = input('second number:')
try:
    sum_number = int(first_num) + int(second_num)
except ValueError:
    print("请输入两个数字而不是其他符号。")
else:
    print(f"They add number sum equal {sum_number}")
print('---------------------------\n')
