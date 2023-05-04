from odoo import api, Command ,fields, models, _
from odoo.exceptions import UserError


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
        compute="_compute_assigned",
        search="_search_assigned",
        inverse='_inverse_assigned'
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

    tickets_count = fields.Integer(
        string="Tickets count",
        compute="_compute_tickets_count"
    )

    tag_name = fields.Char(
        string='tag_name',
    )

    @api.depends('user_id')
    def _compute_tickets_count(self):
        ticket = self.env["helpdesk.ticket"]        
        for record in self:
            tickets = ticket.search([{'user_id', '=', record.user_id.id}])
            record.tickets_count = len(tickets)

    def create_tag(self):
        self.ensure_one()
        # self.write({'tag_ids': [(0,0,{'name': self.tag_name})]})
        # self.write({'tag_ids': [Command.create({'name': self.tag_name})]})
        self.tag_ids = [Command.create({'name': self.tag_name})]

    def clear_tags(self):
        self.ensure_one()
        tag_ids = self.env['helpdesk.ticket.tag'].search([('name', '=', 'otra')])
        # self.write({'tag_ids': [
        #     (5,0,0),
        #     (6,0,tag_ids.ids)]})
        self.tag_ids = [
            Command.clear(),
            Command.set(tag_ids.ids)
        ]
        
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

    def _search_assigned(self, operator, value):
        if operator not in ('=', '!=') or not isinstance(value, bool):
            raise UserError(_("Operation not supported"))
        if operator == '=' and value == True:
            operator = '!='
        else:
            operator = '='
        return [('user_id', operator, False)]

    @api.depends('user_id')
    def _compute_assigned(self):
        for record in self:
            record.assigned = bool(record.user_id)

    def _inverse_assigned(self):
        for record in self:
            if not record.assigned:
                record.user_id = False
            else:
                record.user_id = self.env.user