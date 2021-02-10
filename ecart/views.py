from django.shortcuts import render 

# Create your views here.
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ecart.models import ecart
from ecart.serializers import ecartSerializer
from rest_framework import filters, generics


@api_view(['GET', 'POST'])
def ecart_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        ecarts = ecart.objects.all()
        serializer = ecartSerializer(ecarts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ecartSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def ecart_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        ecarts = ecart.objects.get(pk=pk)
    except ecart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ecartSerializer(ecarts)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ecartSerializer(ecarts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ecarts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ecartListView(generics.ListAPIView): 
    queryset = ecart.objects.all() 
    serializer_class = ecartSerializer
    filter_backends = [filters.SearchFilter] 
    search_fields = ['=category_id__id', '=name']