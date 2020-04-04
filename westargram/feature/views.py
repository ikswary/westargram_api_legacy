import json

from django.http import JsonResponse
from django.views import View

from .models import Comments


class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)

        Comments(
            username=data['username'],
            comment=data['comment']
        ).save()

        return JsonResponse({'message': 'Comment Upload Success'}, status=200)
