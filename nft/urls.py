from rest_framework import routers
from nft.views import ProductViewSet, CollectionViewSet, AccountViewSet

router = routers.DefaultRouter()
router.register('Product', ProductViewSet)
router.register('Collection', CollectionViewSet)
router.register('Account', AccountViewSet)
