from django.shortcuts import render
import json
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'simple_api/index.html')

def return_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message', None)
        return JsonResponse({"message": message}, status=200)
