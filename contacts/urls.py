from django.urls import path
from .views import *

urlpatterns = [
    path("", ContactListView.as_view()),
    path("<int:id>", ContactDetailsView.as_view())
]