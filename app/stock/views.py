from django.shortcuts import render

# Create your views here.
import json
from .models import Produto
from .serializers import ProdutoSerializer
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
def listProdutos(request):
    try:
        queryset = Produto.objects.all().order_by('codigo_produto')
        serializer = ProdutoSerializer(queryset, many=True, context={'request': request})
        return JsonResponse({'produtos': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Produto não existe'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def addProduto(request):
    try:
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse({'produtos': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Produto não existe'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def updateProduto(request, pk):
    try:
        produto = Produto.objects.get(id=pk)
        serializer = ProdutoSerializer(instance=produto, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        return JsonResponse({'produtos': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Produto não existe'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def deleteProduto(request, pk):
    try:
        produto = Produto.objects.get(id=pk)
        produto.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Produto não existe'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


