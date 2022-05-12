from rest_framework import routers
from nft.views import ProductViewSet, CollectionViewSet, RegisterViewSet

router = routers.DefaultRouter()
router.register('Product', ProductViewSet)
router.register('Collection', CollectionViewSet)
router.register('Register', RegisterViewSet)
