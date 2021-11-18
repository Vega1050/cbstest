{
    'name': "Project Sales Report",
    'summary': """Extended version of sales report""",
    'description': """Extended version of sales report""",
    'author': "Suraj Rawat",
    'category': 'Sales',
    'version': '1.1',
    'depends': ['base', 'sale', 'web_widget_colorpicker','sale_management', 'report_qweb_element_page_visibility', 'web'],
    'data': [
        'data/report_paperformat.xml',
        'report/sale_report.xml',
        'views/sale_report_templates.xml',
        'views/res_company_views.xml',
    ],
    'icon_image': 'static/description/icon.png',
}
