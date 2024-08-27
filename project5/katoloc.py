from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import csv
import os, shutil
import time
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# code co the bi loi: requests.exceptions.ReadTimeout: HTTPSConnectionPool(host='www.myjobmag.co.ke', port=443): Read timed out. (read timeout=None)
# em khong tim dc cach fix nhung ma tat di de 1 luc no lai chay duoc:))

path = os.path.dirname(os.path.realpath(__file__))# lay duong dan file py nay dang o
path = path.replace("\\","/") + '/'

# xxxx@gmail.com va xxxx@gmail.com la 2 email de test
# [Reviewer] I don't care about the emails. We don't need to test them
# anh co the log de kiem tra
def send_mail():
    subject = 'JOBIT HERE WE GO'
    body = 'I am comeback! Your list Job here! Good luck!!!'
    sender_email = "xxxx@gmail.com"
    receiver_email = "xxxx@gmail.com"
    password = '<<MASK_PASSWORD>>' # Don't public the password plz

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    list_filename = ['MyJobMag.csv','Itjobpro.csv']
    list_path = [path+'Web My Job Mag'+'/MyJobMag.csv',path+'Web It Job Pro'+'/Itjobpro.csv']
    flag = 0
    for i in list_path:
        with open(i, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {list_filename[flag]}",
        )
        flag += 1
        message.attach(part)
        text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

# chuyen tu ????? ago sang date
def handle_job_date(job_date):
    digit = int(re.search(r'\d+',job_date).group())
    unit = re.search(r'\d+\s(\w+)\sago',job_date).group()
    now = datetime.now()
    if unit == 'seconds' or unit == 'second':
        second = now.second - digit
        job_date = str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(second)
    elif unit == 'mins' or unit == 'min':
        minute = now.minute - digit
        job_date = str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' ' + str(now.hour) + ':' + str(minute) + ':' + str(now.second)
    elif unit == 'hours' or unit == 'hour':
        hour = now.hour - digit
        job_date = str(now.day) + '/' + str(now.month) + '/' + str(now.year) + ' ' + str(hour) + ':' + str(now.minute) + ':' + str(now.second)
    elif unit == 'days' or unit == 'day':
        day = now.day - digit
        job_date = str(day) + '/' + str(now.month) + '/' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    elif unit == 'weeks' or unit == 'week':
        day = now.day - digit*7
        job_date = str(day) + '/' + str(now.month) + '/' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    else:
        month = now.day - digit
        job_date = str(now.day) + '/' + str(month) + '/' + str(now.year) + ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    return job_date

# Nhap cac dieu kien can loc
list_languages =[]
tmp = input('Enter programming languages (e.g., Python, JavaScript)(#:end): ')
while tmp != '#':
    list_languages.append(tmp)
    tmp = input('Enter programming languages (e.g., Python, JavaScript)(#:end): ')
list_keywords = []
tmp = input('Enter certain keywords that Jobs include (e.g., "remote", "full time")(#:end): ')
while tmp != '#':
    list_keywords.append(tmp)
    tmp = input('Enter certain keywords that Jobs include (e.g., "remote", "full time")(#:end): ')
list_exclude = []
tmp = input('Enter unwanted terms (e.g., "senior", "part time")(#:end): ')
while tmp != '#':
    list_exclude.append(tmp)
    tmp = input('Enter unwanted terms (e.g., "senior", "part time")(#:end): ')

#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"}

header = ['','Job Title','Company Name','Job Location','Date Post','Job Link','Job Description']# cac title cua table

list_url = ['https://www.myjobmag.co.ke/jobs-by-field/information-technology','https://itjobpro.com/']# link 2 web


def my_job():
    flag = 0
    for url in list_url:
        df = pd.DataFrame(columns = header)
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        tag = re.findall(r'<ul class=\"(?:job_listings|job-list)(?:\s[^\"]*)?\">(.*?)</ul>\n(\n|<div class)',page.text,re.DOTALL)#lay tat ca <li> trong <ul>
        list_link=[]
        list_folder = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]# list tat ca folder tai noi file py dang o
        # cu moi <li> lay link cua job do
        for i in re.findall(r'<a href=\"(.*?)\">[a-zA-Z]',tag[0][0],re.DOTALL):
            tmp = re.search(r'<a href=\"(.*?)$',i,re.DOTALL)#regex k tot nen loc 1 lan nx de lay dung link job
            if tmp:
                list_link.append('https://www.myjobmag.co.ke'+tmp.group()[9:])
            else:
                if len(i)<90:
                    list_link.append(i)
        if flag == 1:
            # kiem tra folder da ton tai ch va tao folder luu cac file job description va file csv
            if 'Web It Job Pro' not in list_folder:
                os.mkdir(path+'Web It Job Pro')

            for link in list_link:
                pagelink = requests.get(link)
                souplink = BeautifulSoup(pagelink.text,'html.parser')
                taglink = souplink.find('div','page-hero-content')

                job_title = taglink.find('h1').text
                job_title = job_title.replace('/','-')

                company_name = taglink.find('span','entry-company').text

                try:
                    job_location = taglink.find('a','google_map_link').text
                except:
                    job_location = "None"

                date_post = souplink.find('time').text

                job = souplink.find('div','job_description').find_all('p')
                job_des =''
                for data in job:
                    job_des = job_des + data.text + '\n'
                with open(path+'Web It Job Pro' +'/' + job_title +'.txt', 'w' , newline='',encoding='UTF8') as f:
                    f.write(job_des)

                job_link = link

                # Bo loc: # : programing language  * :job co keyword   X :job bi loai vi chua unwanted terms (cho du job co #* cung bi loai)
                note = ''
                for language in list_languages:
                    language ='\s'+language+'(\s|\()'
                    if re.search(language,taglink.text+souplink.find('div','job_description').text,re.IGNORECASE):
                        note = '#'
                for keyword in list_keywords:
                    keyword ='\s'+keyword+'(\s|\()'
                    if re.search(keyword,taglink.text+souplink.find('div','job_description').text,re.IGNORECASE):
                        note += '*'
                for exclude in list_exclude:
                    exclude ='\s'+exclude+'(\s|\()'
                    if re.search(exclude,taglink.text+souplink.find('div','job_description').text,re.IGNORECASE):
                        note = 'X'

                data = [note,job_title,company_name,job_location,handle_job_date(date_post[6:]),job_link,path+'Web It Job Pro' +'/' + job_title +'.txt']
                length = len(df)
                df.loc[length] =data
            df.to_csv(path+'Web It Job Pro'+'/Itjobpro.csv')
        else:
            # kiem tra folder da ton tai ch va tao folder luu cac file job description va file csv
            if 'Web My Job Mag' not in list_folder:
                os.mkdir(path+'Web My Job Mag')

            for link in list_link:
                pagelink = requests.get(link)
                if pagelink.status_code == 400:
                    continue
                souplink = BeautifulSoup(pagelink.text,'html.parser')
                taglink = souplink.find('ul','read-ul')

                job_title = taglink.find('span','subjob-title').text
                job_title = job_title.replace('/','-')

                company_name = re.search(r'\bat.*$',taglink.find('h1').text).group()[2:]

                job_location = taglink.find_all('span','jkey-info')[3].text

                date_post = souplink.find('div',attrs = {'id':'posted-date'}).text

                job_des = souplink.find('div','job-details').text
                with open(path+'Web My Job Mag' +'/' + job_title + '.txt', 'w' , newline='',encoding='UTF8') as f:
                    f.write(job_des)

                job_link = link

                # Bo loc: # : programing language  * :job co keyword   X :job bi loai vi chua unwanted terms (cho du job co #* cung bi loai)
                note = ''
                for language in list_languages:
                    language ='\s'+language+'(\s|\()'
                    if re.search(language,taglink.text,re.IGNORECASE):
                        note = '#'
                for keyword in list_keywords:
                    keyword ='\s'+keyword+'(\s|\()'
                    if re.search(keyword,taglink.text,re.IGNORECASE):
                        note += '*'
                for exclude in list_exclude:
                    exclude ='\s'+exclude+'(\s|\()'
                    if re.search(exclude,taglink.text,re.IGNORECASE):
                        note = 'X'

                data = [note,job_title,company_name,job_location,date_post[7:],job_link,path+'Web My Job Mag' +'/' + job_title + '.txt']
                length = len(df)
                df.loc[length] = data
            df.to_csv(path+'Web My Job Mag'+'/MyJobMag.csv')
        print(df)
        flag += 1
        df[0:0]
    send_mail()
while True:
    my_job()
    time.sleep(90000)# 1 ngay = 86400s ma time.sleep() thuong co thoi gian thuc te it hon thoi gian minh yeu cau(su lap lich cua moi he thong khac nhau)-> lay 90000
