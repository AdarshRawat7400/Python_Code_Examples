
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
print("Authenticating...")
s.login("adarshrawat71@gmail.com", "Helloworld@123")
print("Login Successful")

# message to be sent
print("Message fetching... from file") 
message = ""
for line in open("message.txt", "r"):
    message += line



# sending the mail
s.sendmail("adarshrawat71@gmail.com", "adarshrawat2763@gmail.com", message)

print("Successfully sent email")
# terminating the session
s.quit()
