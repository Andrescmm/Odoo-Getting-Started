# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models



class EstatePropertyOffer(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"

    price = fields.Float("Price", required=True)

    state = fields.Selection(
        selection=[
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ],
        string="Status",
        copy=False,
        default=False,
    )

    # Relational
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    


