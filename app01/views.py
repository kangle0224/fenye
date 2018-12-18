from django.shortcuts import render


USER_LIST = []
for i in range(1,999):
    tem = {'name': 'root'+str(i), "age": i}
    USER_LIST.append(tem)

def index(request):
    num_per_page = 10
    current_page = request.GET.get('p')

    return render(request, 'index.html', {"user_list": USER_LIST})
