from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^tryauth/$', views.auth_user_try, name='tryauth'),
    url(r'^logout/$', views.logout_view, name='logout'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
