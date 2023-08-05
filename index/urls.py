from django.urls import path, include
from index.views import IndexView


urlpatterns = [
    path("", IndexView.as_view({'get': 'index'}), name='index')
]