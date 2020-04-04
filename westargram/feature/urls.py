from django.urls import path

from .views import CommentView

path = [
    path('uploadcomment', CommentView.as_view())
]
