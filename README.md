# JobPostings
# Selenium Project to notify job openings

#Create a virtual environment
python3 -m venv <name>

#Activate the virtual environment
source <name>/bin/activate

#Clone the git repository
git clone <git-repository-url>

#Get inside the folder
cd JobPostings

#Install all the requirements
pip install -r requirements.txt

#Run the script
python linkedin_alert.py --from_email @gmail.com --to_email @gmail.com

#Enter the password
Enter Gmail App Password for @gmail.com:
*(You won’t see the characters as you type — that’s expected and secure.)*

#Deactivate the environment
deactivate
