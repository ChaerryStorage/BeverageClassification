from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'beverage_classification'

urlpatterns = [
    # path('', views.pre_page, name='pre_page'),
    # path('index/', views.index, name='index'),
    path('', views.index, name='index'),

    path('beverage_img/', views.img_upload, name='img_upload'),
    path('beverage_img/predict', views.pred_beverage, name='pred_beverage'),
    path('beverage_img/detect_text/<str:file_name>/', views.detect_text_API, name='detect_text_API'),
    path('beverage_img/delete/<str:file_name>/', views.del_img, name='del_img'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
