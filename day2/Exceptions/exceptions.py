import re
class InvalidLoginException(Exception):
    pass

class InvalidPasswordException(Exception):
    pass

def inputLogin() -> str:
    login=input("Veuillez entrer un login SVP (celui-ci ne doit posséder que des lettres minuscules) :");
    if re.search('[^a-z]', login) != None:
        raise InvalidLoginException("Il ne doit y avoir que des minuscules dans le login !");
    return login

def inputPassword() -> int:
    password=input("Veuillez entrer un mot de passe SVP (celui-ci ne doit posséder que des chiffres) :")    ;
    if re.search('[^0-9]', password) != None:
        raise InvalidPasswordException("Le mot de passe ne doit posséder que des nombres !");
    return password
    
missing_data=True
while missing_data:
    missing_data=False
    try:
        login = inputLogin()
    except InvalidLoginException as ile:
        missing_data=True
        print(ile)
    try:
        password = inputPassword()
    except InvalidPasswordException as ipe:
        missing_data=True
        print(ipe)

print(f"login: {login}, password: {password}")

