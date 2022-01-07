import pyrebase

config = {
  "apiKey": "AIzaSyBc92EOVXBAszZarkNrWcdBLOKJbAcbU6k",
  "authDomain": "portafolio-811dc.firebaseapp.com",
  "databaseURL": "https://portafolio-811dc-default-rtdb.firebaseio.com",
  "projectId": "portafolio-811dc",
  "storageBucket": "portafolio-811dc.appspot.com",
  "messagingSenderId": "819809137842",
  "appId": "1:819809137842:web:517d325f0db9e8752885ab",
  "measurementId": "G-70HS411F9J"
};

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

#Ejemplo de autenticación
usuario = auth.sign_in_with_email_and_password('marcel.lazodelavega@gmail.com','codigo123')
print(auth.get_account_info(usuario['idToken']))

#Enviando mail de verificación
auth.send_email_verificacion(usuario['idToken'])

#Cambiando contraseña
auth.send_password_reset_email('marcel.lazodelavega@gmail.com')

#Ejemplo de creación de usuario
user = input("Email:")
password = input("Password:")
auth.create_user_with_email_and_password(user,password)
print("User added!")