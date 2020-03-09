from django.contrib.auth import models as accounts_models
from django.utils.translation import gettext as _

def validate_email(email: str):
    """
        Method to verify if email of user exists
        The email is unique

        :param email: email of user
        :type email: str
        :return: bool
        :raises: ValueError
    """
    if accounts_models.User.objects.filter(email=email.lower()).exists():
        raise ValueError(str(_("Email registered please try with another")))
    return True

def validate_username(username: str):
    """
        Method to verify if username of user exists
        The username is unique

        :param username: username of user
        :type username: str
        :return: bool
        :raises: ValueError
    """
    if accounts_models.User.objects.filter(username=username.lower()).exists():
        raise ValueError(str(_("username registered please try with another")))
    return True