from odoo import models, fields


class HelpdeskTicketTag(models.Model):
    _name = 'helpdesk.ticket.tag'
    _description = 'Módulo helpdesk ticket tag'

    name = fields.Char()

    """ ticket_id = fields.Many2one(
        string='Ticket',
        comodel_name='helpdesk.ticket',
    ) """
    