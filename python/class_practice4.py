class Account:
    def __init__(self,user_name,balance=0):
        self.user_name=user_name
        self.balance=balance
s1=Account("barun_basnet")
print(s1.balance,s1.user_name)