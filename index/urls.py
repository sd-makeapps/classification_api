from django.urls import path, include
from index.views import IndexView

urlpatterns = [
    path("", IndexView.as_view({'get': 'get_response', 'post': 'post_response'}), name='index'),
]
