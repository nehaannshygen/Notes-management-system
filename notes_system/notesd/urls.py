from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 


urlpatterns=[
    path('search',views.search,name='search'),
    path('SearchPage',views.SearchPage,name='SearchPage'),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
