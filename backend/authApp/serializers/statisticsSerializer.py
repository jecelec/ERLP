from authApp.models.statistics import Historico
from authApp.models.user       import User
from rest_framework            import serializers

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Historico
        '''fields = ['id']'''
        fields = ['id', 'departamento', 'municipio', 'codigo_arl', 'year', 
        'month', 'economia', 'rela_dep', 'rela_indep', 'presu_acci_rasu', 'muertes_AT', 
        'pensiones_AT', 'pensiones_EL', 'incapacidades_EL', 'incapacidades_AT']

    def to_representation(self, obj):
        historico = Historico.objects.get(id=obj.id)
        '''historico = Historico.objects.all()'''



        return {
            'id'              : historico.id,
            'departamento'    : historico.departamento,
            'municipio'       : historico.municipio,
            'codigo_arl'      : historico.codigo_arl,
            'year'            : historico.year,
            'month'           : historico.month,
            'economia'        : historico.economia,
            'rela_dep'        : historico.rela_dep,
            'rela_indep'      : historico.rela_indep,
            'presu_acci_rasu' : historico.presu_acci_rasu,
            'muertes_AT'      : historico.muertes_AT,
            'pensiones_AT'    : historico.pensiones_AT,
            'pensiones_EL'    : historico.pensiones_EL,
            'incapacidades_EL': historico.incapacidades_EL,
            'incapacidades_AT': historico.incapacidades_AT            
        }          
          