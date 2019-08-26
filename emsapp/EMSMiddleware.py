from django.shortcuts import  redirect
from django.utils.deprecation import MiddlewareMixin


class EMSMiddleware(MiddlewareMixin):
    def __init__(self, get_response):  # 初始化
        super().__init__(get_response)

    # view处理请求前执行
    def process_request(self, request):  # 某一个view
        if "/user/" not in request.path:
            if not request.session.get("login"):
                request.session["before"] = request.path
                return redirect("user:login")