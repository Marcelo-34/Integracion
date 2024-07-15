# app/api/router.py

from rest_framework.routers import DefaultRouter
from app.api.views import FacturasApiViewSet, BacturaApiViewSetactura

router = DefaultRouter()
router_app_B = DefaultRouter()

router.register(prefix='Facturas', basename='Facturas', viewset=FacturasApiViewSet)
router.register(prefix='Boleta', basename='Boleta', viewset=BacturaApiViewSetactura)

router_app = router
