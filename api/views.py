from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import ShortURL, Click
from .serializers import ShortURLSerializer
from django.utils.timezone import now

@api_view(['POST'])
def create_short_url(request):
    serializer = ShortURLSerializer(data=request.data)
    if serializer.is_valid():
        shorturl = serializer.save()
        host = request.get_host()
        return Response({
            "shortLink": f"http://{host}/{shorturl.shortcode}",
            "expiry": shorturl.expiry.isoformat()
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_short_url_stats(request, shortcode):
    shorturl = get_object_or_404(ShortURL, shortcode=shortcode)
    click_data = [
        {
            "timestamp": click.timestamp,
            "referrer": click.referrer,
            "location": click.location
        } for click in shorturl.clicks.all()
    ]
    return Response({
        "original_url": shorturl.original_url,
        "created_at": shorturl.created_at,
        "expiry": shorturl.expiry,
        "clicks": shorturl.clicks.count(),
        "click_details": click_data
    })


# Create your views here.
