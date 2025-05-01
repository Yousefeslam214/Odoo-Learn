from odoo import models, fields

class Owner(models.Model):
    _name = 'owner'
    name = fields.Char(required=1)
    phone = fields.Char()
    email = fields.Char()
    address = fields.Text()
    property_ids = fields.One2many('property', 'owner_id')
    tag_ids = fields.Many2many('tag')

