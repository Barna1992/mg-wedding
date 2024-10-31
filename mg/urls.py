from django.contrib import admin
from django.urls import path
from evento import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('submit-allergy/', views.submit_allergy, name='submit_allergy'),
    path('allergie/', views.allergie_view, name='allergies_list'),
]