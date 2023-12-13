#https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023/train/python
import re
def validate_usr(username):
    return re.match("[^\w{4-16}]", username)
print(validate_usr("mr_choung"))