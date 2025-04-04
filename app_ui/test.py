from fromemail import Email

def divide_numbers(a, b):
    return a / b

try:
    # 调用时，传递除数为零，导致 ZeroDivisionError
    result = divide_numbers(10, 0)
    print(result)
except Exception as e:
    # 发送邮件时传递错误信息
    Email(f"发生错误: {e}")
