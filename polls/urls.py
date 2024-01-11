from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]


# path() 함수에는 2개의 필수 인수인 route 와 view, 2개의 선택 가능한 인수로 kwargs 와 name 까지 모두 4개의 인수가 전달 되었다. 

# path() 인수: route
# route 는 URL 패턴을 가진 문자열 이다.  요청이 처리될 때, Django 는 urlpatterns 의 첫 번째 패턴부터 시작하여, 일치하는 패턴을 찾을 때 까지 요청된 URL 을 각 패턴과 리스트의 순서대로 비교한다.

# 패턴들은 GET 이나 POST 의 매개 변수들, 혹은 도메인 이름을 검색하지 않는다. 
# 예를 들어, https://www.example.com/myapp/ 이 요청된 경우, URLconf 는 오직 myapp/ 부분만 바라 본다. https://www.example.com/myapp/?page=3, 같은 요청에도, URLconf 는 역시 myapp/ 부분만 신경쓴다.

# path() 인수: view
# Django 에서 일치하는 패턴을 찾으면, HttpRequest 객체를 첫번째 인수로 하고, 경로로 부터 ‘캡처된’ 값을 키워드 인수로 하여 특정한 view 함수를 호출한다. 

# path() 인수: kwargs
# 임의의 키워드 인수들은 목표한 view 에 사전형으로 전달된다.

# path() 인수: name
# URL 에 이름을 지으면, 템플릿을 포함한 Django 어디에서나 명확하게 참조할 수 있다. 이 강력한 기능을 이용하여, 단 하나의 파일만 수정해도 project 내의 모든 URL 패턴을 바꿀 수 있도록 도와준다.