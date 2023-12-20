from rest_framework import serializers
from .models import Movie
from .models import WhichAge


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True,
                                     default="")
    rating = serializers.ChoiceField(
        choices=WhichAge.choices,
        default=WhichAge.GENERAL,
    )
    synopsis = serializers.CharField(allow_blank=True, default="")
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj: Movie):
        return obj.user.email

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)
