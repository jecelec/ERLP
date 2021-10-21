from django.urls                    import path
from authApp                        import views  as authAppViews
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from authApp import views

urlpatterns = [
    path('login/',                                                    TokenObtainPairView.as_view()), # use credentials to return tokens
    path('refresh/',                                                  TokenRefreshView.as_view()), # generate new access token
    path('user/',                                                     authAppViews.UserCreateView.as_view()), # create a new user
    path('user/<int:pk>/',                                            authAppViews.UserDetailView.as_view()), # check info for an specific user based on id(pk)
    path('statistics/crear/',                                         views.CrearNuevoReporteView.as_view()),
    path('statistics/muertes/',                                       views.HistoricoMuertesView.as_view()),
    path('statistics/departamentos/<int:user>/<int:departamento>/',   views.HistoricoRiesgosPorDepartamentoView.as_view()), 
    path('statistics/actualizar/<int:user>/<int:pk>/',                views.ActualizarReporteView.as_view()),
    path('statistics/eliminar/<int:user>/<int:pk>/',                  views.EliminarReporteView.as_view()),
]
