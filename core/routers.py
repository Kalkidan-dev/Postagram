from rest_framework import routers
from rest_framework_nested import routers
from core.user.viewsets import UserViewSet
from core.auth.viewsets import RegisterViewSet,LoginViewSet,RefreshViewSet
from core.post.viewsets import PostViewSet

router = routers.SimpleRouter()

# ##################################################################### #
# ################### USER                       ###################### #
# ##################################################################### #

router.register(r'user', UserViewSet, basename='user')
# ##################################################################### #
# ################### AUTH                       ###################### #
# ##################################################################### #

router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

###  post  ###

router.register(r'post', PostViewSet, basename='post')

urlpatterns = [
    *router.urls,
]
