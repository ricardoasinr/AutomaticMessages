import pywhatkit as kit

try:
  # Enviamos el mensaje
  pywhatkit.sendwhatmsg("+591########",
                        "Mensaje De Prueba",
                        15,22)
  print("Mensaje Enviado")
  
except:
  print("Ocurrio Un Error")







