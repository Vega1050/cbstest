from odoo import api, fields, models, tools, _

class Company(models.Model):
    _inherit = "res.company"

    background_image = fields.Binary("Background Image")
    table_header = fields.Char("Table Header")
    footer_left = fields.Char("Footer Left Color")
    footer_right = fields.Char("Footer Right Color")
    terms = fields.Text('Technical Notes')