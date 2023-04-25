# Copyright <2023> Carlos Franco Cifuentes
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Carlos Franco",
    "summary": "Gestionado de incidencias",
    "version": "16.0.1.0.0",
    "development_status": "Alpha",
    "category": "Helpdesk",
    "website": "https://github.com/cfrancoc/curso2023",
    "author": "Carlos Franco Cifuentes, Odoo Community Association (OCA)",
    "maintainers": ["cfrancoc"],
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_views.xml",
        "views/main_menu.xml",
    ],
}