from django.contrib.auth.models import User
from apps.pet import models as pet_models
from django.utils.translation import gettext as _
from django.db import transaction, IntegrityError, DatabaseError



def getImage(ur):
    import base64

    from django.core.files.base import ContentFile
    
    if ur != None:
        format, imgstr = ur.split(';base64,')  # format ~= data:image/X,
        ext = format.split('/')[-1]  # guess file extension
        ur = ContentFile(base64.b64decode(imgstr), name='profileimg.' + ext)
        return ur
    return None

def create_pet(user: User, data:dict) -> pet_models.Pet:
    """
        service to create task

        :param user: user
        :type user: Model User
        :param data: information of task
        :type data: dict
        :return: list of tasks
    """
    try:
        with transaction.atomic():
            task = pet_models.Pet.objects.create(
                title=data.get('title'),
                photo= getImage(data.get("file", None)),
                )
    except Exception as e:
        print(e)
        raise ValueError(str(_("An error occurred while saving the task")))
    return task




def update_like_pet(id_pets):
    try:
        pet = pet_models.Pet.objects.get(id=id_pets)
        pet.likes += 1
        pet.save()
        pets = pet_models.Pet.objects.all().order_by('-likes')
    except pet_models.Pet.DoesNotExist as e:
        print(e)
        raise NameError(str(_("Not found")))
    return pets

def get_list_pet() -> pet_models.Pet:
    """
        service to get list or tasks

        :param user: user
        :type user: Model User
        :return: list of tasks
    """
    list_pet = pet_models.Pet.objects.all().order_by('-likes')
    return list_pet


def get_detail_pet(user: User, id: int) -> pet_models.Pet:
    """
        service to get detail from task

        :param user: user
        :type user: Model User
        :param id: id
        :type id: int
        :return: one task
    """
    try:
        pets = pet_models.Pet.objects.filter(id=id, user__id=user.id)
        if(len(task) == 0): 
            raise NameError(str(_("Not found")))
    except pet_models.Pet.DoesNotExist as e:
        print(e)
        raise NameError(str(_("Not found")))
    return pets


def delete_pet(user: User, id: int) -> str:
    """
        service to delete task

        :param user: user
        :type user: Model User
        :param id: id
        :type id: int
        :return: list tasks update
    """
    try:
        pet = pet_models.Pet.objects.get(id=id, user__id=user.id)
        pet.delete()
    except pet_models.Pet.DoesNotExist as e:
        print(e)
        raise NameError(str(_("error to delete")))
    return str(_("the task was deleted successfully"))


def update_pet(user: User, data: dict ,id: int) -> pet_models.Pet:
    """
        service to update task

        :param data: information of task
        :type data: dict
        :param user: user
        :type user: Model User
        :return: task
        :raises: ValueError
    """

    try:
        pet = pet_models.Pet.objects.get(id=id, user__id=user.id)
        pet.title = data.get('title')
        pet.description = data.get('description')
        pet.save()
    except DatabaseError as e:
        print(e)
        raise NameError(str(_("error to update pet")))
    return pet