from django.urls import path

from .views import CommentView

urlpatterns = [
    path('uploadcomment', CommentView.as_view())
]
