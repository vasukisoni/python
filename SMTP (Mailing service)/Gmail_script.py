import smtplib

# ------  Sender\'s Email ID 
fromaddr = input('Enter the Sender\'s Email ID = ')

# ------  Reciever\'s Email ID
toaddr = input('Enter the reciever\'s Email ID = ')

#---------  Message Box
msg = 'Hello , This is Vasuki Soni'

# Once that is done, create a SMTP object which is going to be used
#for connection with the server.

server = smtplib.SMTP("smtp.gmail.com:587")

#Next, we will use the starttls() function which is required by Gmail.

server.starttls()

#Next, log in to the server:

username = input('Username')
password = input('Password')

server.login(username,password)

# Then, we will send the email:

server.sendmail(fromaddr, toaddr, msg)

server.quit()

# ------------------------------ END ----------------------------
