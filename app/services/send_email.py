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
    html_message: str,
    from_name: str = None,
    from_email: str = None,
    subject: str = "Sem assunto"
):

    from_name = from_name or "ORANGO I/O TELEATENDIMENTO"
    from_email = from_email or "naoresponda@filipeelore.love"
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = f"[{from_name}] <{from_email}>"
    message["To"] = f"{to_name} <{to_email}>"

    static_url = "https://filipeelore.love"

    text = text_message or "Sem mensagem"
    html_message = html_message or "Sem mensagem"
    html = f"""\
    <html>
    <body style="width:100vw">
        <div style="display: inline-block; width: 600px; margin: 0 auto">
            <div style="width: 600px; overflow: hidden" >
                Imagem aqui
            </div>
            <div style="position: relative">
                <div style="height: 120%; transform: translateY(-30px); padding: 20px 20px 40px 20px; background-color: #FAFAFA; width: 494px; margin: 0 auto; border-radius:8px; box-sizing: border-box; word-break: break-all">
                    {html_message}
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
        print("Mensagem enviada")
    except Exception as e:
        print(e)
        raise e

    return {
        "msg": f"Email de recuperação de senha enviado com sucesso para {to_email}"}

@app.route("/send_email", methods=["GET"])
def send_email():
    name = request.args.get('name')
    email = request.args.get('email')
    subject = request.args.get('subject')
    message = request.args.get('message')
    send_email_func('Contato - Filipe & Lore', 'contato@filipelopes.me', message, message, name, None, subject)
    print("enviando mensagem")
    return f"Hello World {name}"