from django.contrib.auth import views as auth_views
from graphene_django.views import GraphQLView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('avisos/', views.avisos, name="avisos"),
    path('subiraviso/', views.subiraviso, name="nuevoaviso"),
    path("login/", auth_views.LoginView.as_view(template_name="login/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="logout"),
    path('graphql/', GraphQLView.as_view(graphiql=True))
]