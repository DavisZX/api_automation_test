import json
import logging

from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view

from api_test.common import GlobalStatusCode
from api_test.common.common import del_model, verify_parameter
from api_test.models import Project, ApiInfo, ProjectDynamic, ProjectMember

logger = logging.getLogger(__name__) # 这里使用 __name__ 动态搜索定义的 logger 配置，这里有一个层次关系的知识点。


@api_view(['GET'])
@verify_parameter(['project_id', ], 'GET')
def project_info(request):
    """
    获取项目详情
    project_id 项目id
    :return:
    """
    response = {}
    project_id = request.GET.get('project_id')
    if not project_id.isdecimal():
        return JsonResponse(GlobalStatusCode.ParameterWrong)
    obj = Project.objects.filter(id=project_id)
    if obj:
        data = json.loads(serializers.serialize('json', obj))
        logging.debug(data)
        response['data'] = del_model(data)
        return JsonResponse(dict(response, **GlobalStatusCode.success))
    else:
        return JsonResponse(GlobalStatusCode.ProjectNotExist)


@api_view(['GET'])
@verify_parameter(['project_id', ], 'GET')
def api_total(request):
    """
    获取接口数量
    project_id  项目ID
    :return:
    """
    response = {}
    project_id = request.GET.get('project_id')
    if not project_id.isdecimal():
        return JsonResponse(GlobalStatusCode.ParameterWrong)
    obi = Project.objects.filter(id=project_id)
    if obi:
        obj = ApiInfo.objects.filter(project=project_id)
        response['sum'] = len(obj)
        return JsonResponse(dict(response, **GlobalStatusCode.success))
    else:
        return JsonResponse(GlobalStatusCode.ProjectNotExist)


@api_view(['GET'])
@verify_parameter(['project_id', ], 'GET')
def dynamic_total(request):
    """
    获取动态数量
    project_id  项目ID
    :return:
    """
    response = {}
    project_id = request.GET.get('project_id')
    if not project_id.isdecimal():
        return JsonResponse(GlobalStatusCode.ParameterWrong)
    obi = Project.objects.filter(id=project_id)
    if obi:
        obj = ProjectDynamic.objects.filter(project=project_id)
        response['sum'] = len(obj)
        return JsonResponse(dict(response, **GlobalStatusCode.success))
    else:
        return JsonResponse(GlobalStatusCode.ProjectNotExist)


@api_view(['GET'])
@verify_parameter(['project_id', ], 'GET')
def project_member(request):
    """
    获取成员数量
    project_id  项目ID
    :return:
    """
    response = {}
    project_id = request.GET.get('project_id')
    if not project_id.isdecimal():
        return JsonResponse(GlobalStatusCode.ParameterWrong)
    obi = Project.objects.filter(id=project_id)
    if obi:
        obj = ProjectMember.objects.filter(project=project_id)
        response['sum'] = len(obj)
        return JsonResponse(dict(response, **GlobalStatusCode.success))
    else:
        return JsonResponse(GlobalStatusCode.ProjectNotExist)