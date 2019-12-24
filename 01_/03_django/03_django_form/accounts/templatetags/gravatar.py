import hashlib
from django import template

register = template.Library()

## 커스텀 필터 만들어주는 곳
# 기본필터 추가를 decorator 를 사용하여 등록시켜준다.
@register.filter  ## 아래의 함수를 추가 시켜 준다.
def makemd5(email):
    return hashlib.md5(email.encode('utf-8').lower().strip()).hexdigest()