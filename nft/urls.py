from rest_framework import routers
from nft.views import ProductViewSet, CollectionViewSet, AccountViewSet

# import routers class from rest_framework
router = routers.DefaultRouter()
router.register('Product', ProductViewSet)
router.register('Collection', CollectionViewSet)
router.register('Account', AccountViewSet)
