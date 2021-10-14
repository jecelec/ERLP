from authApp.models.statistics import historico
from authApp.models.user    import User
from rest_framework                import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model  = historico
        fields = ['balance', 'lastChangeDate', 'isActive']

    def to_representation(self, obj):
        user    = User.objects.get(id=obj.user)
        estadistica = historico.objects.get(id=obj.id)
        return {
            'id'             : historico.id,
            'balance'        : historico.balance,
            'lastChangeDate' : historico.lastChangeDate,
            'isActive'       : historico.isActive,
            'user' : {
                'id'    : user.id,
                'name'  : user.name,
                'email' : user.email
            }
        }