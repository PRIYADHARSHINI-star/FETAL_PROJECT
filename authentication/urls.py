from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name="login"),
    path('contacting', views.contacting, name='contacting'),
    path('about',views.about, name='about'),
    path('predict',views.predict,name="predict"),
    path('results',views.results,name="results")
]