from django.urls import path
from .views import (employee_list_view,  employee_detail_view, 
                    EmployeeAPIView , EmployeeDetailsAPIView)


urlpatterns = [ 
    # function based views
    path('api/employee/', employee_list_view, name='employee_list_view'),
    path('api/employee/detail/<int:id>/', employee_detail_view, name='employee_detail_view'),
    # path('api/home/', home_list_view,name = 'home_list_view' ),

    # class based views
    path('api/cbv/employee', EmployeeAPIView.as_view(), name='employee_list_api_view'),
    path('api/cbv/employee_detail/<int:id>', EmployeeDetailsAPIView.as_view(), name='employee_detail_api_view'),
    
]
