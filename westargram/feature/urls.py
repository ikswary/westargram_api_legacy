from django.urls import path

from .views import CommentView, LoginView

urlpatterns = [
    path('uploadcomment', CommentView.as_view()),
    path('printcomment/<str:target>', CommentView.as_view()),
    path('login', LoginView.as_view()),

]
