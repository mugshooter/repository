import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, reseiver_email, subject, message):
    #Подключение к серверу
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    #Авторизация на сервере
    server.login(sender_password, reseiver_email)

    #Создание сообщения
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = reseiver_email
    msg['Subject'] = subject
    
    #Добавление текста сообщения
    msg.attach(MIMEText(message, 'plain'))
    
    #Отправление сообщения
    server.send_message(msg)
    
    #Отключение от сервера
    server.quit()
    
#Пример использования
sender_email = 'ur_mail@gmail.com'
sender_password = 'ur_password@gmail.com'
reseiver_email = 'reseiver@gmail.com'
subject = 'Тема письма'
message = 'Текст письма'

send_email(sender_email, sender_password, reseiver_email, subject, message)