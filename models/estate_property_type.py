# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models


class EstatePropertyType(models.Model):
    # Names
    _name = "estate.property.type"
    _description = "Estate Property type"


    name = fields.Char(required = True)
    


