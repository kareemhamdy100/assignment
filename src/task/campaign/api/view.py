import json
from .serializers import CampaignSerializer
from django.http import HttpResponse, Http404, HttpResponseRedirect
from ..models import Campaign
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters import  rest_framework as filters

class SaleItemFilter(filters.FilterSet):

    class Meta:
        model = Campaign
        fields = {
            'name':['icontains'],
            'url':['iexact'],
            'country':['iexact'],
            'goal':['icontains'],
            'budget':['iexact'],
            'category':['iexact'],
            'created_at':['gte','lte']
        }

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    filterset_class = SaleItemFilter

    def list(self, request, *args, **kwargs):
        fields = request.GET.getlist('fields')
        if (fields):
            data = list(self.filter_queryset(Campaign.objects.values(*fields)))
            return Response(data, status=status.HTTP_200_OK)
        else:
            return super().list(request, args, kwargs)
