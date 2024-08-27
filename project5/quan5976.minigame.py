import discord
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import re
from datetime import datetime
from discord.ext import tasks, commands

intents = discord.Intents.default()
intents.message_content = True  # Kích hoạt quyền truy cập nội dung tin nhắn

bot = commands.Bot(command_prefix='gento!', intents=intents)

# Biến toàn cục để lưu trữ ID kênh
selected_channel_id = None

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name="Ready to find jobs!"))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Lệnh không hợp lệ. Vui lòng kiểm tra và thử lại.")
    else:
        await ctx.send(f"Đã xảy ra lỗi: {error}")

@bot.command(name='set_channel')
async def set_channel(ctx, channel_id: int):
    global selected_channel_id
    selected_channel_id = channel_id
    channel = bot.get_channel(selected_channel_id)
    if channel:
        await ctx.send(f"Bot đã được thiết lập để hoạt động trong kênh {channel.name}.")
    else:
        await ctx.send("Không tìm thấy kênh. Vui lòng kiểm tra ID kênh.")

@bot.command(name='filter')
async def filter_jobs(ctx, keyword: str, order: str = None):
    channel = bot.get_channel(selected_channel_id) if selected_channel_id else ctx.channel
    jobs = scrape_jobs(keyword=keyword)
    if jobs:
        if order:
            jobs = sort_jobs_by_salary(jobs, order)
        await channel.send(f"Found {len(jobs)} jobs matching keyword '{keyword}':\n\n")
        for job in jobs:
            embed = discord.Embed(title=job['Job Title'], url=job['Job Link'], color=0x00ff00)
            embed.add_field(name="Company", value=job['Company Name'], inline=False)
            embed.add_field(name="Location", value=job['Location'], inline=False)
            embed.add_field(name="Posted", value=job['Date Posted'], inline=True)
            embed.add_field(name="Salary", value=job['Salary'], inline=True)
            embed.add_field(name="Skills", value=job['Skills'], inline=False)
            await channel.send(embed=embed)
    else:
        await channel.send(f"No jobs found matching keyword '{keyword}'.")

@bot.command(name='filter_date')
async def filter_jobs_by_specific_date(ctx, specific_date: str, order: str = None):
    channel = bot.get_channel(selected_channel_id) if selected_channel_id else ctx.channel
    jobs = scrape_jobs(specific_date=specific_date)
    if jobs:
        if order:
            jobs = sort_jobs_by_salary(jobs, order)
        await channel.send(f"Found {len(jobs)} jobs posted on {specific_date}:\n\n")
        for job in jobs:
            embed = discord.Embed(title=job['Job Title'], url=job['Job Link'], color=0x00ff00)
            embed.add_field(name="Company", value=job['Company Name'], inline=False)
            embed.add_field(name="Location", value=job['Location'], inline=False)
            embed.add_field(name="Posted", value=job['Date Posted'], inline=True)
            embed.add_field(name="Salary", value=job['Salary'], inline=True)
            embed.add_field(name="Skills", value=job['Skills'], inline=False)
            await channel.send(embed=embed)
    else:
        await channel.send(f"No jobs found on {specific_date}.")

@bot.command(name='start')
async def load_all_jobs(ctx, order: str = None):
    channel = bot.get_channel(selected_channel_id) if selected_channel_id else ctx.channel
    jobs = scrape_jobs()
    if jobs:
        if order:
            jobs = sort_jobs_by_salary(jobs, order)
        await channel.send(f"Found {len(jobs)} jobs:\n\n")
        for job in jobs:
            embed = discord.Embed(title=job['Job Title'], url=job['Job Link'], color=0x00ff00)
            embed.add_field(name="Company", value=job['Company Name'], inline=False)
            embed.add_field(name="Location", value=job['Location'], inline=False)
            embed.add_field(name="Posted", value=job['Date Posted'], inline=True)
            embed.add_field(name="Salary", value=job['Salary'], inline=True)
            embed.add_field(name="Skills", value=job['Skills'], inline=False)
            await channel.send(embed=embed)
    else:
        await channel.send("No jobs found.")

def scrape_jobs(keyword=None, specific_date=None):
    driver = webdriver.Chrome()
    filtered_jobs = []
    today_str = datetime.today().strftime('%d/%m/%Y')

    for page in range(1, 21):  # Thu thập trong 2 trang đầu tiên
        driver.get(f'https://www.vietnamworks.com/viec-lam?q=it&page={page}')
        sleep(3)
        web = driver.page_source
        soup = BeautifulSoup(web, 'html.parser')
        job_data = soup.find('div', class_='block-job-list')
        if job_data:
            job_items = job_data.find_all('div', class_='sc-fwwElh iAsyDt')
            for job in job_items:
                try:
                    job_title = job.find('h2').text.strip() if job.find('h2') else None
                    company_name = job.find('div', class_='sc-hybRYi iVjhps').text.strip() if job.find('div', class_='sc-hybRYi iVjhps') else None
                    location = job.find('span', class_='sc-evdWiO hRDCRg').text.strip() if job.find('span', class_='sc-evdWiO hRDCRg') else None
                    date_posted = job.find('div', class_='sc-lmJFLr eJkRTg').text.strip() if job.find('div', class_='sc-lmJFLr eJkRTg') else None
                    salary = job.find('span', class_='sc-gQSkpc cXNeHq').text.strip() if job.find('span', class_='sc-gQSkpc cXNeHq') else 'Thương lượng'
                    skills = job.find_all('label', class_='sc-dxcDKg RKGYC sc-ERObt jKzuwy')
                    list_skills = [skill.text for skill in skills]
                    job_link = "https://www.vietnamworks.com" + job.find('a', href=True)['href'] if job.find('a', href=True) else None

                    # Định dạng ngày "Hôm nay" về ngày hiện tại
                    if date_posted == "Hôm nay":
                        date_posted = today_str

                    # Điều kiện tìm kiếm với từ khóa
                    if keyword and not re.search(r'\b' + keyword + r'\b', job_title, re.IGNORECASE):
                        continue

                    # Điều kiện tìm kiếm theo ngày cụ thể
                    if specific_date and date_posted != specific_date:
                        continue

                    filtered_jobs.append({
                        'Job Title': job_title,
                        'Company Name': company_name,
                        'Location': location,
                        'Date Posted': date_posted,
                        'Salary': salary,
                        'Skills': ', '.join(list_skills),
                        'Job Link': job_link
                    })
                except Exception as e:
                    print(f"Error processing job: {e}")
    driver.quit()
    return filtered_jobs

def extract_salary(salary):
    try:
        salary_range = re.findall(r'\d+', salary.replace(',', ''))
        if len(salary_range) == 2:
            return (int(salary_range[0]) + int(salary_range[1])) / 2
        elif len(salary_range) == 1:
            return int(salary_range[0])
    except:
        return 0
    return 0

def sort_jobs_by_salary(jobs, order):
    jobs_with_salary = [job for job in jobs if job['Salary'] != 'Thương lượng']
    jobs_with_salary.sort(key=lambda job: extract_salary(job['Salary']), reverse=(order.lower() == 'desc'))

    jobs_without_salary = [job for job in jobs if job['Salary'] == 'Thương lượng']
    return jobs_with_salary + jobs_without_salary

bot.run('<<DISCORD_TOKEN_MASK>>') # Don't hard code your token bruh -_-


# Thiết lập kênh để bot gửi tin nhắn:

# Lệnh: gento!set_channel <channel_id>
# Ví dụ: gento!set_channel 123456789012345678
# Mô tả: Bot sẽ được thiết lập để gửi tin nhắn vào kênh có ID là 123456789012345678.
# Tìm kiếm theo từ khóa và sắp xếp theo lương:

# Lệnh: gento!filter <keyword> <order>
# Ví dụ: gento!filter IT desc
# Mô tả: Tìm kiếm các công việc có chứa từ khóa "IT" trong tiêu đề và sắp xếp theo lương giảm dần. Nếu không cung cấp thứ tự, mặc định sẽ không sắp xếp theo lương.
# Tìm kiếm theo ngày cụ thể và sắp xếp theo lương:

# Lệnh: gento!filter_date <specific_date> <order>
# Ví dụ: gento!filter_date 19/08/2024 desc
# Mô tả: Tìm kiếm các công việc được đăng vào ngày 19/08/2024 và sắp xếp theo lương giảm dần. Nếu không cung cấp thứ tự, mặc định sẽ không sắp xếp theo lương.
# Tìm kiếm tất cả công việc và sắp xếp theo lương:

# Lệnh: gento!start <order>
# Ví dụ: gento!start asc
# Mô tả: Tìm kiếm tất cả các công việc và sắp xếp theo lương tăng dần. Nếu không cung cấp thứ tự, mặc định sẽ không sắp xếp theo lương.
# Xử lý lỗi khi lệnh không hợp lệ:

# Mô tả: Nếu bạn nhập một lệnh không hợp lệ, bot sẽ trả về thông báo: "Lệnh không hợp lệ. Vui lòng kiểm tra và thử lại."
