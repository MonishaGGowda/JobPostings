# JobPostings
# Selenium Project to notify job openings

## Features

- ⏰ Checks every hour (configurable)
- 📧 Sends Gmail email alerts
- 🔒 Secure password input (no plain-text passwords)
- 🧠 Avoids sending duplicates
- 🧹 Runs headless (no browser popup)

  
## 🛠 Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver (automatically managed via `webdriver-manager`)

## Steps

**Create a virtual environment**
---
python3 -m venv <name>

**Activate the virtual environment**
---
source <name>/bin/activate

**Clone the git repository**
---
git clone <git-repository-url>

**Get inside the folder**
---
cd JobPostings

**Install all the requirements**
---
pip install -r requirements.txt

**Run the script**
---
python linkedin_alert.py --from_email @gmail.com --to_email @gmail.com

**Enter the password**
---
Enter Gmail App Password for @gmail.com:

*(You won’t see the characters as you type — that’s expected and secure.)*

**#Deactivate the environment**
---
deactivate

### 💡 Optional Enhancements

Here are useful add-ons you can integrate into the script:

| Feature                             | Description                                                                 | How to Add                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------|
| ⏰ **Time-based Scheduling**         | Only check between 9 AM and 6 PM                                           | Use Python's `datetime.now().hour` to skip checks outside working hours    |
| 🧾 **Log job links to a file**       | Keep a record of job links that triggered notifications                    | Use Python’s `open("log.txt", "a")` or `csv.writer()` for `.csv` logging   |
| 🧪 **One-shot Mode**                 | Run the script once and exit                                               | Replace `while True:` loop with a single `check_new_jobs()` call           |
| 🔄 **Run on Boot**                  | Start script automatically with system                                     | Use Task Scheduler (Windows) or `crontab` (Linux/macOS)                    |
| 🧠 **Daily Summary Email**          | Send one email daily with all jobs found                                   | Use `schedule` or `cron` and store job entries in a list throughout the day |
| 🐳 **Docker Support**               | Containerize the job tracker for deployment                                | Write a `Dockerfile` with Python + Chrome + dependencies                   |
| 🔇 **Sound Alert or Popup**         | Play sound or show popup when new jobs found                               | Use `playsound` or `plyer.notification`                                    |
| 📊 **Google Sheets Logging**        | Save job links in a live Google Sheet                                      | Use `gspread` and Google Sheets API                                        |
| 🌐 **Track Multiple URLs**          | Monitor various job roles or regions at once                               | Store multiple `LINKEDIN_URL`s in a list and loop over them                |
