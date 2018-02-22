from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator

# Create your views here.
from .models import Areasinfo

def areas(request):
    '''地市'''
    area = Areasinfo.objects.filter(aParent_id__isnull=True)
    return render(request,'page_test/areas.html',{'area': area})


def show_page(request,num):
    '''分页显示'''
    # 查询数据库
    areas = Areasinfo.objects.filter(aParent_id__isnull=True)
    # 每页显示数量10个
    p =Paginator(areas,10)
    # 分页后的总页数
    p_num = p.num_pages
    # 分页后的页码列表[1,2,3,4]
    p_list = p.page_range

    # 判断访问的是否第一页,默认显示第一页
    if num=='':
        num = 1
    # 参数页的对象
    page1 = p.page(num)

    # 组织模板上下文
    context = {'page1':page1,'p':p}
    # 模板渲染
    return render(request,'page_test/page1.html',context)