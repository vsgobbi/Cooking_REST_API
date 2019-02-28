from django.conf.urls import include, url
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from .views import RecipeView, IngredientView, CookerCRUD, CookerView

router = DefaultRouter()

router.register(r'ingredients', IngredientView)
router.register(r'recipes', RecipeView)
router.register(r'cooker', CookerView)
app_name = 'core'
urlpatterns = [

    #url(r'^$', include(router.urls)),
    url(r'^path/to/API/', include('rest_framework.urls', namespace='widget-api')),
    path('cooker/id/<int:pk>', CookerCRUD.as_view(), name='cooker'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #path(r'cooker/id/<int:pk>', CookerCRUD.as_view(), name='cooker'),
    #url(r'^api/', include('rest_framework.urls', 'rest_framework')),
]
urlpatterns += router.urls

