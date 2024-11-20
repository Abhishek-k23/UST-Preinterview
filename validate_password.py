import re

def is_valid_password(password):
    #Password Critesria

    if len(password) < 6 or len(password) > 12:
        return False
    
    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'[0-9]', password):
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[$|#|@]', password):
        return False
    
    return True

def validate_passwords(input_passwords):
    #validate and return which are valid

    passwords = input_passwords.split(',')
    valid_passwords = [password for password in passwords if is_valid_password(password)]
    return ','.join(valid_passwords)


if __name__ == "__main__":
    input_passwords = "asqwr1234@1,aF145#,2w3E*,2We3345"
    print(validate_passwords(input_passwords))
