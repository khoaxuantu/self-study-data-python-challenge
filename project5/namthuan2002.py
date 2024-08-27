from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import time
import datetime
import re
import pandas as pd
import schedule




def get_current_time(string):
    result = ''
    if (re.search(r'hour', string, re.I)):
        result =  datetime.datetime.now() - datetime.timedelta(hours= int(re.findall(r'\d+', string)[0]))
    elif (re.search(r'hour', string, re.I)):
        result =  datetime.datetime.now() - datetime.timedelta(hours= int(re.findall(r'\d+', string)[0]))
    elif (re.search(r'week', string, re.I)):
        result =  datetime.datetime.now() - datetime.timedelta(weeks= int(re.findall(r'\d+', string)[0]))
    elif (re.search(r'min..', string, re.I)):
        result =  datetime.datetime.now() - datetime.timedelta(minutes= int(re.findall(r'\d+', string)[0]))

    return result

def crawlData_from_ITViec(page_num=1):
    driver = uc.Chrome()
    url = "https://itviec.com/it-jobs?page=" + str(page_num) # ?job_selected=software-engineer-java-english-fortna-5335"

    driver.get(url)
    page_source = driver.page_source

    page = BeautifulSoup(page_source, "html.parser")

    jobs_cre = page.find_all('div', {"class":"job-card"})
    print(len(jobs_cre))

    jobs_info = []
    core_url = url + "&" + "job_selected="

    for j in jobs_cre:
        print("something.......")

        rear_url = j.get('data-search--job-selection-job-slug-value')

        job_url = core_url + rear_url
        print(job_url)
        driver.get(job_url)
        job_page = driver.page_source
        sub_page = BeautifulSoup(job_page, 'html.parser')

        job_link = "https://itviec.com" + j.find('a', {'data-search--job-selection-target':"jobTitle"})['href']
        label_link = 'Job link'

        job_preview_header = sub_page.find('div', class_="preview-job-header")

        try:
            job_title = job_preview_header.find('h2').get_text()
        except:
            job_title = "Cannot be found"
        label_title = "Job name"

        try:
            job_salary = sub_page.find('div', class_="job-header-info").find('span').get_text()
        except:
            job_salary = "Cannot be found"
        label_salary = 'Salary'
        # url_company = job_preview.find('a')['href']

        job_preview = sub_page.find('div', "preview-job-content")
        info = job_preview.find_all('span')

        
        label_location = "Location"
        label_type = "Type"
        label_time = "Time"
        label_skill = "Required skill"
        try:
            job_location = info[0].get_text()
        except:
            job_location = 'Cannot be found'
        
        try:
            job_type = info[1].get_text()
        except:
            job_type = 'Cannot be found'

        try:
            time_posted = info[2].get_text()
        except:
            time_posted = 'Cannot be found'
        job_time = get_current_time(time_posted)

        try:
            job_skill = job_preview.find('div', class_="d-flex align-items-center gap-1").get_text(separator=",")
        except:
            job_skill = 'Cannot be found'
        

        header = job_preview.find_all('h2')
        try:
            job_reason = job_preview.find('section', class_="reasons-join-us").get_text(separator="\n")
        except:
            job_reason = "Cannot be found"
        label_reason = header[0].get_text()
        try:    
            job_desc = job_preview.find('section', class_="job-description").get_text(separator="\n")
        except:
            job_desc = "Cannot be found"
        label_desc = header[1].get_text()
        try:
            job_exper = job_preview.find('section', class_="job-experiences").get_text(separator="\n")
        except:
            job_exper = "Cannot be found"
        label_exper = header[2].get_text()
        try:
            job_benefit = job_preview.find('section', class_="job-why-love-working").get_text(separator="\n")
        except:
            job_benefit = "Cannot be found"
        label_benefit = header[3].get_text()

        try:
            company = header[4].get_text()
        except:
            company = "Cannot be found"
        label_com = "Company"

        job_detail = [job_title, job_salary, job_location, job_type, job_time, job_skill, job_reason, job_desc, job_exper, job_benefit, company, job_link]
        label = [label_title, label_salary, label_location, label_type, label_time, label_skill, label_reason, label_desc, label_exper, label_benefit, label_com, label_link]

        jobs_info.append(dict(zip(label, job_detail)))

        time.sleep(2)
    
    return jobs_info

def job():
    try:
        df = pd.DataFrame(crawlData_from_ITViec(page_num=1) + crawlData_from_ITViec(page_num=2))
        df.to_excel(r"F:\My_Learning\Python\Challenges\List Jobs.xlsx")


        # Filter Python or SQL or C++ skill job
        df = df[df['Required skill'].apply(lambda x: True if re.search(r'python|SQL|C\+\+', x, re.I) else False)]
        # Filer on-site job
        df = df[df['Type'].apply(lambda x: True if re.search(r'(office)|(on.*site)', x, re.I) else False)]
        # Filter jobs in HCM city
        df = df[df['Location'].apply(lambda x: True if re.search(r'h.*c.*m.*', x, re.I) else False)]
        # # Filter out intern job
        df = df[df['Job name'].apply(lambda x: False if re.search(r'intern|t.*t.*s.*', x, re.I) else True)]

        df.to_excel(r"F:\My_Learning\Python\Challenges\List Jobs Filtered.xlsx")

    except:
        run_fail = True


# set end time for the process
end_time = datetime.datetime.now() + datetime.timedelta(days = 15)

schedule.every().day.at("09:00").do(job)

while True:
    now = datetime.datetime.now()
    if now >= end_time:
        print("Process stop, day 15 coming")
        break
    
    schedule.run_pending()
    time.sleep(60)
