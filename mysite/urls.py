from django.contrib import admin
from django.urls import include, path

from rest_framework.urlpatterns import format_suffix_patterns

from polls.api import QuestionList, QuestionDetail, ChoiceList, ChoiceDetail
from rest_framework.authtoken import views as auth_views


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),

    # api snippet
    path('api/v1/polls/', QuestionList.as_view()),
    path('api/v1/polls/<int:pk>/', QuestionDetail.as_view()),

    # api snippet
    path('api/v1/choices/', ChoiceList.as_view()),
    path('api/v1/choices/<int:pk>/', ChoiceDetail.as_view()),


    path('api-token-auth/', auth_views.obtain_auth_token)


]


urlpatterns = format_suffix_patterns(urlpatterns)
