from django.urls import path
from WebBasicsExam.profiles.views import create_profile, profile_edit, profile_delete, profile_details
urlpatterns = (
    path('create/', create_profile, name='create profile'),
    path('details/', profile_details, name='profile details'),
    path('edit/', profile_edit, name='edit profile'),
    path('delete/', profile_delete, name='delete profile'),
)