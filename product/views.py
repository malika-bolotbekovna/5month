from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from .serializers import CategoryDetailSerializer, ProductDetailSerializer, ReviewDetailSerializer
from .models import Category, Product, Review


@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(data={'error': f'category with id = {str(id)} does not exist!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = CategoryDetailSerializer(category).data
    return Response(data=data)

@api_view(['GET'])
def category_api_view(request):
    categories = Category.objects.all()
    data = CategorySerializer(instance=categories, many=True).data
    return Response(
        data=data,
        status=status.HTTP_200_OK
    )



@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': f'product with id = {str(id)} does not exist!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(product).data
    return Response(data=data)

@api_view(['GET'])
def product_api_view(request):
    products = Product.objects.all()
    data = ProductSerializer(instance=products, many=True).data
    return Response(
        data=data,
        status=status.HTTP_200_OK
    )




@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': f'review with id = {str(id)} does not exist!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(review).data
    return Response(data=data)

@api_view(['GET'])
def review_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(instance=reviews, many=True).data
    return Response(
        data=data,
        status=status.HTTP_200_OK
    )