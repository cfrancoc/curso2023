from odoo import models, fields


class HelpdeskTicketAction(models.Model):
    _name = 'helpdesk.ticket.action'
    _description = 'Módulo helpdesk ticket action'

    name = fields.Char(
        string='Name',
        required=True,
    )
    
    state = fields.Selection(
        string='State',
        selection=[
            ('todo', 'To Do'), 
            ('done', 'Done')
        ],
        default="todo"
    )

    ticket_id = fields.Many2one(
        string='Ticket',
        comodel_name='helpdesk.ticket',
    )

    def set_all_done(self):
        all_actions = self.search([])
        for record in all_actions:
            record.state = "done"