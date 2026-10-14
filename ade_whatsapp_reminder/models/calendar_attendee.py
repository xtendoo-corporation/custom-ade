import pytz

from odoo import api, fields, models

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
MESES = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
    "agosto", "septiembre", "octubre", "noviembre", "diciembre",
]  # fmt: skip


class CalendarAttendee(models.Model):
    _inherit = "calendar.attendee"

    ade_cita_texto = fields.Char(
        string="Fecha de la cita (texto)",
        compute="_compute_ade_cita_texto",
        help="Ej.: Lunes 28 de septiembre a las 18:00h. Se usa en el WhatsApp.",
    )

    @api.depends("event_id.start", "partner_id.tz")
    def _compute_ade_cita_texto(self):
        for attendee in self:
            start = attendee.event_id.start
            if not start:
                attendee.ade_cita_texto = False
                continue
            tz = pytz.timezone(attendee.partner_id.tz or "Europe/Madrid")
            local = pytz.utc.localize(start).astimezone(tz)
            attendee.ade_cita_texto = "%s %d de %s a las %s h" % (
                DIAS[local.weekday()],
                local.day,
                MESES[local.month - 1],
                local.strftime("%H:%M"),
            )
