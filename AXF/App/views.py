from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from .models import *
import hashlib
import uuid, os
from AXF.settings import MEDIA_ROOT
import hashlib


# 首页
def home(request):
    # 轮播数据
    wheels = MainWheel.objects.all()
    # 导航数据
    navs = MainNav.objects.all()
    # 必购数据
    mustbuys = MainMustbuy.objects.all()
    # shop数据
    shops = MainShop.objects.all()
    shop0 = shops.first()
    shop1_2 = shops[1:3]
    shop3_6 = shops[3:7]
    shop7_10 = shops[7:11]
    # 主要商品数据
    mainshows = MainShow.objects.all()

    data = {
        'wheels': wheels,
        'navs': navs,
        'mustbuys': mustbuys,
        'shop0': shop0,
        'shop1_2': shop1_2,
        'shop3_6': shop3_6,
        'shop7_10': shop7_10,
        'mainshows': mainshows,
    }
    return render(request, 'home/home.html', data)


# 闪购
def market(request):
    return redirect(reverse('App:market_with_params', args=['104749', '0', '0']))


# 带参数的闪购
def market_with_params(request, typeid, typechildid, sortid):
    # 分类数据
    foodtypes = FoodType.objects.all()
    # 商品数据,根据主分类id进行筛选
    goods_list = Goods.objects.filter(categoryid=typeid)

    # 再按照子分类进行筛选
    if typechildid != '0':
        goods_list = goods_list.filter(childcid=typechildid)

    # 获取当前主分类下的所有子分类
    childnames = FoodType.objects.filter(typeid=typeid)
    # '全部分类:0#进口水果:103534#国产水果:103533'

    child_type_list = []  # 存放子分类的数据
    if childnames.exists():
        childtypes = childnames.first().childtypenames.split('#')
        # print(childtypes)  # ['全部分类:0', '进口水果:103534', '国产水果:103533']

        for type in childtypes:
            type_list = type.split(':')  # ['进口水果', '103534']
            child_type_list.append(type_list)

    # print(child_type_list)
    # [['全部分类', '0'], ['进口水果', '103534'], ['国产水果', '103533']]

    # 排序规则
    if sortid == '0':  # 综合排序
        pass
    elif sortid == '1':  # 销量排序
        goods_list = goods_list.order_by('-productnum')
    elif sortid == '2':  # 价格降序
        goods_list = goods_list.order_by('-price')
    elif sortid == '3':  # 价格升序
        goods_list = goods_list.order_by('price')

    data = {
        'foodtypes': foodtypes,
        'goods_list': goods_list,
        'typeid': typeid,
        'child_type_list': child_type_list,
        'typechildid': typechildid,
    }

    return render(request, 'market/market.html', data)


# 我的
def mine(request):
    data = {
        'name': '',
        'icon': '',

    }

    userid = request.session.get('userid', '')
    print('userid', userid)
    if userid:
        user = User.objects.get(id=userid)
        name = user.name
        icon = user.icon
        data['name'] = name
        # data['icon'] = icon
        data['icon'] = '/upload/icon/' + icon
    return render(request, 'mine/mine.html', data)


# 注册
def register(request):
    return render(request, 'user/register.html')


# 注册操作
def register_handle(request):
    data = {
        'status': 1,
        'msg': 'ok'
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        passwrod = request.POST.get('password')
        email = request.POST.get('email')
        # passwrod = my_md5(passwrod)
        print('password', passwrod)

        icon = request.FILES.get('icon', '')

        # 检测提交过来的数据是否合法
        if len(username) < 6:
            data['status'] = 0
            data['msg'] = '用户名输入不合法'
            return render(request, 'user/register.html', data)

        try:
            user = User()
            user.name = username
            user.password = passwrod
            user.email = email
            # user.icon = icon

            if icon:
                filename = random_file() + '.png'
                user.icon = filename
                print('filename', filename)
                filepath = os.path.join(MEDIA_ROOT, filename)
                print('filepath', filepath)
                with open(filepath, 'ab') as fp:
                    for part in icon.chunks():
                        fp.write(part)
                        fp.flush()
            else:
                user.icon = ''

            user.save()

            request.session['userid'] = user.id

            return redirect(reverse('App:mine'))
        except:

            # return redirect(reverse('App:register'))
            return render(request, 'user/register.html', {'msg5': '注册失败!'})

    return redirect(reverse('App:register'))


# 获取随机的文件名称
def random_file():
    u = str(uuid.uuid4())
    m = hashlib.md5()
    # m.update(u.encode('utf-8'))
    m.update(u.encode('utf-8'))
    return m.hexdigest()


def logout(request):
    request.session.flush()
    return redirect(reverse('App:mine'))


# 检测有户名
def check_username(request):
    if request.method == 'GET':
        username = request.GET.get('username')

        users = User.objects.filter(name=username)
        # 如果用户名已经存在
        if users.exists():
            return JsonResponse({'status': 0, 'msg': '用户名已存在'})
        # 如果不存在
        else:
            return JsonResponse({'status': 1, 'msg': 'ok'})
    return JsonResponse({'status': -1, 'msg': '请求方式错误'})


# 登陆
def login(request):
    return render(request, 'user/login.html')


# 登陆操作
def login_handle(request):
    data = {
        'status': 0,
        'msg': 'ok',

    }

    if request.method == 'POST':
        # print('1111')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        users = User.objects.filter(name=username, password=password)
        if users.exists():
            request.session['userid'] = users.first().id
            userid = request.session.get('userid')
            print('登录userid', userid)
            data['status'] = 1
            data['msg'] = 'ok'

            return redirect(reverse('App:mine'))
        else:
            data['status'] = 0
            data['msg'] = '用户名或密码错误'
            return render(request, 'user/login.html', data)
    data['status'] = -1
    data['msg'] = '请求方式错误'
    return render(request, 'user/login.html', data)


# 购物车
def cart(request):
    # 先检查是否登陆
    userid = request.session.get('userid', '')
    user = User.objects.get(id=userid)
    if not userid:
        return redirect(reverse('App:login'))
    else:
        carts = Cart.objects.filter(user_id=userid)
        return render(request, 'cart/cart.html', {'carts': carts,'user':user})


# 添加购物车
def add_to_cart(request):
    data = {
        'status': 1,
        'msg': 'ok',
    }

    # 判断用户是否登录了
    userid = request.session.get('userid', '')
    if not userid:
        data['status'] = 0
        data['msg'] = '未登录1'

    else:
        # 如果登录了
        if request.method == 'GET':
            goodsid = request.GET.get('goodsid')
            num = request.GET.get('num')

            # 先判断该商品是否在用户的购物车中
            carts = Cart.objects.filter(user_id=userid, goods_id=goodsid)
            # 如果存在
            if carts.exists():
                cart = carts.first()
                cart.num += int(num)
                cart.save()
            # 添加到购物车
            else:
                cart = Cart()
                cart.user_id = userid
                cart.goods_id = goodsid
                cart.num = num
                cart.save()

        else:
            data['status'] = -1
            data['msg'] = '请求方式不正确'

    return JsonResponse(data)


# 数量+
def add_num(request):
    data = {
        'status': 1,
        'msg': 'ok',
    }

    userid = request.session.get('userid', '')
    if not userid:
        data['status'] = 0
        data['msg'] = '未登录'
    else:
        if request.method == 'GET':
            cartid = request.GET.get('cartid')

            cart = Cart.objects.get(id=cartid)
            cart.num += 1
            cart.save()
            # 防止女朋友
            data['num'] = cart.num

        else:
            data['status'] = -1
            data['msg'] = '请求方式错误'
    return JsonResponse(data)


def reduce_num(request):
    data = {
        'status': 1,
        'msg': 'ok',
    }

    userid = request.session.get('userid')

    if not userid:
        data['status'] = 0
        data['msg'] = '未登录'

    else:
        if request.method == 'GET':

            cartid = request.GET.get('cartid')
            cart = Cart.objects.get(id=cartid)

            if cart.num == 1:
                cart.num = 1
            else:
                cart.num -= 1
            cart.save()
            data['num'] = cart.num
        else:
            data['status'] = -1
            data['msg'] = '请求方式错误'
    return JsonResponse(data)


# 删除
def delete_cart(request):
    data = {
        'status': 1,
        'mag': 'ok'
    }
    userid = request.session.get('userid', '')
    if not userid:
        data['status'] = 0
        data['msg'] = '未登录'
    else:
        if request.method == 'GET':
            cartid = request.GET.get('cartid')
            # shanc
            Cart.objects.get(id=cartid).delete()
        else:
            data['status'] = -1
            data['msg'] = '请求方式错误'
    return JsonResponse(data)


# 勾选/取消勾选
def cart_select(request):
    data = {
        'status': 1,
        'mag': 'ok'
    }
    userid = request.session.get('userid', '')
    if not userid:
        data['status'] = 0
        data['msg'] = '未登录'
    else:
        if request.method == 'GET':
            cartid = request.GET.get('cartid')
            # 勾选/取消勾选
            cart = Cart.objects.get(id=cartid)
            # 去翻
            cart.is_select = not cart.is_select
            cart.save()
            data['is_select'] =cart.is_select


        else:
            data['status'] = -1
            data['msg'] = '请求方式错误'
    return JsonResponse(data)

#全选/取消全选
def cart_selectall(request):
    data = {
        'status': 1,
        'mag': 'ok'
    }
    userid = request.session.get('userid', '')
    if not userid:
        data['status'] = 0
        data['msg'] = '未登录'
    else:
        if request.method == 'GET':
            action = request.GET.get('action')
            selects = request.GET.get('selects')
            select_list = selects.split('#')
            # print(action,selects)

            #全不选操作
            if action == 'cancelselect':
                Cart.objects.filter(id__in=select_list).update(is_select=False)
            #全选操作
            else:
                Cart.objects.filter(goods_id__in=select_list).update(is_select=True)

        else:
            data['status'] = -1
            data['msg'] = '请求方式错误'
    return JsonResponse(data)

def order_add(request):
    data = {
        'status': 1,
        'mag': 'ok'
    }
    userid = request.session.get('userid', '')
    if not userid:
        data['status'] = 0
        data['msg'] = '未登录'
    else:
        if request.method == 'GET':

            #先获取当前用户购物车中勾选的商品
            carts = Cart.objects.filter(user_id=userid, is_select=True)

            #生成订单
            order = Order()
            order.order_id = str(uuid.uuid4())
            order.user_id = userid
            order.save()

            #创建商品信息

            total = 0 # 总价
            for cart in carts:
                order_goods = OrderGoods()
                order_goods.goods_id = cart.goods_id
                order_goods.order_id = order.id
                order_goods.num = cart.num
                order_goods.price = cart.goods.price
                order_goods.save()

                total += order_goods.num * order_goods.price
            # 添加总价
            order.order_price = total
            order.save()
            data['orderid'] = order.id
        else:
            data['status'] = -1
            data['msg'] = '请求方式错误'
    return JsonResponse(data)

#订单页面
def order(request,orderid):

    order = Order.objects.get(id= orderid)

    return render(request,'order/order.html',{'order':order})

#修改订单状态
def order_change_status(request):
    data = {
        'status': 1,
        'mag': 'ok'
    }
    userid = request.session.get('userid', '')
    if not userid:
        data['status'] = 0
        data['msg'] = '未登录'
    else:
        if request.method == 'GET':
            orderid = request.GET.get('orderid')
            # print('用户id:',orderid)
            order = Order.objects.get(id=orderid)

            status = request.GET.get('status')
            # print('订单支付状态改变码:',status)
            #
            Order.objects.filter(id=orderid).update(order_status=status)
            # Order.objects.filter(id=orderid)
            # print('支付状态改变后的实际码:',order.order_status)


        else:
            data['status'] = -1
            data['msg'] = '请求方式错误'
    return JsonResponse(data)

#待付款订单页面
def order_waitpay(request):

    userid = request.session.get('userid', '')
    if not userid:
        return redirect(reverse('App:mine'))
    else:
        # 若果登录了,则过去当前用户下的所有待付款订单
        orders = Order.objects.filter(user_id = userid, order_status='0')

        return render(request,'order/order_waitpay.html',{'orders':orders})

#待收货订单页面
def order_paid(request):

    userid = request.session.get('userid', '')
    if not userid:
        return redirect(reverse('App:mine'))
    else:
        # 若果登录了,则过去当前用户下的所有待收货订单
        orders = Order.objects.filter(user_id = userid, order_status='1')

        return render(request,'order/order_paid.html',{'orders':orders})


# 加密
def my_md5(str1):
    m = hashlib.md5()
    m.update(str1.encode('utf-8'))
    return m.hexdigest()

# def my_md5(str1):
#     m = hashlib.md5()
#     m.update(str1.encode('utf-8'))
#
#     return m.hexdigest()




"""
前后端数据交互,可以采用 在js 中使用ajax技术,在html中使用反向解析跳转,且都可以带上参数

反向跳转是同通过a标签的跳转链接功能  src='{% url 'App:loginhandle' 参数 %}' 通过反向跳转
到/App/loginhandle/ 路径下,找到该路径对应的视图函数,在views 中的函数 def login_handle(request) 实现跳转页面的逻辑功能,函数
数据库交互,经过处理,可将数据库数据再次渲染到(新)模板(templates/xx.html)中,实现前后端的数据交互

ajax 技术是在js(jq) 文件中对html和css进行操作,不能直接操作数据库 $.get('app/loginhandle' ,{'形参a':'实参a',..},functiong(data){ 
 {'形参a':'实参a',..}将html中或js(jq)中的数据传到后端,后端通过request.GET.get('形参a')获得前段传来的数据,经过处理,data={'形参b':'实参b',..}
 return JsonResponse(data) 将后端的数据返回给ajax请求,ajax在将数据通过Dom Bom等操作显示到html页面上去,实现前后端数据交互,且只需局部刷新,
 不用全局刷新网页,实现异步请求.
 ) 




"""








