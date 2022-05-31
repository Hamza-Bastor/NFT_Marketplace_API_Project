from rest_framework import routers
from nft.views import ProductViewSet, CollectionViewSet, AccountViewSet

# Use a routers class
router = routers.DefaultRouter()
router.register('Product', ProductViewSet)
router.register('Collection', CollectionViewSet)
router.register('Account', AccountViewSet)
