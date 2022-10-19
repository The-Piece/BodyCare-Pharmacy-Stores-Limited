# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Account Asset Extension',
    'license': 'Other proprietary',
    'price' : 9.0,
    'currency': 'EUR',
    'version' : '3.1.2',
    'category': 'Accounting',
    'summary' : 'This module will add some more fields on Account Asset.',
    'description': """
Odoo Account Asset Extend
Asset Employee
Asset User
Asset Manager
Warranty Information for Asset
Asset Warranty Information
Asset Warranty Details
Asset Pivot Report
account asset

            """,
    'author' : 'Probuse Consulting Service Pvt. Ltd.',
    'website' : 'www.probuse.com',
    'support': 'contact@probuse.com',
    'images': ['static/description/img_1.jpg'],
    'live_test_url': 'https://probuseappdemo.com/probuse_apps/odoo_account_asset_extend/624',
    'depends' : [
        'account',
        'purchase',
        'maintenance',
        'account_asset',
        'hr',
    ],
    'data' : [
        'data/asset_sequence.xml',
        'views/asset_view.xml',
        'security/res_group.xml',
        'views/asset_menu_view.xml',
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
