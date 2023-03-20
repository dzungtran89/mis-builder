CREATE OR REPLACE VIEW mis_account_move_line AS (
    SELECT
        aal.id,
        aal.company_id,
        aal.date,
        aal.name,
        aal.general_account_id as account_id,
        aal.account_id as analytic_account_id,
        aal.plan_id,
        aa.root_plan_id,
        CASE
            WHEN amount < 0 THEN -amount
            ELSE 0
        END AS debit,
        CASE
            WHEN amount >= 0 THEN amount
            ELSE 0
        END AS credit,
        aml.parent_state,
        aal.move_line_id AS res_id,
        'mis.account.move.line' AS res_model

    FROM account_analytic_line aal
        JOIN account_move_line aml on aml.id = aal.move_line_id
        JOIN account_analytic_account aa on aa.id = aal.account_id
)
