from django.http import Http404
from rest_framework import response, status
from rest_framework.response import Response
from rest_framework.views import APIView

from subscriptions.models import Subscription, Visit, User
from subscriptions.serializers import UserSerializer, SubscriptionSerializer, VisitSerializer


class RegisterUser(APIView):

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):

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

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubscriptionList(APIView):
    def get(self, request, format=None):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response({"subscriptions":serializer.data}, status.HTTP_200_OK)

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

    def get(self, request, pk, format=None):
        subscription = self.get_object(pk)
        serializer = SubscriptionSerializer(subscription)
        return Response({'subscription': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        subscription = self.get_object(pk)
        serializer = SubscriptionSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'subscription': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        subscription = self.get_object(pk)
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VisitList(APIView):

    def get(self, request, format=None):
        visits = Visit.objects.all()
        serializer = VisitSerializer(visits, many=True)
        return Response({"visits":serializer.data}, status.HTTP_200_OK)

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

    def get(self, request, pk, format=None):
        visit = self.get_object(pk)
        serializer = VisitSerializer(visit)
        return Response({'visit': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        visit = self.get_object(pk)
        serializer = VisitSerializer(visit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'visit': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        visit = self.get_object(pk)
        visit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VisitListForSubscription(APIView):

    def get(self, request, pk, format=None):
        visits = Visit.objects.filter(subscription=Subscription.objects.get(pk=pk))
        serializer = VisitSerializer(visits, many=True)
        return Response({'visits': serializer.data}, status=status.HTTP_200_OK)
