from django.shortcuts import render

# Create your views here.
from .models import MainItems
from .serializers import ItemsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
import requests
import json



class ItemsList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    dataPoints = []
    def get(self, request, format=None):
        parameters = {}
        page = request.GET.get('page', None)
        parameters['page'] = page
        if page != None:
            page = '&page=' + page
        else:
            page = ''
        pagesize = request.GET.get('pagesize', None)
        parameters['pagesize'] = pagesize
        if pagesize != None:
            pagesize = '&pagesize=' + pagesize
        else:
            pagesize = ''
        fromdate = request.GET.get('fromdate', None)
        parameters['fromdate'] = fromdate
        if fromdate != None:
            fromdate = '&fromdate=' + fromdate
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        todate = request.GET.get('todate', None)
        parameters['todate'] = todate
        if todate!=None and (fromdate<=todate) :
            todate = '&todate=' + todate

        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        data = None
        dataFound = False
        #print(ItemsList.dataPoints)
        # print(parameters)
        for i in range(0, len(ItemsList.dataPoints)):
            if(parameters == ItemsList.dataPoints[i][0]):
                data = ItemsList.dataPoints[i][1]
                dataFound = True
        url = 'http://api.stackexchange.com/2.3/questions?key=U4DMV*8nvpm3EOpvf69Rxw((&site=stackoverflow' + page + pagesize + fromdate + todate +'&order=desc&sort=votes&filter=default'
        print(url)
        headers = {'user-agent': 'my-app/0.0.1'}
        if dataFound == False:
            response = requests.get(url, headers=headers)
            responseOfStackOverflow = response.text.replace("'", '"')
            data = json.loads(responseOfStackOverflow)
        else:
            print('Hitting Cache')
        serializer = ItemsSerializer(data=data)
       
        if serializer.is_valid():
            serializer.save()
            ItemsList.dataPoints = ItemsList.dataPoints + [[parameters, data]]
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer._errors)
            ItemsList.dataPoints = ItemsList.dataPoints + [[parameters, data]]
            return Response(serializer.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


