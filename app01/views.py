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

class CustomPaginator(Paginator):
    # 此函数未完成，重点关注自定义分页
    def __init__(self, current_page, per_page_num, *args, **kwargs):
        super(CustomPaginator, self).__init__(*args, **kwargs)

    def page_num_range(self):
        # 返回页码起始位置
        return range(1,12)
def index1(request):
    current_page = request.GET.get('p')
    # 数据源 每页10条数据
    paginator = CustomPaginator(USER_LIST, 10)
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    # page:     page对象

    try:
        posts =paginator.page(current_page)
        # has_next              是否有下一页
        # next_page_number      下一页页码
        # has_previous          是否有上一页
        # previous_page_number  上一页页码
        # object_list           分页之后的数据列表
        # number                当前页
        # paginator             paginator对象
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'index1.html', {'posts': posts})

def index2(request):
    from app01.pager import Pagination
    current_page = request.GET.get('p')
    obj = Pagination(666, current_page)
    data_list = USER_LIST[obj.start(): obj.end()]

    return render(request, 'index2.html', {'data': data_list,
                                           'page_obj': obj})

