from fromemail import Email

def divide_numbers(a, b):
    return a / b

try:
    # ����ʱ�����ݳ���Ϊ�㣬���� ZeroDivisionError
    result = divide_numbers(10, 0)
    print(result)
except Exception as e:
    # �����ʼ�ʱ���ݴ�����Ϣ
    Email(f"��������: {e}")
