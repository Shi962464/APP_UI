import os
import time

def clear_result_file(path='data.txt'):
    if os.path.exists(path):
        os.remove(path)
    else:
        with open(path, 'a') as f:
            f.write('')

def append_result(success: bool, count: int, path='data.txt'):
    with open(path, 'a') as f:
        status = "升级成功" if success else "升级失败"
        f.write(f"第{count}次{status}\t时间为{time.strftime('%Y-%m-%d %H-%M-%S')}\n")
