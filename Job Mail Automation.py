import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# Email details
gmail_user = "atulat1996@gmail.com"
gmail_password = ""
recipient = ""
subject = "Application for Data Science / Machine Learning cum Python Developer position"

# Load body template from string
body_template = """Dear Hiring Manager,

I am excited to express my interest in the Data Science / Machine Learning cum Python Developer position at your company. As a recent intern in ML for 6 months and a certified data scientist with a strong background in computer science, I am confident in my ability to contribute to your team's success.

During my internship, I worked on several ML projects, including developing a recommendation system and performing sentiment analysis on customer reviews. I also gained experience in data preprocessing, feature engineering, and model evaluation.

In addition to my ML skills, I have a strong proficiency in Python and have worked on various projects using libraries such as NumPy, Pandas, and Scikit-learn. I am passionate about solving complex problems and always eager to learn and apply new technologies.

I have attached my resume to this email. I look forward to discussing how I can contribute to your team.

Sincerely,
Atul A T
"""

# Substitute placeholders in body template with actual values
body = body_template.format()

# Attachment details
attachment_path = "/Users/atulat/Desktop/Work/Atul_Resume_ML_PD.pdf" # escape the pipe character

# Compose email
msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = recipient
msg['Subject'] = subject

# Add body to email
msg.attach(MIMEText(body, 'plain'))

# Add attachment to email
attachment = open(attachment_path, "rb")
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(attachment_path))
msg.attach(p)

# Send email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(gmail_user, gmail_password)
text = msg.as_string()
server.sendmail(gmail_user, recipient, text)
server.quit()
print('Email sent successfully!')
