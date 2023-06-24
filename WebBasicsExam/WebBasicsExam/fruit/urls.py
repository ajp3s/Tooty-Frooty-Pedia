from django.urls import path

from WebBasicsExam.fruit.views import fruit_details, fruit_edit, fruit_delete

urlpatterns =(
    path('details/', fruit_details, name='fruit_details'),
    path('delete/', fruit_delete, name='fruit delete'),
    path('edit/', fruit_edit, name='fruit edit'),
)