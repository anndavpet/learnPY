def check_password(s, chars="$%!?@#"):
    flag = False
    if len(s) >= 8:
        flag = True
        for i in chars:
            if i in s:
                flag = True
                break
            else:
                flag = False
    return flag
