from odoo import fields, models, tools
from odoo.modules.module import get_module_resource


class MisAccountMoveLine(models.Model):
    _name = "mis.account.move.line"
    _description = "MIS Account Move Line"
    _auto = False

    name = fields.Char()
    account_id = fields.Many2one("account.account")
    company_id = fields.Many2one("res.company")
    credit = fields.Float()
    debit = fields.Float()
    date = fields.Date()
    analytic_account_id = fields.Many2one(
        "account.analytic.account", "Analytic Account"
    )

    def init(self):
        with open(
            get_module_resource(
                "mis_builder",
                "datas",
                "mis_account_move_line.sql",
            )
        ) as f:
            tools.drop_view_if_exists(self.env.cr, "mis_account_move_line")
            self.env.cr.execute(f.read())
