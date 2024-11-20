from django.urls import path

from UserServices.Controller import AuthController


urlpatterns = [
    path('login/',AuthController.LoginAPIView.as_view(),name='loginApi'),
    path('signup/',AuthController.SignupAPIView.as_view(),name='signupApi'),
    path('publicApi/',AuthController.PublicAPIView.as_view(),name='publicApi'),
    path('protectedApi/',AuthController.ProtectedAPIView.as_view(),name='protectedApi'),
]