
from rest_framework import serializers
from .models import ShortURL
from django.utils.timezone import now, timedelta
import random, string

class ShortURLSerializer(serializers.ModelSerializer):
    url = serializers.URLField(write_only=True)
    validity = serializers.IntegerField(default=30, write_only=True)
    shortcode = serializers.CharField(required=False)

    class Meta:
        model = ShortURL
        fields = ['url', 'validity', 'shortcode']

    def create(self, validated_data):
        validity = validated_data.pop('validity', 30)
        shortcode = validated_data.pop('shortcode', None)

        if not shortcode:
            shortcode = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

        expiry_time = now() + timedelta(minutes=validity)

        return ShortURL.objects.create(
            original_url=validated_data['url'],
            shortcode=shortcode,
            expiry=expiry_time
        )