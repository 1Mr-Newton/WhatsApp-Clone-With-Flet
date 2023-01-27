from model import *
def auth():
  choice = input('Welcome to WhatsApp\n1: Create account\n2: Sign in\n')
  if choice == '1':
    username = input('Please enter your username\n')
    password = input('Please enter your password\n')
    u = session.query(User).filter_by(username=username).first()
    if u == None:
      u =  User(username=username,password=password)
      session.add(u)
      session.commit()
    else:
      print('username:',u.username,',already exists\nPlease log in')  


  elif choice == "2":
    username = input('Please enter your username\n')
    password = input('Please enter your password\n')
    u = session.query(User).filter_by(username=username).first()
    if u and u.password == password:
      print('Logged in')
    else:
      print('Wrong password')  