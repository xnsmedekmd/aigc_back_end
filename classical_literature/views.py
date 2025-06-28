from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Poetry, Prose
from .serializers import PoetrySerializer, ProseSerializer, ContentListSerializer

def get_error_response(code, message):
    """生成错误响应"""
    return {
        'code': code,
        'message': message,
        'data': None
    }

@api_view(['GET'])
def content_video(request):
    """获取内容视频接口"""
    content_type = request.GET.get('type')
    content_id = request.GET.get('id')
    
    # 参数检查
    if not content_type or not content_id:
        return Response(get_error_response(1001, '请求参数错误'), status=status.HTTP_400_BAD_REQUEST)
    
    try:
        content_id = int(content_id)
    except ValueError:
        return Response(get_error_response(1001, 'ID必须为数字'), status=status.HTTP_400_BAD_REQUEST)
    
    try:
        if content_type == 'poetry':
            content = Poetry.objects.get(id=content_id)
            serializer = PoetrySerializer(content)
        elif content_type == 'prose':
            content = Prose.objects.get(id=content_id)
            serializer = ProseSerializer(content)
        else:
            return Response(get_error_response(1001, '内容类型错误'), status=status.HTTP_400_BAD_REQUEST)
    except (Poetry.DoesNotExist, Prose.DoesNotExist):
        return Response(get_error_response(1002, '内容不存在'), status=status.HTTP_404_NOT_FOUND)
    
    # 返回成功响应
    return Response({
        'code': 0,
        'message': 'success',
        'data': serializer.data
    })

@api_view(['GET'])
def content_detail(request):
    """获取内容详情接口"""
    content_type = request.GET.get('type')
    content_id = request.GET.get('id')
    
    # 参数检查
    if not content_type or not content_id:
        return Response(get_error_response(1001, '请求参数错误'), status=status.HTTP_400_BAD_REQUEST)
    
    try:
        content_id = int(content_id)
    except ValueError:
        return Response(get_error_response(1001, 'ID必须为数字'), status=status.HTTP_400_BAD_REQUEST)
    
    try:
        if content_type == 'poetry':
            content = Poetry.objects.get(id=content_id)
            serializer = PoetrySerializer(content)
        elif content_type == 'prose':
            content = Prose.objects.get(id=content_id)
            serializer = ProseSerializer(content)
        else:
            return Response(get_error_response(1001, '内容类型错误'), status=status.HTTP_400_BAD_REQUEST)
    except (Poetry.DoesNotExist, Prose.DoesNotExist):
        return Response(get_error_response(1002, '内容不存在'), status=status.HTTP_404_NOT_FOUND)
    
    # 返回成功响应
    return Response({
        'code': 0,
        'message': 'success',
        'data': serializer.data
    })

@api_view(['GET'])
def content_list(request):
    """获取所有内容列表接口"""
    # 从数据库获取所有内容
    poetry_list = Poetry.objects.all()
    prose_list = Prose.objects.all()
    
    # 序列化数据
    poetry_serializer = ContentListSerializer(poetry_list, many=True)
    prose_serializer = ContentListSerializer(prose_list, many=True)
    
    # 返回成功响应
    return Response({
        'code': 0,
        'message': 'success',
        'data': {
            'poetry': poetry_serializer.data,
            'prose': prose_serializer.data
        }
    })
