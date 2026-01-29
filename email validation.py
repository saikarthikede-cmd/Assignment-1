#task 5
import re
def validate(emails):
    pattern=r'^[\w_]+@[\w]+\.\w{2,4}'
    return bool(re.match(pattern,email)) #match is used to compare pattern and email
emails=["user@example.com", "invalidemail.von", "ttg@domaitest_123n.co.uk.bn", "t@nodomain.com"]
for email in emails:
    if validate(email):
        print("Valid Email")
    else:
        print("Invalid Email")
