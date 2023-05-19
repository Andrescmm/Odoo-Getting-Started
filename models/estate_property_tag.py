# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models


class EstatePropertyTag(models.Model):
    # Names
    _name = "estate.property.tag"
    _description = "Estate Property Tag"
    _order = "name"

    #SQL Constrains

    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique"),
    ]


    name = fields.Char(required = True)
    color = fields.Integer("Color Index")
    


