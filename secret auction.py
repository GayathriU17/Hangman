

name=input('What is your name?')
amount=input("What's your bid?")
dict={}
dict[name]=amount



ch=input('Do you have one more person to bid? Type "y" for yes and "n" for no.').lower()
while(ch=='y'):
  name=input('What is your name?')
  amount=input("What's your bid?")
  
  dict[name]=amount
  
  
print(dict)
