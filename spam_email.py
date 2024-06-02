import smtplib, os, json, time, shutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from content import email_subject, email_text

class WorkinWithFile:

    def examination():
        if not os.path.exists('Done'):
            os.makedirs('Done')
        if not os.path.exists('Collented'):
            os.makedirs('Collected')
        if not os.path.exists('Trash'):
            os.makedirs('Trash')

    def removeDirs():    
        time.sleep(3)
        os.removedirs('Done')
        os.removedirs('Collected')

    def jsonCreate():
        with open('sender.txt', 'r') as json_file:
            num = 0
            for line_email in json_file.readlines():
                num+=1
                line_email = line_email.strip()
        
                login, password = line_email.split(':')
                to_json = {'login':login, 'password':password}
                with open(f'Collected/{num}.json', 'w') as json_write:
                    json.dump(to_json, json_write)

def newDirs():
    try:new_dirs = WorkinWithFile
    except:pass
    try:new_dirs.examination()
    except:pass
    try:new_dirs.jsonCreate()
    except:password
newDirs()
email_to = input('Email: ')

def main_email(sender, password, files):

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = email_to
    msg['Subject'] = email_subject
    msg.attach(MIMEText(email_text, 'plain'))
    try:
        server = smtplib.SMTP_SSL('smtp.rambler.ru', 465)
        server.login(sender, password)
        server.sendmail(sender, email_to, msg.as_string())
        server.quit()
        print(f'[+] Сообщение отправлено с {sender} на {email_to}')
        shutil.move(f'Collected/{files}', f'Done/{files}')
    except Exception as ex:
        print(f'[x] Ошибка при отправке с почты {sender} на {email_to}\n{ex}\n')
        shutil.move(f'Collected/{files}', f'Trash/{files}')
    finally:time.sleep(1)

all_files = os.listdir('Collected/')
for files in all_files:
    with open(f'Collected/{files}') as f:
        data = json.load(f)
        sender = data['login']
        password = data['password']
        main_email(sender=sender, password=password, files=files)