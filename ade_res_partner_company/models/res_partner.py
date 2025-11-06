from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    related_company_id = fields.Many2one(
        'res.partner',
        string='Compañía relacionada',
        domain="[('is_company', '=', True)]"
    )
