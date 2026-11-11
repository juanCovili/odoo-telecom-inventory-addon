# -*- coding: utf-8 -*-
{
    'name': 'Gestión de Equipamiento de Telecomunicaciones y Enlaces',
    'version': '17.0.1.0.0',
    'category': 'Operations/Inventory',
    'summary': 'Control de inventario, números de serie, asignaciones de routers, ONUs y antenas para empresas de telecomunicaciones.',
    'description': """
Módulo personalizado de Odoo para el control y trazabilidad de equipamiento técnico:
- Registro de números de serie y direcciones MAC.
- Clasificación por tipo de equipo (Router, ONU Fibra, Switch, Antena, CCTV).
- Estados de ciclo de vida (En Bodega, Asignado a Técnico, Instalado en Cliente, En Reparación).
- Fechas de instalación y vigencia de garantías.
    """,
    'author': 'Juan Andrés Covili Cabezas',
    'website': 'https://juancovili.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/telecom_device_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
