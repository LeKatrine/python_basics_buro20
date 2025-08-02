from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import smtplib
import os


def main():
    load_dotenv()

    done_mods = ["Основы Python", "GitHub", "API"]
    not_done_mods = ["Командная строка", "Введение в Python", "Введение в JS", "WEB-разработка"]
    dur = "3 месяца"
    msg_text = f"Привет Мама(Папа), я занимаюсь в школе третье место уже {dur}. В процессе я выполнил модули: {done_mods}! Сейчас я работаю над модулями {not_completed_modules}. Обучение мне нравится, я получил море знаний!"
    if not done_mods:
        msg_text = f"Привет Мама(Папа), я занимаюсь в школе третье место уже {dur}. Сейчас я работаю над модулями {not_done_mods}. Пока что я улучшаю свои навыки и узнаю много нового!"
    
    msg = MIMEMultipart()
    msg["From"] = os.environ["EMAIL_FROM"]
    msg["To"] = os.environ["EMAIL_FROM"]
    msg["Subject"] = "Тестовое письмо"
    msg.attach(MIMEText(msg_text, "plain"))
    
    server = smtplib.SMTP_SSL("smtp.yandex.ru:465")
    server.login(msg["From"], os.environ["PASSWORD"])
    server.sendmail(msg["From"], msg["To"], msg.as_string())
    server.quit()


if __name__ == "__main__":
    main()

