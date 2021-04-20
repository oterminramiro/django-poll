from rest_framework import serializers
from .models import Poll, Option, Choice
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'password', 'email', 'date_joined')

class PollSerializer(serializers.ModelSerializer):
	customer = CustomerSerializer(many=False, read_only=False, required=False)

	class Meta:
		model = Poll
		fields = ('customer', 'name', 'slug', 'guid', 'created')
		depth = 1

class OptionSerializer(serializers.ModelSerializer):
	poll = PollSerializer(many=False, read_only=False, required=True)

	class Meta:
		model = Poll
		fields = ('poll', 'value', 'guid', 'created')
		depth = 1

class ChoiceSerializer(serializers.ModelSerializer):
	poll = PollSerializer(many=False, read_only=False, required=True)
	option = OptionSerializer(many=False, read_only=False, required=True)
	customer = CustomerSerializer(many=False, read_only=False, required=False)

	class Meta:
		model = Choice
		fields = ('poll', 'option', 'customer', 'guid', 'created')
		depth = 1
