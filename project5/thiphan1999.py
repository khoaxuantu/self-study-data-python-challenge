import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
from datetime import datetime

# Ví dụ:
# - regions = input('Chọn tên khu vực (Hồ Chí Minh | Đà Nẵng | Hà Nội |All Location): ').title()
    # Chọn Hồ Chí Minh

# - start_page = int(input("Trang bắt đầu: "))
    # - chọn trang 1

# -   end_page = int(input("Trang kết thúc: "))
    # end = chọn trang 4

# filter_jobs = input(f'Nhập từ khóa công việc muốn tiềm kiếm ở {regions} hoặc để trống: ')
    # lọc job data chọn từ khóa cở bản như: data, javascript, python

# Kết file lưu về máy với tên: Hồ Chí Minh-from 1 to 4-ngày crawling


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Referer': 'https://topdev.vn/',
        'X-Xsrf-Token': '<<TOKEN_MASK>>' # Don't hard code the token -.-
    }


def region_params(region=None):
    if region == 'Hồ Chí Minh' or region == 'Hà Nội' or region == 'Đà Nẵng':
        choose = region.title()
        regions = {
            'Hồ Chí Minh': '79',
            'Hà Nội': '01',
            'Đà Nẵng': '48'
        }
        params = {
                'region_ids': None,
                'ordering': 'newest_job',
                'page': 1,
                'page_size': 15,
                'locale': 'en_US',
                'fields[job]': 'id,title,salary,slug,company,extra_skills,skills_str,skills_arr,skills_ids,job_types_str,job_levels_str,job_levels_arr,job_levels_ids,addresses,status_display,detail_url,job_url,salary,published,refreshed,applied,candidate,requirements_arr,packages,benefits,content,features,contract_types_ids,is_free,is_basic,is_basic_plus,is_distinction',
                'fields[company]': 'tagline,addresses,skills_arr,industries_arr,industries_ids,industries_str,image_cover,image_galleries,num_job_openings,company_size,nationalities_str,skills_str,skills_ids,benefits,num_employees',
            }
        params['region_ids'] = regions[choose]
        return params
    else:
        params = {
                    'fields[job]': 'id,slug,title,salary,company,extra_skills,skills_str,skills_arr,skills_ids,job_types_str,job_levels_str,job_levels_arr,job_levels_ids,addresses,status_display,detail_url,job_url,salary,published,refreshed,applied,candidate,requirements_arr,packages,benefits,content,features,is_free,is_basic,is_basic_plus,is_distinction',
                    'fields[company]': 'slug,tagline,addresses,skills_arr,industries_arr,industries_str,image_cover,image_galleries,benefits',
                    'page': 1,
                    'locale': 'vi_VN',
                    'ordering': 'jobs_new'
                }
        return params


print('''
    Chọn khu vực:
      1: Hồ Chí Minh ('Mặc định')
      2: Hà Nội
      3: Đà Nẵng
      4: All Locations
''')


regions = input('Chọn tên khu vực (Hồ Chí Minh | Đà Nẵng | Hà Nội |All Location): ').title()
start_page = int(input("Trang bắt đầu: "))
end_page = int(input("Trang kết thúc: "))

# Hàm dùng để lấy dữ liêu api từ web
def get_json_data():
    params = region_params(regions)
    url_api = 'https://api.topdev.vn/td/v2/jobs?'
    all_job_lists = []
    for page in range(start_page, end_page + 1):
        params['page'] = page
        r = requests.get(url_api, headers=headers, params=params)
        job_lists = r.json()['data']
        all_job_lists += job_lists
    return all_job_lists

filter_jobs = input(f'Nhập từ khóa công việc muốn tiềm kiếm ở {regions} hoặc để trống: ')

# Lộc các từ khóa cơ bản như data, javascipt, python
def filter_job(list_job=get_json_data(), user=filter_jobs):
    data_job = []
    if user:
        for job in list_job:
            regex = re.compile(user, re.I)
            if regex.search(job['title']):
                data_job.append(job)
        return data_job
    else:
        return list_job


# Lấy những thông tin cần thiết từ dữ liệu API ở phía trên sau khi đã lọc
def get_job_date():
    try:
        publish_date = []
        for job in filter_job():
            dates = {
                    'job_ids': str(job['id']),
                    'title': job['title'],
                    'datetime': job['refreshed']['datetime'],
                    'is_negotiable': job['salary']['is_negotiable'],
                    'unit': job['salary']['unit'],
                    'min': job['salary']['min'],
                    'max': job['salary']['max'],
                    'currency': job['salary']['currency'],
                    'min_estimate': job['salary']['min_estimate'],
                    'max_estimate': job['salary']['max_estimate'],
                    'currency_estimate': job['salary']['currency_estimate']
            }
            publish_date.append(dates)

    # remove duplicate publish date
        a = set()
        unique_publish_date = []
        for date in publish_date:
            t = tuple(date.items())
            if t not in a:
                a.add(t)
                unique_publish_date.append(date)
    except TypeError:
        unique_publish_date = None
    return unique_publish_date

# Lấy đường link của các job để crawling thông tin của từng job
def get_detail_job_links():
    try:
        base_url = 'https://topdev.vn/detail-jobs/'
        detail_job_links = []
        for i in filter_job():
            slug = i['slug']
            job_id = str(i['id'])
            job_link = base_url + slug + '-' + job_id
            detail_job_links.append(job_link)

        # remove duplicate detail job links
        unique_detail_job_link = list(set(detail_job_links))
    except:
        unique_detail_job_link = None
    return unique_detail_job_link

# Sau khi có đường link dùng request và beatifulsoup để lấy dữ liệu. Hàm trả về danh sách job dạng dictionary
def job_information():
    jobs = []
    for detail_url in get_detail_job_links():
        res = requests.get(detail_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        job_id = re.search(r'(\d+$)', detail_url).group()
        job_title = soup.find('h1', class_='text-2xl').text
        company_name = soup.find('p', class_='my-1').text
        job_location = soup.find('div', class_='w-11/12').text
        job_description = soup.find('div', class_='prose max-w-full text-sm text-black lg:text-base').find('span').text

        year_of_experience = soup.find('div', class_='flex flex-wrap').find('div', class_='item-card-info mb-2 w-1/2 md:mb-4 md:w-full').find('a')['title']
        lists_level = soup.find('div', class_='flex flex-wrap').find('div', class_='item-card-info mb-2 w-1/2 pl-3 md:mb-4 md:w-full md:pl-0').find_all('a')

        level = [a['title'] for a in lists_level]
        levels = ', '.join(level)


        job_type = soup.find('div', class_='flex flex-wrap').find('div', class_='item-card-info mb-2 w-1/2 md:mb-4 md:w-full').find_next_sibling().find_next_sibling().find('a')['title']
        full_type = soup.find('div', class_='flex flex-wrap').find('div', class_='item-card-info mb-2 w-1/2 md:mb-4 md:w-full').find_next_sibling().find_next_sibling().find_next_sibling().find('a')['title']


        job_link = detail_url
        job_dict = {
                'job_id': str(job_id),
                'job_title': job_title,
                'company_name': company_name,
                'job_location': job_location,
                'year_of_experience': year_of_experience,
                'level': levels,
                'job_description': job_description,
                'job_type': job_type,
                'full_type': full_type,
                'job_link': job_link
            }
        jobs.append(job_dict)
    return jobs


# Tạo file csv
def create_csv():
    if get_job_date() is None or get_detail_job_links() is None:
        return 'no data'
    else:
        # tạo dataframe cho 2 dữ liệu đã lấy ở phía trên
        data_1 = pd.DataFrame(job_information())

        data_2 = pd.DataFrame(get_job_date())

        # kết nối 2 bảng dữ liệu bằng từ khóa job_id
        df = data_1.merge(data_2, how='inner', left_on='job_id', right_on='job_ids')

        # Lấy thời gian crawling thực tế
        df['web_scraping_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # dùng thời gian crawling trừ ngày giờ đăng bài ==> thời gian bài đố được đăng lên
        df['job_time_posted'] = (pd.to_datetime(df['web_scraping_date']) - pd.to_datetime(df['datetime']))


        columns = ['job_id', 'job_title', 'company_name', 'job_location',
                    'year_of_experience', 'level', 'job_description', 'job_type',
                    'full_type', 'datetime','job_link','is_negotiable', 'unit', 'min', 'max', 'currency', 'min_estimate',
                    'max_estimate', 'currency_estimate', 'web_scraping_date','job_time_posted', 'job_ids'
                ]
        # Lọc các bài đăng sớm nhất
        df = df[columns].sort_values('job_time_posted')

        # tạo file name
        filename = f"{regions}-(from {start_page} to {end_page})-{datetime.now().strftime('%d-%m-%Y %H-%M')}.csv"

        # Lưu lại file theo đường dẫn chỉ định, lưu ý encoding='utf-8' hoặc encoding='utf-8-sig' để định dạng Tiếng Việt
        df.to_csv(filename, index=False, encoding='utf-8-sig')

        print(f"Created {filename} Successful!")

create_csv()
# Thay đổi thời gian theo ý muốn
# schedule.every().hour.do(region_params)
# schedule.every().hour.do(filter_job)
# schedule.every().hour.do(get_json_data)
# schedule.every().hour.do(get_job_date)
# schedule.every().hour.do(get_detail_job_links)
# schedule.every().hour.do(job_information)
# schedule.every().hour.do(create_csv)

# run = True
# try:
#     while run:
#         schedule.run_pending()
#         time.sleep(1)
# except KeyboardInterrupt:
#     print("Script interrupted and stopped.")
