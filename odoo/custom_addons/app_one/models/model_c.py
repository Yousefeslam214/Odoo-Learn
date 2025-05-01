from odoo import models, fields
class ModelC(models.AbstractModel):
    _name = 'model_c'
    # _description = 'Model A'
    # model_a_ids = fields.One2many('your.model.a', 'model_a_id', string="Model A")

    # name = fields.Char(string='Name', required=True)
    # description = fields.Text(string='Description')
    # model_b_ids = fields.One2many('app_one.model_b', 'model_a_id', string='Model B Records')
    # model_c_ids = fields.One2many('app_one.model_c', 'model_a_id', string='Model C Records')