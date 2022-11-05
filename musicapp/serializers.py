from rest_framework import serializers
from .models import Song, Artiste


class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        fields =(
            "id",
            "first_name",
            "last_name",
            "age",
        )
        model = Artiste


#create your seralizers here
class SongSerializer(serializers.ModelSerializer):
    artist_id = ArtisteSerializer
    class Meta:
        fields = (
        "id",
        "title",
         "date_released",
         "likes",
         "artist_id"
        )
        model = Song