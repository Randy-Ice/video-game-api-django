from djoser.serializers import UserCreatePasswordRetypeSerializer

class UserCreationPasswordRetypeSerializer(UserCreatePasswordRetypeSerializer):
    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
        ]