from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^home/$', home, name='home'),

    url(r'^market/$', market, name='market'),
    url(r'^marketwithparams/(\d+)/(\d+)/(\d+)/$', market_with_params, name='market_with_params'),

    url(r'^mine/$', mine, name='mine'),
    url(r'^register/$', register, name='register'),
    url(r'registerhandle/$', register_handle, name='register_handle'),
    url(r'^checkusername/$', check_username, name='check_username'),
    url(r'^logout/$', logout, name='logout'),

    url(r'^login/$', login, name='login'),
    url(r'^loginhandle/$', login_handle, name='login_handle'),
    url(r'^cart/$', cart, name='cart'),

    url(r'^addtocart/$', add_to_cart, name='add_to_cart'),
    url(r'^addnum/$', add_num, name='add_num'),
    url(r'^reducenum/$', reduce_num, name='reduce_num'),
    url(r'^deletecart/$', delete_cart, name='deltet_cart'),
    url(r'^cartselect/$', cart_select, name='cart_select'),
    url(r'^cartselectall/$', cart_selectall, name='cart_selectll'),

    url(r'^orderadd/$',order_add,name='order_add'),
    url(r'^order/(\d+)/$', order, name='order'),
    url(r'^orderchangestatus/$', order_change_status, name='order_change_status'),
    url(r'^orderwaitpay/$', order_waitpay, name='order_waitpay'),
    url(r'^orderpaid/$', order_paid, name='order_paid'),
    url('^topaid/$',to_paid,name='to_paid'),
    url('^cancelpaid/$',cancel_paid,name='cancel_paid'),

    url(r'^getpwd/$',getpwd,name='gepwd')
]




