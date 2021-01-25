from rest_framework import serializers
from .models import MatchModel, MatchContent
from rest_meets_djongo.serializers import DjongoModelSerializer


class MatchModelSerializer(serializers.ModelSerializer):
    match_image = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = MatchModel

    def get_match_image(self, obj):
        re_serializer = MatchModelSerializer(obj.match_image, many=True)
        return re_serializer.data


class MatchContentSerializer(DjongoModelSerializer):
    class Meta:
        # fields = ['activity_name', 'match_image', 'match_keyword', 'match_definition', 'created_at']
        fields = '__all__'
        model = MatchContent
        abstract = True


###############################
#
# class MatchImageSerializer(DjongoModelSerializer):
#     class Meta:
#         fields = 'match_image'
#         model = MatchImage
#
#
# class MatchKeySerializer(DjongoModelSerializer):
#     class Meta:
#         fields = 'match_keyword'
#         model = MatchKey
#
#
# class MatchDefSerializer(DjongoModelSerializer):
#     class Meta:
#         fields = 'match_definition'
#         model = MatchDef
#
# class MatchGameSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = '__all__'
#         model = MatchupGame
#
# class AllSerializer(serializers.ModelSerializer):
#     Title = MatchGameSerializer(write_only=True)
#     # Img = MatchDefSerializer(many=True, write_only=True)
#     # Key = MatchKeySerializer(many=True, write_only=True)
#     # Def = MatchDefSerializer(many=True, write_only=True)
#
#     class Meta:
#         fields = ['Title']
#         model = MatchupGame
#         abstract = True
