from django.conf.urls import include, url
from .views import *


urlpatterns = [
    url(r'clogin', UserLogin.as_view(),name="clogin"),
    url(r'super/base', SuperBaseView.as_view(), name="super_base"),  # 超级管理员对基础设施管理员管理
    url(r'super/school', SuperSchoolView.as_view(), name="super_school"),  # 超级管理员对学校管理员管理
    url(r'super/dorm', SuperDormView.as_view(), name="super_dorm"),  # 超级管理员对宿舍管理员管理
    url(r'super/guide', SuperGuideView.as_view(), name="super_guide"),  # 超级管理员对导员管理
]