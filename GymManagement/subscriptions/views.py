from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import response, status
from rest_framework.response import Response
from rest_framework.views import APIView

from subscriptions.models import Subscription, Visit, User
from subscriptions.serializers import UserSerializer, SubscriptionSerializer, VisitSerializer


class RegisterUser(APIView):

    @swagger_auto_schema(operation_description="Register a new user", request_body=UserSerializer, responses={
        201: openapi.Response("Created user", UserSerializer),
        400: 'Bad Request. Invalid input or missing required fields.',
    })
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):

    @swagger_auto_schema(operation_description="Get a list of all users", responses={
        200: openapi.Response("List of users", UserSerializer(many=True))
    })
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users":serializer.data}, status.HTTP_200_OK)

class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_description="Get details of a particular user", responses={
        200: openapi.Response("Founded user", UserSerializer),
        404: "User does not exist"
    })
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Update details of a particular user",
                         request_body=UserSerializer, responses={
            200: openapi.Response("Updated user", UserSerializer),
            400: 'Bad Request. Invalid input or missing required fields.',
        })
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_description="Delete a user by id", responses={
        204: "User was successfully deleted"
    })
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubscriptionList(APIView):
    @swagger_auto_schema(operation_description="Get a list of all subscriptions", responses={
        200: openapi.Response("List of subscriptions", SubscriptionSerializer(many=True))
    })
    def get(self, request, format=None):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response({"subscriptions":serializer.data}, status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Create a new subscription", request_body=SubscriptionSerializer, responses={
        201: openapi.Response("Created subscription", SubscriptionSerializer),
        400: 'Bad Request. Invalid input or missing required fields.',
    })
    def post(self, request, format=None):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'subscriptions': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubscriptionDetail(APIView):

    def get_object(self, pk):
        try:
            return Subscription.objects.get(pk=pk)
        except Subscription.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_description="Get details of a particular subscription", responses={
        200: openapi.Response("Founded subscription", SubscriptionSerializer),
        404: "Subscription does not exist"
    })
    def get(self, request, pk, format=None):
        subscription = self.get_object(pk)
        serializer = SubscriptionSerializer(subscription)
        return Response({'subscription': serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Update details of a particular subscription",
                         request_body=SubscriptionSerializer, responses={
            200: openapi.Response("Updated subscription", SubscriptionSerializer),
            400: 'Bad Request. Invalid input or missing required fields.',
        })
    def put(self, request, pk, format=None):
        subscription = self.get_object(pk)
        serializer = SubscriptionSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'subscription': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_description="Delete a subscription by id", responses={
        204: "Subscription was successfully deleted"
    })
    def delete(self, request, pk, format=None):
        subscription = self.get_object(pk)
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VisitList(APIView):

    @swagger_auto_schema(operation_description="Get a list of all visits", responses={
        200: openapi.Response("List of visits", VisitSerializer(many=True))
    })
    def get(self, request, format=None):
        visits = Visit.objects.all()
        serializer = VisitSerializer(visits, many=True)
        return Response({"visits":serializer.data}, status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Create a new visit", request_body=VisitSerializer, responses={
        201: openapi.Response("Created visit", VisitSerializer),
        400: 'Bad Request. Invalid input or missing required fields.',
    })
    def post(self, request, format=None):
        serializer = VisitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'visits': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VisitDetail(APIView):
    def get_object(self, pk):
        try:
            return Visit.objects.get(pk=pk)
        except Visit.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_description="Get details of a particular visit", responses={
        200: openapi.Response("Founded visit", VisitSerializer),
        404: "Visit does not exist"
    })
    def get(self, request, pk, format=None):
        visit = self.get_object(pk)
        serializer = VisitSerializer(visit)
        return Response({'visit': serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Update details of a particular visit",
                         request_body=VisitSerializer, responses={
            200: openapi.Response("Updated visit", VisitSerializer),
            400: 'Bad Request. Invalid input or missing required fields.',
        })
    def put(self, request, pk, format=None):
        visit = self.get_object(pk)
        serializer = VisitSerializer(visit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'visit': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_description="Delete a visit by id", responses={
        204: "Visit was successfully deleted"
    })
    def delete(self, request, pk, format=None):
        visit = self.get_object(pk)
        visit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VisitListForSubscription(APIView):

    @swagger_auto_schema(operation_description="Get a list of visits of particular subscription", responses={
        200: openapi.Response("List of visits of particular subscription", VisitSerializer(many=True))
    })
    def get(self, request, pk, format=None):
        visits = Visit.objects.filter(subscription=Subscription.objects.get(pk=pk))
        serializer = VisitSerializer(visits, many=True)
        return Response({'visits': serializer.data}, status=status.HTTP_200_OK)
