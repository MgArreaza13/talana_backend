from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from apps.accounts import serializers as accounts_serializers
from apps.accounts import services as accounts_services
from django.utils.translation import gettext as _
from django.core.exceptions import PermissionDenied

# Create your views here.


class LoginView(APIView):
    """
       Get access to API with user information
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            user = accounts_services.login(request.data)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied as e:
            return Response({"detail": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        token, created = Token.objects.get_or_create(user=user)
        serializer = accounts_serializers.UserSerializers(user, many=False).data
        serializer['username'] = user.username
        serializer['token'] = token.key
        serializer['last_login'] = user.last_login
        return Response(serializer, status=status.HTTP_200_OK)


class LogoutView(APIView):
    """
        Deletes the user's token in the system.
    """
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        try:
            user = accounts_services.logout(user=request.user)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied as e:
            return Response({"detail": str(e)}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'detail': str(_('You have disconnected from the system'))}, status=status.HTTP_200_OK)


class ManagementUserViewSet(APIView):
    """
        Service for user
        contain cruds, creation, update, deleted, and list
    """
    # permission_classes = (permissions.IsAuthenticated,)
    # serializer_class = accounts_serializers.UserSerializers
    # queryset = accounts_models.User.objects.all()

    # def get_permissions(self):
    #     if self.action == 'retrieve':
    #         self.permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    #     return super(self.__class__, self).get_permissions()

    # def list(self, request, *args, **kwargs):
    #     search = self.request.query_params.get('search', None)
    #     filter_role = self.request.query_params.get('role', None)
    #     filter_status = self.request.query_params.get('status', None)
    #     try:
    #         users = accounts_services.list_profile(search, filter_role, filter_status, user=request.user)
    #     except ValueError as e:
    #         return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    #     except PermissionDenied as e:
    #         return Response({'detail': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
    #     except Exception as e:
    #         return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    #     page = self.paginate_queryset(users)
    #     serializer = self.get_serializer(page, many=True)
    #     return self.get_paginated_response(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    def post(self, request):
        try:
            user = accounts_services.register_user(request.data, user=request.user)
        except ValueError as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except PermissionDenied as e:
            return Response({'detail': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = accounts_serializers.UserSerializers(user, many=False).data
        serializer['detail'] = str(_("You have register a user correctly"))
        return Response(serializer, status=status.HTTP_201_CREATED)

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     try:
    #         user = accounts_services.edit_user(request.data, instance, user=request.user)
    #     except ValueError as e:
    #         return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    #     except PermissionDenied as e:
    #         return Response({'detail': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
    #     except Exception as e:
    #         return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    #     serializer = self.get_serializer(user, many=False).data
    #     serializer['detail'] = str(_("You have edit user data correctly"))
    #     return Response(serializer, status=status.HTTP_200_OK)

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     try:
    #         user = accounts_services.remove_user(instance, user=request.user)
    #     except ValueError as e:
    #         return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    #     except PermissionDenied as e:
    #         return Response({'detail': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
    #     except Exception as e:
    #         return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    #     return Response({"detail": str(_("You have remove this user correctly"))}, status=status.HTTP_200_OK)
