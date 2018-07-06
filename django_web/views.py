from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def test_api(request):
    return JsonResponse({"result": 0, "msg": "执行成功"})