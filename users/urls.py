from django.contrib import admin
from django.urls import path, include
from .views import AutoCompMemberView, LoginView, LogoutView, RegisterView, UserView, GEVAInitView, BBTAPInitView

urlpatterns = [
	path('register/', RegisterView.as_view()),
	path('login/', LoginView.as_view()),
	path('user/', UserView.as_view()),
	path('logout/', LogoutView.as_view()),
	path('gevainit/', GEVAInitView.as_view()),
	path('bbtapinit/', BBTAPInitView.as_view()),
	path('autoCompM/', AutoCompMemberView.as_view()),
]