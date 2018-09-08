from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render, HttpResponse
from .models import UseInfo, Publisher, Book, Author
from django.views import View
from django.urls import reverse
from utils import mypage,mypage_search

'''
 # CBV(class base view)和FBV(function base view)
'''


def test(request):
    content = {
        'name': '小哈',

    }
    return render(request, 'test.html', content)


# 上传文件
'''
# 当文件小于2.5M时,django会将上传的文件的全部内容读入内存,但当文件很大时,会把上传文件写到临时文件中,
# 然后存放系统临时文件夹中
'''
class UploadFile(View):
    def post(self,request):
        # 从请求的files中获取文件名,为页面中type=files类型input的name属性值
        filename = request.FILES['upload_file'].name
        # 在项目目录下新建一个文件
        with open(filename,'wb') as f:
            # 从上传的文件对象中一点一点的读
            for i in request.FILES['upload_file'].chunks():
                # 写入本地文件
                f.write(i)
        return HttpResponse('上传成功!')


def login(request):
    error_msg = ''
    if request.method == 'POST':
        email = request.POST.get('email', None)
        pwd = request.POST.get('pwd', None)
        print(email, pwd)
        if email == '111@qq.com' and pwd == '123456':
            # return HttpResponse('登录成功')
            return redirect('http://www.baidu.com')  # 重定向
        else:
            error_msg = '邮箱或密码错误'
    return render(request, 'login.html', {'error': error_msg})


def user_list(request):
    # 去数据库中查询所有用户数据
    ret = UseInfo.objects.all()
    return render(request, 'user_list.html', {'user_list': ret})


def add_user(request):
    '''添加用户'''
    if request.method == 'POST':
        new_name = request.POST.get('username', None)
        UseInfo.objects.create(name=new_name)
        return redirect('/user_list/')
    return render(request, 'add_user.html')


# 图书出版社列表
def publisher_list(request):
    ret = Publisher.objects.all().order_by('id')
    return render(request, 'publisher_list.html', {'publisher_list': ret})


def add_publisher(request):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('publisher_name', None)
        if new_name:
            Publisher.objects.create(name=new_name)
            # return redirect('/publisher_list/')
            redirect_url = reverse('pub_l')      # 利用反向解析
            return redirect(redirect_url)
        else:
            error_msg = '出版社名字不能为空！'
    return render(request, 'add_publisher.html', {'error_msg': error_msg})


def delete_publisher(request,del_id):
    # 删除指定的数据
    # 1. 从GET请求的参数里面拿到将要删除的数据的ID值
    # del_id = request.GET.get('id', None)
    if del_id:
        # 去数据库删除当前id值的数据
        # 根据id值查找到数据
        del_obj = Publisher.objects.get(id=del_id)
        del_obj.delete()
        return redirect(reverse('pub_l'))

    else:
        return HttpResponse('要删除的数据不存在')


def edit_publisher(request,edit_id):
    # edit_id = request.GET.get('id', None)
    if request.method == 'GET':
        if edit_id:
            publisher_obj = Publisher.objects.get(id=edit_id)
            return render(request, 'edit_publisher.html', {'publisher': publisher_obj})
    if request.method == 'POST':
        new_name = request.POST.get('publisher_name', None)
        # edit_id = request.POST.get('id', None)
        publisher_obj = Publisher.objects.get(id=edit_id)
        if new_name:
            edit_publisher = Publisher.objects.get(id=edit_id)
            edit_publisher.name = new_name
            edit_publisher.save()
            return redirect(reverse('pub_l'))
        else:
            return render(request, 'edit_publisher.html', {'publisher': publisher_obj, 'error': '不能为空！'})


# 书籍搜索
def book_search(request):
    page_num = request.GET.get('page', 1)
    book_search = None
    if request.method == 'POST':
        book_search = request.POST.get('book_search')
    if request.method == 'GET':
        book_search = request.GET.get('q')
    if book_search:
        book_obj = Book.objects.filter(title__contains=book_search)
        total_count = book_obj.count()
    else:
        book_obj = Book.objects.all()
        total_count = book_obj.count()
    url_prefix = '/book_search/'
    my_page = mypage_search.Page(page_num,total_count,url_prefix,book_search)
    data_start = my_page.data_start
    data_end = my_page.data_end
    page_html = my_page.page_html()
    all_book = book_obj[data_start:data_end]
    # print(all_book)

    return render(request, 'book_list.html', {'all_book': all_book,'page_html':page_html})

# # 书的列表
# def book_list(request):
#     all_book = Book.objects.all()
#     return render(request, 'book_list.html', {'all_book': all_book})

# 书的列表
def book_list(request):
    page_num = request.GET.get('page',1)

    total_count = Book.objects.count()
    url_prefix = '/book_list/'
    my_page = mypage.Page(page_num,total_count,url_prefix)
    data_start = my_page.data_start
    data_end = my_page.data_end
    page_html = my_page.page_html()
    all_book = Book.objects.all()[data_start:data_end]
    print(all_book)

    return render(request, 'book_list.html', {'all_book': all_book,'page_html':page_html})

# 添加书籍
def add_book(request):
    if request.method == 'POST':
        new_title = request.POST.get('book_title')
        new_publisher_id = request.POST.get('publisher')

        # 用出版社对象创建
        # publisher_obj = Publisher.objects.get(id=new_publisher_id)
        # Book.objects.create(title=new_title, publisher=publisher_obj)

        Book.objects.create(title=new_title, publisher_id=new_publisher_id)
        return redirect('/book_list/')
    ret = Publisher.objects.all()
    return render(request, 'add_book.html', {'publisher_list': ret})


# 删除书籍
def delete_book(request,delete_id):
    # delete_id = request.GET.get('id')
    Book.objects.get(id=delete_id).delete()
    return redirect(reverse('book_l'))


# 编辑书籍
def edit_book(request):
    edit_id = request.GET.get('id', None)
    publisher_list = Publisher.objects.all()
    if edit_id:
        edit_book_obj = Book.objects.get(id=edit_id)
        publisher_list = Publisher.objects.all()
        return render(request, 'edit_book.html', {'publisher_list': publisher_list, 'edit_book_obj': edit_book_obj})
    if request.method == 'POST':
        book_id = request.POST.get('id')
        edit_book_obj = Book.objects.get(id=book_id)
        new_book_title = request.POST.get('book_title')
        new_publisher_id = request.POST.get('publisher')
        if new_book_title:
            edit_book_obj.title = new_book_title
            edit_book_obj.publisher_id = new_publisher_id
            edit_book_obj.save()
            return redirect('/book_list/')
        else:
            return render(request, 'edit_book.html',
                          {'publisher_list': publisher_list, 'edit_book_obj': edit_book_obj, 'error': '书名不能为空!'})


# 编辑书籍
def edit_book1(request,edit_id):
    # edit_id = request.GET.get('id', None)
    publisher_list = Publisher.objects.all()
    if request.method == 'GET':
        if edit_id:
            edit_book_obj = Book.objects.get(id=edit_id)
            publisher_list = Publisher.objects.all()
            return render(request, 'edit_book.html', {'publisher_list': publisher_list, 'edit_book_obj': edit_book_obj})
    if request.method == 'POST':
        # book_id = request.POST.get('id')
        edit_book_obj = Book.objects.get(id=edit_id)
        new_book_title = request.POST.get('book_title')
        new_publisher_id = request.POST.get('publisher')
        # new_publisher_obj = Publisher()
        if new_book_title:
            edit_book_obj.title = new_book_title
            edit_book_obj.publisher_id = new_publisher_id
            edit_book_obj.save()
            redirect_url = reverse('book_l')
            # return redirect('/book_list/')
            return redirect(redirect_url)
        else:
            return render(request, 'edit_book.html',
                          {'publisher_list': publisher_list, 'edit_book_obj': edit_book_obj, 'error': '书名不能为空!'})

# 作者列表
def author_list(request):
    all_author = Author.objects.all()
    return render(request, 'author_list.html', {'author_list': all_author})


# 添加作者
def add_author(request):
    if request.method == 'POST':
        new_author_name = request.POST.get('author_name')
        books = request.POST.getlist('books')  # 多个值时用getlist
        new_author_obj = Author.objects.create(name=new_author_name)
        new_author_obj.book.set(books)  # 把新作者和书籍建立对应关系，自动提交
        return redirect(reverse('author_l'))
    book_list = Book.objects.all()
    return render(request, 'add_author.html', {'book_list': book_list})


# 删除作者
def delete_author(request,delete_id):
    # delete_id = request.GET.get('id')
    Author.objects.get(id=delete_id).delete()  # 会自动删除关联记录
    return redirect(reverse('author_l'))


# 编辑作者
def edit_author(request):
    if request.method == 'POST':
        new_author_name = request.POST.get('author_name')
        new_books = request.POST.getlist('books')
        edit_author_id = request.POST.get('author_id')
        edit_author_obj = Author.objects.get(id=edit_author_id)
        edit_author_obj.name = new_author_name
        edit_author_obj.book.set(new_books)  # 把新作者和书籍建立对应关系，自动提交
        edit_author_obj.save()  # 编辑的要提交
        return redirect('/author_list/')

    edit_id = request.GET.get('id')
    edit_author_obj = Author.objects.get(id=edit_id)
    book_list = Book.objects.all()
    return render(request, 'edit_author.html', {'book_list': book_list, 'author': edit_author_obj})


# CBV版 编辑作者 (class base view)
class EditAuthor(View):

    def get(self, request,edit_id):
        # edit_id = request.GET.get('id')
        edit_author_obj = Author.objects.get(id=edit_id)
        book_list = Book.objects.all()
        return render(request, 'edit_author.html', {'book_list': book_list, 'author': edit_author_obj})

    def post(self, request,edit_id):
        new_author_name = request.POST.get('author_name')
        new_books = request.POST.getlist('books')
        # edit_author_id = request.POST.get('author_id')
        edit_author_obj = Author.objects.get(id=edit_id)
        edit_author_obj.name = new_author_name
        edit_author_obj.book.set(new_books)  # 把新作者和书籍建立对应关系，自动提交
        edit_author_obj.save()  # 编辑的要提交
        redirect_url = reverse('author_l')
        # return redirect('/author_list/')
        return redirect(redirect_url)