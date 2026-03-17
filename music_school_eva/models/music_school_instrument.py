from odoo import models, fields


class MusicSchoolInstrument(models.Model):
    _name = 'music.school.instrument'
    _description = 'Instruments'
    _order = 'name desc'

    active = fields.Boolean(string="Active", default=True)
    name = fields.Char(string="Name", required=True, translate=True)
    family_id = fields.Many2one(
        comodel_name='music.school.instrument.family',
        string="Family",
        help="Family of the instrument"
    )
    description = fields.Text(string="Description")
    last_maintenance_date = fields.Date(
        string="Last Maintenance Date",
        help="Date of the last maintenance performed on the instrument"
    )

    is_repaired = fields.Boolean(
        string="Is Repaired",
        compute='_compute_is_repaired',
        inverse='_set_is_repaired',

    )