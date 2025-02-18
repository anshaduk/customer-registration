from django.urls import path
from . import views

from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView


urlpatterns = [
    path('personal/',views.PersonalDetailList.as_view(),name='personal_detail_list'),
    path('personal/<int:pk>/',views.PersonalDetailDetailView.as_view(),name='personal_detail_detail'),
    path('employment/',views.EmploymentDetailList.as_view(),name='employment_detail_list'),
    path('employment/<int:pk>/',views.EmploymentDetailDetialView.as_view(),name='employment_detail_detail'),

    path('schema/',SpectacularAPIView.as_view(),name='schema'),
    path('schema/swagger-ui/',SpectacularSwaggerView.as_view(url_name='schema'),name='swagger-ui'),
]