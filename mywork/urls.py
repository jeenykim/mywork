"""
URL configuration for mywork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]

# 1.주소에서 polls/가 입력되면 polls.urls로 연결하고  
# 2.polls.urls의 views.index으로 연결하면 
# 3.views의 내용이 화면에 출력

# 최상위 URLconf 에서 polls.urls 모듈을 바라보게 설정한다.

# include() 함수는 다른 URLconf들을 참조할 수 있도록 도와준다. 

# Django가 함수 include()를 만나게 되면, URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include 된 URLconf로 전달한다.

# URL을 쉽게 연결할 수 있다. polls 앱에 그 자체의 URLconf(polls/urls.py)가 존재하는 한, “/polls/”, 또는 “/fun_polls/”, “/content/polls/”와 같은 경로, 또는 그 어떤 다른 root 경로에 연결하더라도, 앱은 잘 동작한다.

# 다른 URL 패턴을 포함할 때마다 항상 include()를 사용해야 합니다.