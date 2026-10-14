# Copyright (C) 2026 Dani Domínguez (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models

SERVICIO_SELECTION = [
    ("psicologia", "Psicología"),
    ("logopedia", "Logopedia"),
    ("pedagogia", "Pedagogía"),
    ("refuerzo_educativo", "Refuerzo educativo"),
]


class ResPartner(models.Model):
    _inherit = "res.partner"

    baja = fields.Boolean(string="Baja", default=False)
    numero_paciente = fields.Integer(string="Número paciente")
    datos_tutor = fields.Char(string="Datos tutor")
    dni_titular_factura = fields.Char(string="DNI titular factura")
    servicio = fields.Selection(SERVICIO_SELECTION, string="Servicio")
    numero_cuenta = fields.Char(string="Nº cuenta")
    observaciones_paciente = fields.Text(string="Observaciones")
    fecha_inicio_tratamiento = fields.Date(string="Fecha inicio tratamiento")
    fecha_fin_tratamiento = fields.Date(string="Fecha fin tratamiento")
    tipo_asistencia = fields.Char(string="Tipo de asistencia")
    precio_forma_pago = fields.Text(string="Precio sesión y forma de pago")
