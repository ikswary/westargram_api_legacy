import json

from django.http import JsonResponse
from django.views import View

from .models import Comments, UserData


class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)

        Comments(
            username=data['username'],
            comment=data['comment']
        ).save()

        return JsonResponse({'message': 'Comment Upload Success'}, status=200)

    def get(self, request, target):
        result = list()
        comments = Comments.objects.values()
        for comment in comments:
            if comment['username'] == target:
                result.append(comment['comment'])
        print(result)
        return JsonResponse({'messages': result}, status=200)


class LoginView(View):
    def post(self, request):
        input = json.loads(request.body)
        userdatas = UserData.objects.values()

        for userdata in userdatas:
            if input['userid'] == userdata['userid'] and input['password'] == userdata['password']:
                return JsonResponse({'message': ''}, status=200)

        return JsonResponse({'message': 'INVALID_USER'}, status=401)
