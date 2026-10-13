from odoo import fields, models


class CalendarAlarm(models.Model):
    _inherit = "calendar.alarm"

    default_for_new_events = fields.Boolean(
        string="Por defecto en citas nuevas",
        help="Esta alarma se añade automáticamente a las citas nuevas "
        "(también las sincronizadas desde Google) que no traigan alarmas.",
    )
