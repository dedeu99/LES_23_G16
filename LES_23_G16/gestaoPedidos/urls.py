"""LES_23_G16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import consultar_pedidos,criar_pedido_horario,alterar_pedido_horario,apagar_pedido_horario,criar_pedido_outro,alterar_pedido_outros,apagar_pedido_outro,criar_pedido_uc,alterar_pedido_uc,apagar_pedido_uc

app_name = 'gestaoPedidos'

urlpatterns = [
    path("consultar_pedidos",consultar_pedidos.as_view(), name="consultar_pedidos"),
	path("criar_pedido_horario",criar_pedido_horario, name="criar_pedido_horario"),
    path("alterar_pedido_horario",alterar_pedido_horario, name="alterar_pedido_horario"),
    path("apagar_pedido_horario",apagar_pedido_horario, name="apagar_pedido_horario"),
    path("criar_pedido_outro",criar_pedido_outro, name="criar_pedido_outro"),
    path("alterar_pedido_outros",alterar_pedido_outros, name="alterar_pedido_outros"),
    path("apagar_pedido_outro",apagar_pedido_outro, name="apagar_pedido_outro"),
    path("criar_pedido_uc",criar_pedido_uc, name="criar_pedido_uc"),
    path("alterar_pedido_uc",alterar_pedido_uc, name="alterar_pedido_uc"),
    path("apagar_pedido_uc",apagar_pedido_uc, name="apagar_pedido_uc")
]
