from rest_framework import routers
from nft.views import ProductViewSet, CollectionViewSet, AccountViewSet

# Create routers
router = routers.DefaultRouter()
router.register('Product', ProductViewSet)
router.register('Collection', CollectionViewSet)
router.register('Account', AccountViewSet)
