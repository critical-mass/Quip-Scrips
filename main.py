from ast import Return
from urllib import response
from quip_remove_user import remove_user
from quip_add_users import add_user

decision=""
email=""
nickName=""
lastName=""
message = os.environ['client_payload.message']
print(message)
      
def main(decision, email, nickName, lastName):
    if decision == "onboard":
        add_user(nickName, lastName, email)
    elif decision == "offboard":
        remove_user(email)
    else:
        print("no way my guy")
