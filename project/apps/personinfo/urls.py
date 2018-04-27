from django.urls import path
from .views import index
from .views import  AddPersonInfo, ViewPersonInfo,SearchPersonInfo,PersonInfolist,UpdateAddPersonInfo,DeleteAddPersonInfo
urlpatterns = (
   path('',index),
   path('add', AddPersonInfo.as_view(),name='add'),
   path('<int:pk>/update', UpdateAddPersonInfo.as_view(),name='update'),
   path('<int:pk>/delete', DeleteAddPersonInfo.as_view(),name='delete'),
   path('view', ViewPersonInfo.as_view(),name='view'),
   path('search', SearchPersonInfo.as_view(),name='search'),
   path('api/personinfo', PersonInfolist.as_view(),name='api'),
)
