from rest_framework.routers import DefaultRouter
from app.api.views import FacturasApiViewSet

router_app = DefaultRouter()

router_app.register(prefix='Facturas', basename='Facturas', viewset=FacturasApiViewSet)

urlpatterns = router_app.urls