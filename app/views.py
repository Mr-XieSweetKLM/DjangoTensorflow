from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
import logging

# Create your views here.

logger = logging.getLogger(__name__)


class IndexView(ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        """
        过滤数据，并转为html格式
        Returns:

        """
        return


def InputImage(request, ):
    print("function InputImage start:")
    print("request: ", request.GET['location'])
    location = str(request.GET['location'])
    print("location: ", location)

    return HttpResponse("上传成功!")

# 参考代码
def blog_search(request, ):
    print("function start:")
    # form = ImageForm()
    # if request.method == 'post':
    #     form = ImageForm(request.POST)

    return HttpResponse("上传成功")

# 参考代码
def suggest_view(request):
    # form = SuggestForm()
    # if request.method == 'POST':
    #     form = SuggestForm(request.POST)
    #     if form.is_valid():
    #         suggest_data = form.cleaned_data['suggest']
    #         # new_record = Suggest(suggest=suggest_data)
    #         # new_record.save()
    #         # try:
    #         #     # 使用celery并发处理邮件发送的任务
    #         #     celery_send_email.delay('访客意见', suggest_data, 'haibincoder@outlook.com', ['tomming233@163.com'])
    #         # except Exception as e:
    #         #     logger.error("邮件发送失败: {}".format(e))
    #         return redirect('app:thanks')
    return render(request, 'blog/about.html')
