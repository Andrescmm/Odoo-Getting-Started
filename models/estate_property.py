# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    # Names
    _name = "estate.property"
    _description = "Estate Property"


    # Functions


    def _default_date_availability(self):
        return fields.Date.context_today(self) + relativedelta(months=3)


    name = fields.Char(required = True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Datetime(copy = False, default=lambda self: self._default_date_availability() )
    expected_price = fields.Float(Required = True)
    selling_price = fields.Float("Selling Price", readonly = True, copy = False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string="Garden Area (sqm)")
    garden_orientation = fields.Selection(
        string='Garden_Orientation',
        selection=[('north', 'North'), ('south', 'South'),('east', 'East'),('west', 'West')])
    active = fields.Boolean()

    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )


    # Relational
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")

    ## De muchos a uno
    # User can be an employee
    user_id = fields.Many2one("res.users", string="Salesman", default=lambda self: self.env.user)
    # Buyer can be anyone
    buyer_id = fields.Many2one("res.partner", string="Buyer", readonly=True, copy=False)

    ## De muchos a muchos
    tag_ids = fields.Many2many("estate.property.tag", string="Property Tag")

    #De uno a muchos 
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")


