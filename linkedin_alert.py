import argparse
import getpass
from email.mime.text import MIMEText
import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# === Parse command-line arguments ===
parser = argparse.ArgumentParser(description="LinkedIn Job Monitor with Secure Email")
parser.add_argument("--from_email", required=True, help="Sender's Gmail address")
parser.add_argument("--to_email", required=True, help="Receiver's email address")
args = parser.parse_args()

# === Secure password prompt ===
EMAIL_PASSWORD = getpass.getpass("Enter Gmail App Password for {}: ".format(args.from_email))

# === Config ===
FROM_EMAIL = args.from_email
TO_EMAIL = args.to_email
LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?currentJobId=4186477202&distance=25.0&f_TPR=r86400&geoId=103644278&keywords=internship&origin=JOB_SEARCH_PAGE_JOB_FILTER"
CHECK_INTERVAL = 3600  # seconds (1 hour)
sent_jobs = set()

# === Send Email ===
def send_email(subject, body):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(FROM_EMAIL, EMAIL_PASSWORD)
        smtp.send_message(msg)

# === Scrape LinkedIn Jobs ===
def check_new_jobs():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run browser in background
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(LINKEDIN_URL)
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        jobs = soup.find_all('li', {'class': 'jobs-search-results__list-item'})

        new_jobs = []

        for job in jobs:
            link_tag = job.find('a', href=True)
            title_tag = job.find('span', class_='sr-only')

            if link_tag and title_tag:
                job_title = title_tag.get_text(strip=True)
                job_link = "https://www.linkedin.com" + link_tag['href'].split("?")[0]

                if job_link not in sent_jobs:
                    new_jobs.append((job_title, job_link))
                    sent_jobs.add(job_link)

        if new_jobs:
            body = "<h3>📌 New LinkedIn Internships (Last 24h)</h3>"
            for title, link in new_jobs:
                body += f"<p><b>{title}</b><br><a href='{link}'>{link}</a></p>"
            send_email("🎯 New LinkedIn Internships Found", body)
            print(f"✅ Email sent with {len(new_jobs)} job(s).")
        else:
            print("⏳ No new jobs found.")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        driver.quit()

# === Loop Forever ===
while True:
    check_new_jobs()
    time.sleep(CHECK_INTERVAL)
