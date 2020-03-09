# from django.core.mail import send_mail
# from django.core.mail import send_mass_mail
# from django.contrib.auth.models import User
# from celery import task
# from todoAppBackend.celery import app
# import time
# import json
# import logging

# @app.task
# def welcome_email(usuario, correo):
# 	cuerpo = ""
# 	###Mensaje para el usuario #########
# 	email_subject_usuario = 'Bienvenido'
# 	email_body_usuario = "Hola %s, bienvenido a nuestra todo app" %(usuario)
# 	send_mail (email_subject_usuario, cuerpo, 'mg.arreaza.13@gmail.com', ['',correo], fail_silently=True, html_message=email_body_usuario)
# 	#####Mensaje para el Administrador#######
# 	email_subject_Soporte = 'Nueno Registro'
# 	email_body_Soporte = "nuevo registro" 
# 	send_mail(email_subject_Soporte, cuerpo , 'mg.arreaza.13@gmail.com', ['mg.arreaza.13@gmail.com'],fail_silently=True, html_message=email_body_Soporte)