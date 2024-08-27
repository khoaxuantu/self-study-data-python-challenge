import discord
from discord.ext import tasks, commands
from dataclasses import dataclass
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import csv
import schedule
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = 1275160630025916601
MAX_SESSION_TIME_MINUTES = 45

@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
session = Session()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command. Please check and try again.")
    else:
        await ctx.send(f"Error: {error}")

@bot.event
async def on_ready():
    print("Hello! Find Job bot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! Find Job bot is ready!")

@bot.command(name='start')
async def load_all_jobs(ctx):
    channel = bot.get_channel(CHANNEL_ID) if CHANNEL_ID else ctx.channel
    job_data = scrape_jobs()
    if job_data:
        await channel.send(f"Found {len(job_data)} jobs:\n\n")
        for job in job_data:
            embed = discord.Embed(title=job['Job Title'], url=job['Job Link'], color=0x00ff00)
            embed.add_field(name="Company", value=job['Company Name'], inline=False)
            embed.add_field(name="Location", value=job['Job Location'], inline=False)
            embed.add_field(name="Salary", value=job['Salary'], inline=False)
            embed.add_field(name="Date posted", value=job['Date posted'], inline=False)
            embed.add_field(name="Application Deadline", value=job['Application Deadline'], inline=True)
            await channel.send(embed=embed)
    else:
        await channel.send("No jobs found.")

def scrape_jobs():
    job_data = []
    i = 1
    while True:
        print(f'Getting page, {i}')
        soup = extract(i)
        new_job_data = transform(soup)
        if not new_job_data:
            break
        job_data.extend(new_job_data)
        i += 1
    return job_data

def extract(page):
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    url = f"https://careerviet.vn/viec-lam/Data-Analyst-k-trang-{page}-vi.html"
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()
    return soup

def transform(soup):
    job_data = []
    job_find = soup.find(class_="no-search")
    if job_find:
        return job_data
    else:
        job_results_div = soup.find(id="jobs-side-list-content")
        job_listings = job_results_div.find_all(class_="job-item")
        for job in job_listings:
            job_title_element = job.find('a', class_='job_link')
            job_title = job_title_element.contents[0].strip()
            job_link_tag = job.find(class_="job_link")
            job_link = job_link_tag.get("href")
            company_name_element = job.find(class_="company-name")
            company_name = company_name_element.text
            job_location_element = job.find(class_="location")
            job_location_tag = job_location_element.find_all('li')
            job_location = ' | '.join([li.text.strip() for li in job_location_tag])
            job_salary_element = job.find(class_="salary")
            job_salary = job_salary_element.text
            job_date_element = job.find(class_="time")
            job_date = job_date_element.find('time').text.strip()
            application_deadline_element = job.find(class_="expire-date")
            application_deadline = application_deadline_element.text
            job_data.append({
                'Job Title': job_title,
                'Job Link': job_link,
                'Company Name': company_name,
                'Job Location': job_location,
                'Salary': job_salary,
                'Date posted': job_date,
                'Application Deadline': application_deadline
            })
        return job_data

bot.run('<<TOKEN_MASK>>') # Don't hard code your token bruh -_-

schedule.every().day.at("06:00").do(scrape_jobs)
while True:
    schedule.run_pending()
    time.sleep(60)
