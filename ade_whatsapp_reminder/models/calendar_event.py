from odoo import api, models


class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    @api.model_create_multi
    def create(self, vals_list):
        default_alarms = self.env["calendar.alarm"].sudo().search(
            [("default_for_new_events", "=", True)]
        )
        if default_alarms:
            for vals in vals_list:
                if not vals.get("alarm_ids"):
                    vals["alarm_ids"] = [(6, 0, default_alarms.ids)]
        return super().create(vals_list)
