def is_password_good(password):
    sum = 0
    if len(password) >= 8:
        sum += 1
        for i in range(len(password)):
            if password[i] in '0123456789':
                continue
            if password.upper()[i] in password[i]:
                sum += 1
                break
        for i in range(len(password)):
            if password.lower()[i] in password[i]:
                sum += 1
        for i in range(len(password)):
            if password[i] in '0123456789':
                sum += 1
    if sum >= 4:
        return True
    else:
        return False

txt = input()

print(is_password_good(txt))