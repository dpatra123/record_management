from django.conf.urls import url
from myrecords import views
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
admin.site.site_header = "Record Management Admin Portal"
admin.site.site_title = "Record Management Admin Portal"
admin.site.index_title = "Welcome to Record Management Portal"

urlpatterns = [
        url(r'^myrecords/$', views.myRecords),
        url(r'^dashboard/$', views.myDashboard),
        url(r'^manage_records/$', views.manageRecords),
        url(r'^add_records/$', views.addRecord),
        url(r'^ajax/save_record/$', views.saveRecord),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)