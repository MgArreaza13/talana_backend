from django.contrib.auth import models as accounts_models
from django.db.models import Q
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
from django.contrib.auth.models import Group
from django.db import transaction, IntegrityError, DatabaseError
from django.core.exceptions import PermissionDenied
import datetime as datetime_modules
from apps.accounts import validations as accounts_validations
from django.contrib.auth.hashers import make_password
from apps.accounts import tasks as accounts_task
# from apps.accounts.tasks import welcome_email

def login(data: dict) -> accounts_models.User:
	"""
		Get access user 
		Raise exception if user or password are incorrect or user does not exist.

		:param data: username and password of user.
		:type: dict.
		:return: user.
		:raises: ValueError, PermissionDenied.
	"""
	username = data.get("username", None)
	password = data.get("password", None)
	if username is None or not username:
		raise ValueError(str(_("The username cannot be empty")))
	if password is None or not password:
		raise ValueError(str(_("The password cannot be empty")))
	try:
		# Obtain user from database if exist
		user = accounts_models.User.objects.get(Q(username=username) | Q(email=username.lower()))
	except accounts_models.User.DoesNotExist as e:
		print(e)
		raise ValueError(str(_("The username or password is incorrect")))
	# Verify is user is active
	if not user.is_active:
		raise PermissionDenied(str(_("Account blocked, contact the administrators.")))
	# Verify if password match
	if not user.check_password(password):
		raise ValueError(str(_("The username or password is incorrect")))
	user = authenticate(username=user.username, password=password)
	return user



def logout(user: accounts_models.User) -> bool:
	"""
		Remove token access to user
		Raises exception if user is inactive.

		:param user: User into app
		:type: Model User.
		:return: User.
		:raises: ValueError.
	"""
	user.last_login = datetime_modules.datetime.now()
	user.save()
	user.auth_token.delete()
	return True



def register_user(data: dict, user: accounts_models.User):
	"""
		Method to register user in massone

		:param data: information of user to register
		:type data: dict
		:param user: user admin
		:type user: Model User
		:return: user
		:raises: ValueError
	"""
	email = data.get('email')
	# validate email
	if email is not None:
		accounts_validations.validate_email(email)
	else:
		email = ""
	# validate username
	if data.get('username') is not None:
		accounts_validations.validate_username(data.get('username'))
	# validate password
	if data.get('password1') != data.get('password2'):
		raise ValueError(str(_("An error occurred while saving the user, Passwords do not match")))
	with transaction.atomic():
		try:
			user_registered = accounts_models.User.objects.create(
				username=data.get('username'),
				first_name=data.get('first_name'),
				last_name=data.get('last_name'),
				email=email,
				password=make_password(data.get('password1')),
			)
			if user_registered.email != "":
				# welcome_email.delay(user_registered.username, user_registered.email)
				pass
		except Exception as e:
			raise ValueError(str(_("An error occurred while saving the user")))
	return user_registered