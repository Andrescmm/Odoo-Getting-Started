# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models
from dateutil.relativedelta import relativedelta

class RecurringPlan(models.Model):
    # Names
    _name = "estate.property"
    _description = "Estate Property"


    # Functions





    name = fields.Char(required = True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Datetime(copy = False, default=lambda self: self._default_date_availability() )
    expected_price = fields.Float(Required = True)
    selling_price = fields.Float("Selling Price", readonly = True, copy = False)
    bedrooms = fields.Integer(default = 2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden_Orientation',
        selection=[('north', 'North'), ('south', 'South'),('east', 'East'),('west', 'West')])
    active = fields.Boolean()
    status = fields.Selection(
        string='Status',
        selection=[('Offer Recieve', 'Offer Recieve'),('Offer Accepted', 'Offer Accepted'), ('Offer Rejected', 'Offer Rejected')])


