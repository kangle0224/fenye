from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, HttpResponse

USER_LIST = []
for i in range(1,999):
    tem = {'name': 'root'+str(i), "age": i}
    USER_LIST.append(tem)

def index(request):
    num_per_page = 10
    current_page = request.GET.get('p')
    current_page = int(current_page)
    start = (current_page-1)*num_per_page
    end = current_page*num_per_page
    data = USER_LIST[start: end]

    return render(request, 'index.html', {"user_list": data})


def index1(request):
    current_page = request.GET.get('p')
    paginator = Paginator(USER_LIST, 10)

    try:
        posts =paginator.page(current_page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'index1.html', {'posts': posts})