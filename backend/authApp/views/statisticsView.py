from django.conf                                      import settings
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from rest_framework.permissions                       import IsAuthenticated
from rest_framework_simplejwt.backends                import TokenBackend

from authApp.models.statistics                        import Historico
from authApp.serializers.statisticsSerializer         import StatisticsSerializer


class VerRegistroView(generics.ListAPIView):
    serializer_class = StatisticsSerializer
    permission_classes = (IsAuthenticated,)
    queryset            = Historico.objects.all()

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Historico.objects.filter(id=self.kwargs['id'])
        return queryset

class CrearNuevoReporteView(generics.CreateAPIView):
    serializer_class = StatisticsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        


        serializer = StatisticsSerializer(data=request.data['report_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save() 

        return Response("Se creó reporte exitosamente", status=status.HTTP_201_CREATED)  

class EliminarReporteView(generics.DestroyAPIView):   
    serializer_class = StatisticsSerializer
    permission_classes = (IsAuthenticated,)
    queryset            = Historico.objects.all()

    def deliete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().destroy(request, *args, **kwargs)


class ActualizarReporteView(generics.UpdateAPIView):  
    serializer_class = StatisticsSerializer
    permission_classes = (IsAuthenticated,)
    queryset            = Historico.objects.all()

    def update(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().update(request, *args, **kwargs)


class HistoricoMuertesView(generics.ListAPIView):
    serializer_class = StatisticsSerializer
    permission_classes = (IsAuthenticated,)
    queryset            = Historico.objects.all()

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Historico.objects.filter(id=self.kwargs['id'])
        return queryset


class HistoricoRiesgosPorDepartamentoView(generics.ListAPIView):
    serializer_class = StatisticsSerializer
    permission_classes = (IsAuthenticated,)
    queryset            = Historico.objects.all()

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) 

        queryset = Historico.objects.filter(departamento = self.kwargs['departamento']) 
        return queryset  


  




