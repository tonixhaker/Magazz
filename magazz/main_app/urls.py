from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index),
    url(r'^products/$', views.ProductsView.as_view(), name='products'),
    url(r'^products/post$', views.ProductsView.as_view(), name='products'),
    url(r'^productedit/(?P<pk>\d+)/$', views.ProductEdit.as_view(), name='productedit'),
    url(r'^addprod/$', views.ProductsAdd.as_view(), name='addprod'),
    url(r'^prodetail/(?P<pk>\d+)/$', views.ProductDetail.as_view(), name='prodetail'),
    url(r'^prodell/(?P<pk>\d+)/$', views.ProductDel.as_view(), name='prodell'),
    url(r'^catdel/(?P<pk>\d+)/$', views.CategoryDel.as_view(), name='catdel'),
    url(r'^categories/$', views.CategoriesView.as_view(), name='categories'),
    url(r'^addcat/$', views.CategoriesAdd.as_view(), name='addcat'),
    url(r'^review/$', views.add_review, name='review'),
    url(r'^addtocart/(?P<pk>\d+)/$', views.AddInCart.as_view(), name='addtocart'),
    url(r'^cart/$', views.CartView.as_view(), name='cart'),
    url(r'^cartdel/(?P<pk>\d+)/$', views.CartDel.as_view(), name='cartdel'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
