from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^products/$', views.ProductsView.as_view(), name='products'),
    url(r'^addprod/$', views.ProductsAdd.as_view(), name='addprod'),
    url(r'^categories/$', views.CategoriesView.as_view(), name='categories'),
    url(r'^addcat/$', views.CategoriesAdd.as_view(), name='addcat'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
