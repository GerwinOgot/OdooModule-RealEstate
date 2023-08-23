# -*- coding: utf-8 -*-
from odoo import models, fields,api


class RealEstate(models.Model):
    _name = "estate.model"
    _description = "Estate Model"

    name = fields.Char(string='House Name', required=True)
    description = fields.Text(string='House Description')
    postcode = fields.Char(string=' House Post Code')
    date_availability = fields.Datetime(string=' Hoouse Date Available', copy=False)
    expected_price = fields.Float(string=' House Expected Price', required=True)
    selling_price = fields.Float(string='House Selling Price', readonly=True, copy=False, default=200000)
    bedrooms = fields.Integer(string='Bedrooms', default=2)
    living_room = fields.Integer(string='Living Area (sqm)')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden_area = fields.Integer(string='Garden Area')
    swimming_pool = fields.Boolean(string='Swimming Pool')
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')], help="Direction is where the garden is facing.")
    active = fields.Boolean(string='Active Contract', default=True)
    state = fields.Selection(
        string='Contract State',
        selection=[
            ('new', 'New'),
            ('offer received', 'Offer Received'),
            ('offer accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled')
        ], default='new'
    )
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)

    @api.depends('expected_price', 'selling_price')
    def _compute_total_amount(self):
        for estate in self:
            estate.total_amount = estate.expected_price + estate.selling_price

