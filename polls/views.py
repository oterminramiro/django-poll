from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from django.conf import settings
from django.core import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from .models import Poll, Option, Choice
from .serializers import CustomerSerializer, PollSerializer, OptionSerializer, ChoiceSerializer

# POST FOR CREATE USER
class CustomerCreate(APIView):
	def post(self,request):
		try:
			user = User.objects.create_user(
				username = request.data['username'],
				password = request.data['password']
			)
			return returnResponse( request, list(user) , True , 200 )
		except Exception as e:
			return returnResponse( request, str(e) , False , 500)

# GET ALL POLLS
class PollList(generics.ListAPIView):
	def get(self,request):
		try:
			queryset = Poll.objects.all()
			serializer = PollSerializer(queryset, many=True)
			return returnResponse( request, serializer.data , True , 200 )
		except Exception as e:
			return returnResponse( request, str(e) , False , 500 )

# GET A SINGLE POLL
class PollExist(generics.RetrieveAPIView):
	def get(self,request,slug):
		try:
			queryset = Poll.objects.filter(slug = slug)
			serializer = PollSerializer(queryset, many=True)
			return returnResponse( request, serializer.data , True , 200 )
		except Exception as e:
			return returnResponse( request, str(e) , False , 500)

# CREATE POLL
class PollCreate(APIView):
	def post(self,request):
		try:
			user_id = request.user.id

			poll = Poll.objects.create(
				name = request.data['name'],
				customer_id = user_id,
				slug = request.data['slug'],
			)

			for item in request.data['options']:
				option = Option.objects.create(
					value = item['value'],
					poll_id = poll.id
				)

			return returnResponse( request, poll.guid , True , 200 )
		except Exception as e:
			return returnResponse( request, str(e) , False , 500)

class ChoiceCreate(APIView):
	def post(self,request):
		try:
			user_id = request.user.id

			poll = Poll.objects.filter(guid = request.data['poll']).first()
			if poll == None:
				return returnResponse( request, 'Poll not found' , False , 200 )

			option = Option.objects.filter(guid = request.data['option']).first()
			if option == None:
				return returnResponse( request, 'Option not found' , False , 200 )

			choice = Choice.objects.create(
				poll_id = poll.id,
				option_id = option.id,
				customer_id = user_id,
			)

			return returnResponse( request, choice.guid , True , 200 )
		except Exception as e:
			return returnResponse( request, str(e) , False , 500)



def returnResponse(request, data, status, code):
	response = {
		'success': status,
		'data': data,
	}
	return Response( response , status = code )
