from config import gmail,app_password
from index import MailSender


send=MailSender();
send.ReadCSVFile()

large=send.GetLargeCompanyData()
small=send.GetsamllCompanydata();

def SmallCompanyhelperfun(hrName ,gender ,company_clean):
    if gender == "male":
        greeting = f"Dear {hrName} Sir,"
    elif gender == "female":
        greeting = f"Dear {hrName} Mam,"
    else:
        greeting = "Dear Sir/Mam,"

    return f"""
{greeting}

My name is Manish Kumar, and I am interested in exploring Frontend Developer or Junior Developer opportunities at {company_clean}.

I have professional experience in Laravel/PHP and hands-on experience developing frontend projects using React.js, JavaScript, HTML,

CSS, and Tailwind CSS. I am also currently learning Next.js through my personal projects.One of my main projects is DebugDuel, an IT

learning and coding platform that I have developed and deployed as a practical full-stack project.I would appreciate it if you could

let me know about any suitable Frontend Developer or Junior Developer openings at {company_clean} where my skills and experience could

be a good fit.

GitHub: https://github.com/Manish9582

I have attached my resume for your consideration.

Thank you for your time.

Best regards,
Manish Kumar
New Delhi, India
+91 9582747332
mk5758029@gmail.com
    """

def LargeCompanyhelperfun(hrName ,gender ,company_clean):
    if gender == "male":
        greeting = f"Dear {hrName} Sir,"
    elif gender == "female":
        greeting = f"Dear {hrName} Mam,"
    else:
        greeting = "Dear Sir/Mam,"

    return f"""
{greeting}

My name is Manish Kumar, and I am interested in exploring a Frontend Developer Internship or suitable Junior Developer opportunity

at {company_clean}.I have professional experience in Laravel/PHP and hands-on experience building frontend projects using React.js, 

JavaScript, HTML, CSS, and Tailwind CSS. I am also currently learning Next.js through my personal projects.I have built and deployed

my own project, DebugDuel, an IT learning and coding platform, which has given me practical experience in developing real-world web 

applications.I would be grateful if you could consider my profile for any relevant internship or junior-level frontend opportunity at

{company_clean}.

GitHub: https://github.com/Manish9582

I have attached my resume for your consideration.

Thank you for your time.

Best regards,
Manish Kumar
New Delhi, India
+91 9582747332
mk5758029@gmail.com
    """

for sml in small:
    print("Small Comapny",sml)      
    help=SmallCompanyhelperfun(sml['hrName'],sml['gender'],sml['company'])
    sendEmail=send.SendEmailSmallCompany(help,sml['Company_Email'])
    print(sendEmail)
    
    
for lrg in large:
    print("Large Comapny",lrg)        
    help=LargeCompanyhelperfun(lrg['hrName'],lrg['gender'],lrg['company'])
    sendEmail=send.SendEmailLargeCompany(help,lrg['Company_Email']);
    print(sendEmail)