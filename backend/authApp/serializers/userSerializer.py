from rest_framework                               import serializers
from authApp.models.user                   import User
from authApp.models.statistics               import historico

class UserSerializer(serializers.ModelSerializer):
    account = StatisticsSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'account']
        

    def to_representation(self, obj):
        user    = User.objects.get(id=obj.id)
        return {
            'id'      : user.id,
            'username': user.username,
            'name'    : user.name,
            'email'   : user.email
        }