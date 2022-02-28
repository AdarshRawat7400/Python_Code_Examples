import re

def verify_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if(re.fullmatch(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")
 

verify_email("adarshrawat71@gmail.com")
verify_email("adarshrawat71@gmail")
verify_email("adarsmail.com")
verify_email("ram@gmail.com")


#Output:-
#Valid Email
#Invalid Email
#Invalid Email
#Valid Email
