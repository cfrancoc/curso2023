from odoo import models, fields


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Módulo helpdesk ticket'

    name = fields.Char(
        string='Name',
        required=True,
    )
    sequence = fields.Integer(
        string='Sequence',
    )
    
    description = fields.Text(
        string='Description',
        help='Explain your problem'
    )
    date = fields.Date(
        string='Date'
    )
    date_limit = fields.Datetime(
        string='Date and Time limit',
        default=fields.Datetime.now,
    )
    assigned = fields.Boolean(
        string='Assigned',
        readonly=True 
    )
    actions_todo = fields.Html(
        string='Actions ToDo',
    )
    user_id = fields.Many2one(comodel_name='res.users', string="Assigned User", default=lambda self:self.env.user)
    state = fields.Selection(
        string='State',
        selection=[
            ('new', 'New'), 
            ('accepted', 'Accepted'),
            ('in_progress', 'In Progress'),
            ('pending', 'Pending'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled'),
        ],
        default='new'
    )
    