# == START OF PROGRAM DETAILS == #
###
#   NAME: EMAIL SLICER
#   SHORT_DISC: The email slicer is a handy program to get the username and domain name from an email address.
#   You can customize and send a message to the user with this information.
#   PARAMS: email - str EX: asaeed@bisak.org
#   LIBRARIES/DEPENDENCIES: re
###
# == END OF PROGRAM DETAILS == #

# == VALIDATION ==
#    - Any input of any case is valid >> DONE
# == VALIDATION ==

import re
regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

# email = input("Enter your email: ")
email = "asaeed@bisak.org"

def validate():
    global email
    validateStatus = re.match(regex, email)

    if validateStatus == False:
        print("Incorrect email format, please try again!")
        email = input("Enter your email: ")

def getUsernameAndGetDomainName():
    global email
    return print("Email Username: " + email.split("@")[0] + "\nEmail Domain: " + email.split("@")[1])

validate()
getUsernameAndGetDomainName()