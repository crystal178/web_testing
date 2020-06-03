# 正常场景的数据
normal_data = {"user": "1303845892@qq.com", "passwd": "nmb_python"}

# 异常场景的数据
incorrect_datas = [
    {"user": "1303845892@qq.com", "passwd": "", "check": "密码不能为空"},
    {"user": "", "passwd": "nmb_python", "check": "账号不能为空"},
    {"user": "34", "passwd": "nmb_python", "check": "用户不存在"}
]
