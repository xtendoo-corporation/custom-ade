{
    'name': 'Ade WhatsApp Reminder',
    'version': '19.0.1.1.0',
    'category': 'Calendar',
    'summary': 'Recordatorio por WhatsApp de las citas del calendario.',
    'description': """
        Envía por WhatsApp un recordatorio de las citas del calendario de Odoo
        (sincronizado con Google) a los pacientes de Ade Intervención.

        Características:
        - Plantilla de WhatsApp con la fecha y hora de la cita en negrita
        - Alarmas de WhatsApp 24 horas y 2 horas antes
        - Alarma por defecto en las citas nuevas, también las sincronizadas desde Google
    """,
    'author': 'Manuel Calero, Xtendoo',
    'website': 'https://www.xtendoo.com',
    'license': 'LGPL-3',
    'depends': [
        'calendar',
        'whatsapp_calendar',
    ],
    'data': [
        'data/whatsapp_template_data.xml',
        'data/calendar_alarm_data.xml',
        'views/calendar_alarm_views.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
