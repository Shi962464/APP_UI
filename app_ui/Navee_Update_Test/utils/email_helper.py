from app_ui.fromemail  import Email  # 假设你已有封装

def send_error_email(msg='升级过程异常'):
    Email(msg)
