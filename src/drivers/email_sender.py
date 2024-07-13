import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_email: str, body: str) -> None:
  from_addr = "jqryriuchma3kfmy@ethereal.email"
  login = "jqryriuchma3kfmy@ethereal.email"
  password = "Ka68hQ2Yd4TmRT9Kpk"

  # Create message
  message = MIMEMultipart()
  message['From'] = 'viagens_confirmar@email.comm'
  message['To'] = ', '.join(to_email)

  message['Subject'] = "Confirmação de Viagem!"
  message.attach(MIMEText(body, 'plain'))

  server = smtplib.SMTP('smtp.ethereal.email', 587)
  server.starttls()
  server.login(login, password)
  text = message.as_string()
 
  for email in to_email:
    server.sendmail(from_addr, email, text)

  server.quit()