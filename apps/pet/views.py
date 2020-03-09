import json
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.pet import services as pets_services
from apps.pet import serializers as pets_serializers
# Create your views here.



class PetsView(APIView):

	"""
		get the list of tasks created by the user
	"""
	# permission_classes = (permissions.IsAuthenticated,)
	def get(self, request):
		try:
			pets = pets_services.get_list_pet()
		except ValueError as e:
			return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
		except PermissionDenied as e:
			return Response({'detail': str(e)}, status=status.HTTP_403_FORBIDDEN)
		except Exception as e:
			return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer = pets_serializers.PetSerializers(pets, many=True).data
		return Response(serializer, status=status.HTTP_200_OK)



class ManageViewsPetsView(APIView):

	"""
		get the list of tasks created by the user
	"""
	# permission_classes = (permissions.IsAuthenticated,)
	def get(self, request, id_pet):
		try:
			pets = pets_services.update_like_pet(id_pet)
		except ValueError as e:
			return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
		except PermissionDenied as e:
			return Response({'detail': str(e)}, status=status.HTTP_403_FORBIDDEN)
		except Exception as e:
			return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer = pets_serializers.PetSerializers(pets, many=True).data
		return Response(serializer, status=status.HTTP_200_OK)



class PetOptionsView(APIView):

	"""
		get the detail of tasks created by the user
		contain cruds, creation, update, deleted, list, and search
	"""
	# permission_classes = (permissions.IsAuthenticated,)
	def post(self, request):
		try:
			pet = pets_services.create_pet(request.user, request.data)
		except ValueError as e:
			return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
		except PermissionDenied as e:
			return Response({'detail': str(e)}, status=status.HTTP_403_FORBIDDEN)
		except Exception as e:
			return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer_context = {
			'request': request,
		}
		serializer = pets_serializers.PetSerializers(pet, context=serializer_context, many=False).data
		return Response(serializer, status=status.HTTP_200_OK)

	def get(self, request, id_task):
		try:
			pet = pets_services.get_detail_pet(request.user, id_task)
		except ValueError as e:
			return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
		except PermissionDenied as e:
			return Response({'detail': str(e)}, status=status.HTTP_403_FORBIDDEN)
		except Exception as e:
			return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer_context = {
			'request': request,
		}
		serializer = pets_serializers.TasksSerializers(pet,  context=serializer_context, many=False).data
		return Response(serializer, status=status.HTTP_200_OK)
	
	def put(self, request, id_task):
		try:
			pet = pets_services.update_pet(request.user, request.data, id_task)
		except ValueError as e:
			return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
		except PermissionDenied as e:
			return Response({'detail': str(e)}, status=status.HTTP_403_FORBIDDEN)
		except Exception as e:
			return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		serializer_context = {
			'request': request,
		}
		serializer = pets_serializers.TasksSerializers(pet, context=serializer_context, many=False).data
		serializer['detail'] = str(_("You have edit task correctly"))
		return Response(serializer, status=status.HTTP_200_OK)

	def delete(self, request, id_task):
		try:
			message = pets_services.delete_pet(request.user, id_task)
		except ValueError as e:
			return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
		except PermissionDenied as e:
			return Response({'detail': str(e)}, status=status.HTTP_403_FORBIDDEN)
		except Exception as e:
			return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		# serializer = pets_serializers.TasksSerializers(task, many=True).data
		return Response(message, status=status.HTTP_200_OK)