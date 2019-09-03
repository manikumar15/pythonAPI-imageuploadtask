
from django.contrib import admin
from django.conf.urls import url,include
from restimgapp import views
from rest_framework import routers

from django.conf.urls.static import static
from django.conf import settings


# router=routers.DefaultRouter()

router=routers.SimpleRouter()
router.register('task',views.StudentViewSet)
router.register('duetask',views.DueViewSet)
router.register('completetask',views.CompleteViewSet)

urlpatterns = [
   url('admin/', admin.site.urls),
   url(r'',include(router.urls)),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
