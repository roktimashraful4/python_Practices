# Function
#types of function 
# build-in function 
# User define function
# function arguments 
# default arguments
# required arguments
# arguments keywords


def sum_of_sum(number1,number2=3): #default arguments
    print(number1+number2)


sum_of_sum(4,5)

sum_of_sum(3)

def sent_email(to,sub,body,cc=''):
    # There are the code of email send 
    subject = sub
    New_to = to
    New_body = body
    cc = cc
    print("Send Successful"+" "+ New_to)


def No_Aur(a): 
    print(a)



sent_email(
    cc="support@roktim.com",
    body="Invoice",
    to="There are a Invoice",
    sub="dfgdfg"
    )

sent_email("info@roktim.com","Invoice","There are a Invoice")
sent_email("others@roktim.com","Invoice","There are a Invoice")


sum_of_sum("Roktim","Ashraful")
