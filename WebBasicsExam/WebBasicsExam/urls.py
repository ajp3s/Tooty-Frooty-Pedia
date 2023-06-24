from django.contrib import admin
from django.urls import path, include
from WebBasicsExam.fruit.views import create_fruit
from WebBasicsExam.common.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WebBasicsExam.common.urls')),
    path('<int:pk>', include('WebBasicsExam.fruit.urls')),
    path('profile/', include('WebBasicsExam.profiles.urls')),
    path('create/', create_fruit, name='create_fruit'),
    path('dashboard/', dashboard, name='dashboard'),

]
