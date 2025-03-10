# INTERMEDIATE PYTHON  (day 17) (06.03.25) (3rd assignment)
# Assignment -- HOW TO SEND REAL TIME MAIL USING PYTHON (give it in repository)

import smtplib
import random


def read_data_send_mail():
    
    try:
        # f = open("student_mails.txt","x")
        # print("file created successfully")
        
        f = open("D:\Python Codes\Besant Technology\student_mails.txt","r")
        student_mails=f.read()
        
        student_mails = student_mails.split(",")
        print(student_mails)
        
    except:
        print("file not available")
        
    sender_email = "sneha.snehamayee@gmail.com"
    
    for i in student_mails:
        otp_number = random.randint(00000,99999)
        # print(f"OTP Number for {i} is : {otp_number}")
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(sender_email,"ztkg kemb qpnm cgys")
        message = f"Hi your OTP number is {otp_number}"
        
        try:
            s.sendmail(sender_email,i,message)
            print("Mail send successfully")
            print(f"OTP Number for {i} is : {otp_number}")
            s.quit()
            
        except:
            print("Mail not sent..")
read_data_send_mail()