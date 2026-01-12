{
    "name": "Ade Groups and Attendance",
    "summary": "Adds groups for contacts and attendance register.",
    "version": "19.0.1",
    "category": "Contact",
    "author": "Manuel Calero, Abraham Carrasco, Xtendoo",
    "license": "LGPL-3",
    "application": True,
    "depends": [
        "base",
        "contacts",
        "ade_extend_res_partner",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/contact_groups_view.xml",
        "views/attendance_record_view.xml",
    ],
    "installable": True,
}
