from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl

from app import app, db
from flask import request

def send_email_func(
    to_name: str,
    to_email: str,
    text_message: str,
    from_name: str = None,
    from_email: str = None,
    subject: str = "Sem assunto"
):

    from_name = from_name or "CASAMENTO DE FILIPE & LORENA"
    from_email = from_email or "naoresponda@filipeelore.love"
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = f"[{from_name}] <{from_email}>"
    message["To"] = f"{to_name} <{to_email}>"

    static_url = "https://filipeelore.love"

    text = text_message or "Sem mensagem"
    html = f"""\
    <html>
    <body style="width:100vw">
        <div style="display: block; position: relative; width: 600px; margin: 0 auto">
            <div style="width: 600px; height: 140px; background-color: #000; overflow: hidden; text-align: center">
                <img src="https://filipeelore.love/static/img/white-email-logo.png" height="50px" style="margin-top:35px" />
            </div>
            <div style="position: relative">
                <div style="height: auto; transform: translateY(-20px); padding: 20px 20px 40px 20px; background-color: #FAFAFA; width: 494px; margin: 0 auto; box-sizing: border-box; word-break: break-all; box-shadow: 1px 1px 20px rgba(0,0,0,0.1)">
                    {text_message}
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    port = 465
    password = 'n@Or3sp7'

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL("mail.filipeelore.love", port, context=context) as server:
            server.login(from_email, password)
            server.sendmail(from_email, to_email, message.as_string())
    except Exception as e:
        print(e)
        raise e

@app.route("/send_email", methods=["GET"])
def send_email():
    name = request.args.get('name')
    email = request.args.get('email')
    subject = request.args.get('subject')
    message = request.args.get('message')
    
    # Mensagem para o casal
    send_email_func('Contato - Filipe & Lore', 'contato@filipeelore.love', f'''
    <p>Segue mensagem escrita:</p>
    <p>{message}</p>

    <p>Por {name} - {email}</p>
    ''', subject=f"Mensagem de {name}")
    
    # Mensagem de retorno
    send_email_func(name, email, f'''
    <p>Olá {name},</p>

    <p>Somos gratos pelo carinho e por fazer parte desse mmomento, desejamos também para você tudo de bom e que o SENHOR multiplique as bençãos sobre a sua vida.</p>

    <p>"Porque dele, e por meio dele, e para ele são todas as coisas. A ele, pois, a glória eternamente. Amém!" Rm 11:36</p>

    <p>Essa é uma mensagem automática,</p>

    <p>Gratidão,</p>

    <p>Filipe e Lore.</p>
    ''', subject="Filipe & Lore - Obrigado")
    print("enviando mensagem")

    return f"Hello World {name}"