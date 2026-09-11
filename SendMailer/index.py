import csv
import smtplib
from email.message import EmailMessage
from config import gmail ,app_password
class MailSender:
    def __init__(self):
       self.large=[];
       self.small=[]
    
    def ReadCSVFile(self):
        with open('company.csv' ,'r') as file:
         read=csv.DictReader(file);
         for data in read:
            if(data['company_size']=="Large"):
                if(data['email']!=None):
                    company= {
                        'company_name':data['company_clean'],
                        'Company_Email':data['email'],
                        'hrName':data['person_name'],
                        'gender':data['gender'],
                        'company':data['company_clean'],
                    }
                    self.large.append(company)
            else:
                company= {
                        'company_name':data['company_clean'],
                        'Company_Email':data['email'],
                        'hrName':data['person_name'],
                        'gender':data['gender'],
                        'company':data['company_clean'],
                    }
                self.small.append(company) 
    def GetLargeCompanyData(self):
        return self.large;
    
    def GetsamllCompanydata(self):
        return self.small;
    
    def SendEmailLargeCompany(self ,body ,receiver):
        message=EmailMessage();
        message['Subject']="Application for Frontend Developer Internship / Junior Opportunity";
        message['From']=gmail
        message['To']=receiver;
        message.set_content(body)
        
        with open ('manish_kumar.pdf','rb') as mr:
            resume=mr.read();
        message.add_attachment(resume,maintype="application",subtype="pdf",filename="resume.pdf")
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(gmail,app_password);
            server.send_message(message)
        return "Successfully send"
    

    def SendEmailSmallCompany(self  ,body ,receiver):
        message=EmailMessage();
        message['Subject']="Application for Frontend Developer / Junior Developer Position";
        message['From']=gmail
        message['To']=receiver;
        message.set_content(body)
        
        with open ('manish_kumar.pdf','rb') as mr:
            resume=mr.read();
        message.add_attachment(resume,maintype="application",subtype="pdf",filename="resume.pdf")
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(gmail,app_password);
            server.send_message(message)
        return "Successfully send"