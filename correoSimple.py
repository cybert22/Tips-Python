#importamos los paquetes necesarios

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# creamos instancia de objeto de mensaje

msg = MIMEMultipart()

message = "Correo desde python"

#configuramos los parametros del mensaje

password = "123" # correo valido del remitente gmail
msg['From'] = "origen4@gmail.com" # correo del remitente
msg['To'] = "desetino@outlook.com" # correo destino
msg['Subject'] = " que tal mi gente" # encabezado

# agregar en el cuerpo del mensaje

msg.attach(MIMEText(message, 'plain'))

# crear el servidor

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()

#credenciales de inicio de session para enviar el correo

server.login(msg['From'],password)

#Enviar el mensaje por medio del servidor

server.sendmail(msg['From'],msg['To'],msg.as_string())
server.quit()
print("mensaje enviado correctamente  a --> : %s:"%(msg['To']))


"""         IMPORTANTE
    NO OLVIDAR ACTIVAR  
    Permitir el acceso de apps menos seguras: SÍ EN SU CUENTA DE CORREO QUE LO DEJO EN 
    LA DESCRIPCION PARA QUE LO REDIRIJA AUTOMATICAMENTE DE LO CONTRARIO NO 
    PODRA ENVIAR EL CORREO y por cierto es necesario tener acceso a internet
    

    el proximo video tutorial subiré como adjuntar un archivo y fotos bye gente


   
    """

