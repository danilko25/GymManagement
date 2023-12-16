from rest_framework import serializers

from subscriptions.models import User, Subscription, Visit


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User(email=validated_data['email'], first_name=validated_data["first_name"], last_name=validated_data["last_name"])
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        if "last_name" in validated_data:
            instance.last_name = validated_data['last_name']
        if "first_name" in validated_data:
            instance.first_name = validated_data['first_name']
        instance.save()
        return instance

class SubscriptionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date =serializers.DateField()
    price=serializers.IntegerField()
    type=serializers.CharField()

    def validate(self, data):
        if data["start_date"] > data["end_date"]:
            raise serializers.ValidationError("End of the subscription cannot be earlier than start date.")
        else:
            return data

    def create(self, validated_data):
        return Subscription.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if "start_date" in validated_data:
            instance.start_date = validated_data['start_date']
        if "end_date" in validated_data:
            instance.first_name = validated_data['end_date']
        if "price" in validated_data:
            instance.first_name = validated_data['price']
        if "type" in validated_data:
            instance.first_name = validated_data['type']

        instance.save()
        return instance

class VisitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    subscription_id = serializers.IntegerField()
    date = serializers.DateField()

    def create(self, validated_data):
        return Visit.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if "date" in validated_data:
            instance.start_date = validated_data['date']
        instance.save()
        return instance

