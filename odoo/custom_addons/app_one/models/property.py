from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Property(models.Model):
    _name = 'property'
    name = fields.Char(required=1)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer(required=True, default=1)
    living_area = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(default=0)
    owner_id = fields.Many2one('owner', string='Owner')
    tag_ids = fields.Many2many('tag')

    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ])
    
    # , string='Garden Orientation')

    _sql_constraints = [
    ('unique_name', 'unique("name")', 'The property name must be unique.'),
    ('check_garden_area', 'CHECK(garden_area >= 0)', 'Garden area must be a positive value or zero.')
]


    @api.constrains('bedrooms')
    def _check_bedrooms(self):
        for record in self:
            if record.bedrooms < 1:
                raise ValidationError("Number of bedrooms must be at least 1.")
            if record.bedrooms > 10:
                raise ValidationError("Number of bedrooms cannot exceed 10.")


    @api.model_create_multi
    def create(self, vals):
        res = super(Property, self).create(vals)
        print("Property created:", res)
        return res