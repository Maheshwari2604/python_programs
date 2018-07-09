import smtplib
 
# list of email_id to send the mail
li = ["musky1999@gmail.com"]
 
for i in range(len(li)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("maheshwarishivam2604@gmail.com", "maheshwari@2604")
    message = "Message through a python program"
    s.sendmail("maheshwarishivam2604@gmail.com", li[i], message)
    s.quit()
