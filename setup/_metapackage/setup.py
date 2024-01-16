import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-survey",
    description="Meta package for oca-survey Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-partner_survey>=15.0dev,<15.1dev',
        'odoo-addon-survey_contact_generation>=15.0dev,<15.1dev',
        'odoo-addon-survey_crm_generation>=15.0dev,<15.1dev',
        'odoo-addon-survey_crm_sale_generation>=15.0dev,<15.1dev',
        'odoo-addon-survey_legal>=15.0dev,<15.1dev',
        'odoo-addon-survey_multi_company>=15.0dev,<15.1dev',
        'odoo-addon-survey_placeholder>=15.0dev,<15.1dev',
        'odoo-addon-survey_resource_booking>=15.0dev,<15.1dev',
        'odoo-addon-survey_result_mail>=15.0dev,<15.1dev',
        'odoo-addon-survey_sale_generation>=15.0dev,<15.1dev',
        'odoo-addon-survey_skip_start>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
