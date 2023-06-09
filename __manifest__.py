{
    'name': "Real State",
    'version': '1.0',
    'depends': ['base'],
    'author': "Inka Labs",
    'website': "https://inka-labs.com/",
    'category': 'Sales/state',
    "depends": [
        "base",
        "web",
    ],

    'data': [
     'security/ir.model.access.csv',
     'views/estate_property_offer_views.xml',
     'views/estate_property_tag_views.xml',
     'views/estate_property_type_views.xml',
     'views/estate_property_views.xml',
     'views/res_users_views.xml',
     'views/estate_menus.xml',
    ],
    "application": True,
}