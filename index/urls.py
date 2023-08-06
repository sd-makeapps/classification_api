from django.urls import path, include
from index.views import IndexView

urlpatterns = [
    path("", IndexView.as_view({'post': 'post_response'}), name='post_response'),
]
