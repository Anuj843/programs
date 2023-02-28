letter='''Dear <|NAME|>
We are glad to give you an oppurtunity to work with us
Please reply your answer with in 24hrs
Date:<|DATE|>
'''
identity=input("Enter your name\n")
today=input("Enter date\n")
letter=letter.replace("<|NAME|>", identity)
letter=letter.replace("<|DATE|>", today)
print(letter)