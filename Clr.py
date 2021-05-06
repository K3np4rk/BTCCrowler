import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from selenium import webdriver
from time import sleep


def getInfoNS():
    driver = webdriver.Firefox()
    try:
        driver.get("https://www.nicehash.com/my/mining/stats")
        sleep(1.0)
    finally:
        driver.close()


def enviaEmail():
    # Criando estancia da mensagem
    msg = MIMEMultipart()
    message = "Esse é um email teste"

    # Configurar parametros do email
    password = "Azevedo#1"
    msg['From'] = "higor.com@hotmail.com"
    msg['To'] = "higor_com@hotmail.com"
    msg['Subject'] = "Segue em anexo lucros referente aos dias "

    # Adicona mensagem e anexo ao corpo do email
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("teste.xlsx", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="teste.xlsx"')

    msg.attach(part)
    msg.attach(MIMEText(message, 'plain'))

    # Conexão com server
    server = smtplib.SMTP('smtp.office365.com: 587')
    server.starttls()

    # Credenciais de login para enviar o e-mail
    server.login(msg['From'], password)

    # envie a mensagem através do servidor
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

    # Confirmação
    print("successfully sent email to %s:" % (msg['To']))


getInfoNS()
#enviaEmail()
