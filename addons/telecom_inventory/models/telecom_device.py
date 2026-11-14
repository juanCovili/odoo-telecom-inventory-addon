# -*- coding: utf-8 -*-
# @project   Odoo Telecom Inventory & Network Devices Addon
# @author    Juan Covili <https://github.com/juanCovili>
# @repo      https://github.com/juanCovili/odoo-telecom-inventory-addon
# @portfolio https://juancovili.com
# @copyright Copyright (c) 2026 Juan Covili. Todos los derechos reservados.
__author__ = "Juan Covili"
__github__ = "https://github.com/juanCovili"
__portfolio__ = "https://juancovili.com"
from odoo import models, fields, api

class TelecomDevice(models.Model):
    _name = 'telecom.device'
    _description = 'Equipamiento de Telecomunicaciones y Enlaces'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    name = fields.Char(string='Modelo / Nombre del Equipo', required=True, tracking=True)
    serial_number = fields.Char(string='Número de Serie (S/N)', required=True, index=True, copy=False, tracking=True)
    mac_address = fields.Char(string='Dirección MAC', tracking=True)
    
    device_type = fields.Selection([
        ('onu', 'ONU / ONT Fibra Óptica'),
        ('router', 'Router / Gateway WiFi'),
        ('switch', 'Switch Administrable'),
        ('antenna', 'Antena Enlace Punto a Punto'),
        ('cctv', 'Cámara CCTV / Seguridad IP'),
        ('media_converter', 'Conversor de Medios'),
    ], string='Tipo de Dispositivo', required=True, default='router', tracking=True)

    status = fields.Selection([
        ('in_stock', 'Disponible en Bodega'),
        ('assigned', 'Asignado a Cuadrilla Técnica'),
        ('installed', 'Instalado en Cliente'),
        ('maintenance', 'En Diagnóstico / Taller'),
        ('scrapped', 'Baja Técnica / Defectuoso'),
    ], string='Estado Operativo', required=True, default='in_stock', tracking=True)

    partner_id = fields.Many2one('res.partner', string='Cliente / Destino', tracking=True)
    technician_id = fields.Many2one('res.users', string='Técnico Responsable', tracking=True)
    
    installation_date = fields.Date(string='Fecha de Instalación', tracking=True)
    warranty_expire_date = fields.Date(string='Vencimiento Garantía')
    
    ip_address = fields.Char(string='Dirección IP Asignada')
    notes = fields.Text(string='Observaciones Técnicas')

    _sql_constraints = [
        ('serial_unique', 'unique(serial_number)', '¡El número de serie ingresado ya se encuentra registrado en el sistema!')
    ]

    def action_set_in_stock(self):
        self.write({'status': 'in_stock'})

    def action_set_installed(self):
        self.write({'status': 'installed', 'installation_date': fields.Date.today()})
