from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
	path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

	path("list/", views.PollList.as_view(), name="list"),
	path("create/", views.PollCreate.as_view(), name="create"),
	path("vote/", views.ChoiceCreate.as_view(), name="vote"),
	path("poll/<slug:slug>/", views.PollExist.as_view(), name="poll"),
	path("customer_create/", views.CustomerCreate.as_view(), name="customer_create"),
]
