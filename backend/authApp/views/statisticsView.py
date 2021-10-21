from django.conf                               import settings
from django.utils                              import translation
from rest_framework                            import generics, status
from rest_framework.response                   import Response
from rest_framework.permissions                import IsAuthenticated
from rest_framework_simplejwt.backends         import TokenBackend

from authApp.models.statistics                 import historico
from authApp.serializers.statisticsSerializer  import StatisticsSerializer


class CrearNuevoReporteView(generics.CreateAPIView):
    serializer_class = StatisticsSerializer
    permission_classes = (IsAuthenticated)
    queryset            = historico.objects.all()

    def post(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != request.data['user_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) 

        serializer = StatisticsSerializer(data=request.data['report_data'])
        serializer.is_valid(raise_exception=True)
        serializer.save() 

        return Response("Se creó reporte exitosamente", status=status.HTTP_201_CREATED)          

class HistoricoMuertesView(generics.ListAPIView):
    serializer_class = StatisticsSerializer
    permission_classes = (IsAuthenticated)
    queryset            = historico.objects.all()

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        queryset = historico.objects.aggregate(sum('muertes_AT'))
        return queryset


class HistoricoRiesgosPorDepartamentoView(generics.ListAPIView):
    serializer_class = StatisticsSerializer
    permission_classes = (IsAuthenticated)
    queryset            = historico.objects.all()

    def get_queryset(self):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != self.kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) 

        queryset = historico.objects.filter(departamento = self.kwargs['departamento']) 
        return queryset  


class ActualizarReporteView(generics.UpdateAPIView):  
    serializer_class = StatisticsSerializer
    permission_classes = (IsAuthenticated)
    queryset            = historico.objects.all()

    def put(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) 

        return super().update(request, *args, **kwargs)    


class EliminarReporteView(generics.DestroyAPIView):   
    serializer_class = StatisticsSerializer
    permission_classes = (IsAuthenticated)
    queryset            = historico.objects.all()

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['user']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)  

        return super().destroy(request, *args, **kwargs)    