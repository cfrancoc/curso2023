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
        default=10,
        help="Secuencia para el orden de las incidencias."
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
    
    tag_ids = fields.Many2many(
        string='Tags',
        comodel_name='helpdesk.ticket.tag',
    )
    
    action_ids = fields.One2many(
        string='Actions',
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
    )  
    
    color = fields.Integer(
        string='color',
        default=0,
    )

    amount_time = fields.Float(
        string='Amount Time',
    )

    person_id = fields.Many2one(
        string='Person',
        comodel_name='res.partner',
        domain=[("is_company", "=", False)]
    )
    
    
    def update_one_description(self):
        self.ensure_one()
        self.description += "OK"

    def update_all_description(self):
        """ all_tickets = self.env["helpdesk.ticket"].search([]) """
        all_tickets = self.search([])
        for record in all_tickets:
            record.update_one_description()

    def set_actions_as_done(self):
        self.ensure_one()
        self.action_ids.set_done()

    