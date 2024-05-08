import numpy as np
import ast

class ReportContentParser:

    def parse(self, template_id, content_string):

        content = ast.literal_eval(content_string)
        
        tables_content = content.get('tabulky')
        if tables_content is None:
            print('DOES NOT CONTAIN TABLES')
            return

        primary_features = []
        if template_id == 687: primary_features = self.__parse_MUJ(tables_content)
        if template_id == 699: primary_features = self.__parse_POD(tables_content)         
        if template_id == 21: primary_features = self.__parse_POD_1(tables_content)        
        if template_id == 22: primary_features = self.__parse_POD_2(tables_content)

        return primary_features
    
    
    def __parse_MUJ(self, tables_content):
        # 687

        assets = tables_content[0]['data']
        assets = np.reshape(np.array(assets), (len(assets)//2, 2))[:, 0]
        assets[assets=='']='0'
        assets = assets.astype(float)

        liab = tables_content[1]['data']
        liab = np.reshape(np.array(liab), (len(liab)//2, 2))[:, 0]
        liab[liab=='']='0'
        liab = liab.astype(float)

        balance_sheet = np.concatenate([assets, liab])

        income = tables_content[2]['data']
        income = np.reshape(np.array(income), (len(income)//2, 2))[:, 0]
        income[income=='']='0'
        income = income.astype(float)

        profit_and_loss = income

        total_assets = balance_sheet[0] # total_assets
        non_current_assets = balance_sheet[1] # non_current_assets
        intangible_assets = balance_sheet[2] # intangible_assets
        total_non_current_tangible_assets = balance_sheet[3] # total_non_current_tangible_assets
        land_and_buildings = balance_sheet[4] # land_and_buildings
        separate_movable_assets_and_sets_of_movable_assets = balance_sheet[5] # separate_movable_assets_and_sets_of_movable_assets
        other_long_term_tangible_assets = balance_sheet[6] # other_long_term_tangible_assets
        adjustment_item_for_acquired_assets = balance_sheet[7] # adjustment_item_for_acquired_assets
        total_long_term_financial_assets = balance_sheet[8] # total_long_term_financial_assets
        bank_balances_with_maturity_longer_than_one_year = balance_sheet[11] # bank_balances_with_maturity_longer_than_one_year
        current_assets = balance_sheet[13] # current_assets
        inventories = balance_sheet[14] # inventories
        long_term_receivables = balance_sheet[15] # long_term_receivables
        total_short_term_receivables = balance_sheet[16] # total_short_term_receivables
        trade_receivables = balance_sheet[17] # trade_receivables
        social_security_tax_receivables_and_grants = balance_sheet[18] # social_security_tax_receivables_and_grants
        financial_assets = balance_sheet[20] # financial_assets
        other_financial_accounts = balance_sheet[22] # other_financial_accounts
        cash_and_bank_balances = balance_sheet[21] # cash_and_bank_balances


        total_owners_equity_and_liabilities=balance_sheet[23] # total_owners_equity_and_liabilities
        owners_equity=balance_sheet[24] # owners_equity
        share_capital=balance_sheet[25] # share_capital
        share_capital_and_changes_in_share_capital=balance_sheet[26] # share_capital_and_changes_in_share_capital
        claims_for_subscribed_owners_equity=balance_sheet[27] # claims_for_subscribed_owners_equity
        capital_funds=balance_sheet[28]+balance_sheet[29] # capital_funds

        valuation_differences=balance_sheet[30] # valuation_differences

        undivided_profit_or_unpaid_loss_from_previous_years=balance_sheet[31] # undivided_profit_or_unpaid_loss_from_previous_years
        profit_for_the_reporting_period_after_tax=balance_sheet[32] # profit_for_the_reporting_period_after_tax
        liabilities=balance_sheet[33] # liabilities
        long_term_liabilities_excluding_reserves_and_loans=balance_sheet[34] # long_term_liabilities_excluding_reserves_and_loans
        long_term_reserves=balance_sheet[35] # long_term_reserves
        long_term_bank_loans=balance_sheet[36] # long_term_bank_loans
        total_short_term_liabilities_excluding_reserves_loans_and_advances=balance_sheet[37] # total_short_term_liabilities_excluding_reserves_loans_and_advances
        short_term_trade_liabilities=balance_sheet[38] # short_term_trade_liabilities
        liabilities_to_employees_and_social_insurance=balance_sheet[39] # liabilities_to_employees_and_social_insurance

        tax_liabilities_and_grants=balance_sheet[40] # tax_liabilities_and_grants
        short_term_reserves=balance_sheet[42] # short_term_reserves
        current_bank_loans=balance_sheet[43] # current_bank_loans
        short_term_financial_assistance=balance_sheet[44] # short_term_financial_assistance


        total_operating_revenues=profit_and_loss[0] # total_operating_revenues
        sales_revenue=profit_and_loss[1] # sales_revenue
        revenue_from_the_sale_of_own_products_and_services=profit_and_loss[2] # revenue_from_the_sale_of_own_products_and_services
        change_in_intra_organizational_inventories=profit_and_loss[3] # change_in_intra_organizational_inventories
        activation=profit_and_loss[4] # activation
        revenue_from_the_sale_of_long_term_intangible_assets_long_term_tangible_assets_and_materials=profit_and_loss[5] # revenue_from_the_sale_of_long_term_intangible_assets_long_term_tangible_assets_and_materials
        other_revenues_from_operating_activities=profit_and_loss[6] # other_revenues_from_operating_activities
        total_operating_costs=profit_and_loss[7] # total_operating_costs
        costs_incurred_to_acquire_sold_goods=profit_and_loss[8] # costs_incurred_to_acquire_sold_goods
        consumption_of_materials_energy_and_other_non_inventory_supplies=profit_and_loss[9] # consumption_of_materials_energy_and_other_non_inventory_supplies
        services=profit_and_loss[10] # services
        personnel_costs=profit_and_loss[11] # personnel_costs
        taxes_and_fees=profit_and_loss[12] # taxes_and_fees
        depreciation_and_adjustments_to_long_term_intangible_assets_and_long_term_tangible_assets=profit_and_loss[13] # depreciation_and_adjustments_to_long_term_intangible_assets_and_long_term_tangible_assets
        remaining_cost_of_sold_long_term_assets_and_materials=profit_and_loss[14] # remaining_cost_of_sold_long_term_assets_and_materials
        adjustments_to_receivables=profit_and_loss[15] # adjustments_to_receivables
        other_costs_of_operating_activities=profit_and_loss[16] # other_costs_of_operating_activities
        operating_result_from_operating_activities=profit_and_loss[17] # operating_result_from_operating_activities
        value_added=profit_and_loss[18] # value_added
        total_financial_revenues=profit_and_loss[19] # total_financial_revenues
        revenue_from_the_sale_of_securities_and_shares=profit_and_loss[20] # revenue_from_the_sale_of_securities_and_shares
        revenue_from_long_term_financial_assets=profit_and_loss[21] # revenue_from_long_term_financial_assets
        revenue_from_short_term_financial_assets=profit_and_loss[22] # revenue_from_short_term_financial_assets
        interest_income=profit_and_loss[23] # interest_income
        exchange_gains=profit_and_loss[24] # exchange_gains
        other_revenues_from_financial_activities=profit_and_loss[25] # other_revenues_from_financial_activities
        total_financial_costs=profit_and_loss[26] # total_financial_costs
        sale_of_securities_and_shares=profit_and_loss[27] # sale_of_securities_and_shares
        costs_of_short_term_financial_assets=profit_and_loss[28] # costs_of_short_term_financial_assets
        adjustments_to_financial_assets=profit_and_loss[29] # adjustments_to_financial_assets
        interest_expenses=profit_and_loss[30] # interest_expenses
        exchange_losses=profit_and_loss[31] # exchange_losses
        other_costs_of_financial_activities=profit_and_loss[32] # other_costs_of_financial_activities
        financial_result=profit_and_loss[33] # financial_result
        result_of_operations_for_the_reporting_period_before_tax=profit_and_loss[34] # result_of_operations_for_the_reporting_period_before_tax
        income_tax=profit_and_loss[35] # income_tax
        transfer_of_shares_in_the_result_to_shareholders=profit_and_loss[36] # transfer_of_shares_in_the_result_to_shareholders
        result_of_operations_for_the_reporting_period_after_tax=profit_and_loss[37] # result_of_operations_for_the_reporting_period_after_tax


        values = [
            total_assets,
            non_current_assets,
            intangible_assets,
            total_non_current_tangible_assets,
            land_and_buildings,
            separate_movable_assets_and_sets_of_movable_assets,
            other_long_term_tangible_assets,
            adjustment_item_for_acquired_assets,
            total_long_term_financial_assets,
            bank_balances_with_maturity_longer_than_one_year,
            current_assets,
            inventories,
            long_term_receivables,
            total_short_term_receivables,
            trade_receivables,
            social_security_tax_receivables_and_grants,
            financial_assets,
            other_financial_accounts,
            cash_and_bank_balances,
            total_owners_equity_and_liabilities,
            owners_equity,
            share_capital,
            share_capital_and_changes_in_share_capital,
            claims_for_subscribed_owners_equity,
            capital_funds,
            valuation_differences,
            undivided_profit_or_unpaid_loss_from_previous_years,
            profit_for_the_reporting_period_after_tax,
            liabilities,
            long_term_liabilities_excluding_reserves_and_loans,
            long_term_reserves,
            long_term_bank_loans,
            total_short_term_liabilities_excluding_reserves_loans_and_advances,
            short_term_trade_liabilities,
            liabilities_to_employees_and_social_insurance,
            tax_liabilities_and_grants,
            short_term_reserves,
            current_bank_loans,
            short_term_financial_assistance,
            total_operating_revenues,
            sales_revenue,
            revenue_from_the_sale_of_own_products_and_services,
            change_in_intra_organizational_inventories,
            activation,
            revenue_from_the_sale_of_long_term_intangible_assets_long_term_tangible_assets_and_materials,
            other_revenues_from_operating_activities,
            total_operating_costs,
            costs_incurred_to_acquire_sold_goods,
            consumption_of_materials_energy_and_other_non_inventory_supplies,
            services,
            personnel_costs,
            taxes_and_fees,
            depreciation_and_adjustments_to_long_term_intangible_assets_and_long_term_tangible_assets,
            remaining_cost_of_sold_long_term_assets_and_materials,
            adjustments_to_receivables,
            other_costs_of_operating_activities,
            operating_result_from_operating_activities,
            value_added,
            total_financial_revenues,
            revenue_from_the_sale_of_securities_and_shares,
            revenue_from_long_term_financial_assets,
            revenue_from_short_term_financial_assets,
            interest_income,
            exchange_gains,
            other_revenues_from_financial_activities,
            total_financial_costs,
            sale_of_securities_and_shares,
            costs_of_short_term_financial_assets,
            adjustments_to_financial_assets,
            interest_expenses,
            exchange_losses,
            other_costs_of_financial_activities,
            financial_result,
            result_of_operations_for_the_reporting_period_before_tax,
            income_tax,
            transfer_of_shares_in_the_result_to_shareholders,
            result_of_operations_for_the_reporting_period_after_tax
        ]
        
        return values
    
    def __parse_POD(self, tables_content):
        # 699
        assets = tables_content[0]['data']
        assets = np.reshape(np.array(assets), (len(assets)//4, 4))[:, 2]
        assets[assets=='']='0'
        assets = assets.astype(float)

        liab = tables_content[1]['data']
        liab = np.reshape(np.array(liab), (len(liab)//2, 2))[:, 0]
        liab[liab=='']='0'
        liab = liab.astype(float)

        balance_sheet = np.concatenate([assets, liab])

        income = tables_content[2]['data']
        income = np.reshape(np.array(income), (len(income)//2, 2))[:, 0]
        income[income=='']='0'
        income = income.astype(float)

        profit_and_loss = income

        total_assets=balance_sheet[0] # total_assets
        non_current_assets=balance_sheet[1] # non_current_assets
        intangible_assets=balance_sheet[2] # intangible_assets
        total_non_current_tangible_assets=balance_sheet[10] # total_non_current_tangible_assets
        land_and_buildings=balance_sheet[11]+balance_sheet[12] # land_and_buildings
        separate_movable_assets_and_sets_of_movable_assets=balance_sheet[13] # separate_movable_assets_and_sets_of_movable_assets
        other_long_term_tangible_assets=balance_sheet[16] # other_long_term_tangible_assets
        adjustment_item_for_acquired_assets=balance_sheet[19] # adjustment_item_for_acquired_assets
        total_long_term_financial_assets=balance_sheet[20] # total_long_term_financial_assets
        bank_balances_with_maturity_longer_than_one_year=balance_sheet[29] # bank_balances_with_maturity_longer_than_one_year
        current_assets=balance_sheet[32] # current_assets
        inventories=balance_sheet[33] # inventories
        long_term_receivables=balance_sheet[40] # long_term_receivables
        total_short_term_receivables=balance_sheet[52] # total_short_term_receivables
        trade_receivables=balance_sheet[53] # trade_receivables
        social_security_tax_receivables_and_grants=balance_sheet[61]+balance_sheet[62] # social_security_tax_receivables_and_grants
        financial_assets=balance_sheet[65]+balance_sheet[70] # financial_assets
        other_financial_accounts=balance_sheet[65] # other_financial_accounts
        cash_and_bank_balances=balance_sheet[70] # cash_and_bank_balances
        total_owners_equity_and_liabilities=balance_sheet[78] # total_owners_equity_and_liabilities
        owners_equity=balance_sheet[79] # owners_equity
        share_capital=balance_sheet[80] # share_capital
        share_capital_and_changes_in_share_capital=balance_sheet[81]+balance_sheet[82] # share_capital_and_changes_in_share_capital
        claims_for_subscribed_owners_equity=balance_sheet[83] # claims_for_subscribed_owners_equity
        capital_funds=balance_sheet[84]+balance_sheet[85]+balance_sheet[86]+balance_sheet[89]+balance_sheet[92] # capital_funds
        valuation_differences=balance_sheet[94]+balance_sheet[96] # valuation_differences
        undivided_profit_or_unpaid_loss_from_previous_years=balance_sheet[96] # undivided_profit_or_unpaid_loss_from_previous_years
        profit_for_the_reporting_period_after_tax=balance_sheet[99] # profit_for_the_reporting_period_after_tax
        liabilities=balance_sheet[100] # liabilities
        long_term_liabilities_excluding_reserves_and_loans=balance_sheet[101] # long_term_liabilities_excluding_reserves_and_loans
        long_term_reserves=balance_sheet[117] # long_term_reserves
        long_term_bank_loans=balance_sheet[120] # long_term_bank_loans
        total_short_term_liabilities_excluding_reserves_loans_and_advances=balance_sheet[121] # total_short_term_liabilities_excluding_reserves_loans_and_advances
        short_term_trade_liabilities=balance_sheet[122] # short_term_trade_liabilities
        liabilities_to_employees_and_social_insurance=balance_sheet[130]+balance_sheet[131] # liabilities_to_employees_and_social_insurance
        tax_liabilities_and_grants=balance_sheet[132] # tax_liabilities_and_grants
        short_term_reserves=balance_sheet[135] # short_term_reserves
        current_bank_loans=balance_sheet[138] # current_bank_loans
        short_term_financial_assistance=balance_sheet[139] # short_term_financial_assistance

        total_operating_revenues=profit_and_loss[1] # total_operating_revenues
        sales_revenue=profit_and_loss[2] # sales_revenue
        revenue_from_the_sale_of_own_products_and_services=profit_and_loss[3]+profit_and_loss[4] # revenue_from_the_sale_of_own_products_and_services

        change_in_intra_organizational_inventories=profit_and_loss[5] # change_in_intra_organizational_inventories
        activation=profit_and_loss[6] # activation
        revenue_from_the_sale_of_long_term_intangible_assets_long_term_tangible_assets_and_materials=profit_and_loss[7] # revenue_from_the_sale_of_long_term_intangible_assets_long_term_tangible_assets_and_materials
        other_revenues_from_operating_activities=profit_and_loss[8] # other_revenues_from_operating_activities
        total_operating_costs=profit_and_loss[9] # total_operating_costs
        costs_incurred_to_acquire_sold_goods=profit_and_loss[10] # costs_incurred_to_acquire_sold_goods
        consumption_of_materials_energy_and_other_non_inventory_supplies=profit_and_loss[11] # consumption_of_materials_energy_and_other_non_inventory_supplies
        services=profit_and_loss[13] # services
        personnel_costs=profit_and_loss[14] # personnel_costs
        taxes_and_fees=profit_and_loss[19] # taxes_and_fees
        depreciation_and_adjustments_to_long_term_intangible_assets_and_long_term_tangible_assets=profit_and_loss[20] # depreciation_and_adjustments_to_long_term_intangible_assets_and_long_term_tangible_assets
        remaining_cost_of_sold_long_term_assets_and_materials=profit_and_loss[23] # remaining_cost_of_sold_long_term_assets_and_materials
        adjustments_to_receivables=profit_and_loss[24] # adjustments_to_receivables
        other_costs_of_operating_activities=profit_and_loss[25] # other_costs_of_operating_activities
        operating_result_from_operating_activities=profit_and_loss[26] # operating_result_from_operating_activities
        value_added=profit_and_loss[27] # value_added
        total_financial_revenues=profit_and_loss[28] # total_financial_revenues
        revenue_from_the_sale_of_securities_and_shares=profit_and_loss[29] # revenue_from_the_sale_of_securities_and_shares
        revenue_from_long_term_financial_assets=profit_and_loss[30] # revenue_from_long_term_financial_assets
        revenue_from_short_term_financial_assets=profit_and_loss[34] # revenue_from_short_term_financial_assets
        interest_income=profit_and_loss[38] # interest_income
        exchange_gains=profit_and_loss[41] # exchange_gains
        other_revenues_from_financial_activities=profit_and_loss[43] # other_revenues_from_financial_activities
        total_financial_costs=profit_and_loss[44] # total_financial_costs
        sale_of_securities_and_shares=profit_and_loss[45] # sale_of_securities_and_shares
        costs_of_short_term_financial_assets=profit_and_loss[46] # costs_of_short_term_financial_assets
        adjustments_to_financial_assets=profit_and_loss[47] # adjustments_to_financial_assets
        interest_expenses=profit_and_loss[48] # interest_expenses
        exchange_losses=profit_and_loss[51] # exchange_losses
        other_costs_of_financial_activities=profit_and_loss[53] # other_costs_of_financial_activities
        financial_result=profit_and_loss[54] # financial_result
        result_of_operations_for_the_reporting_period_before_tax=profit_and_loss[55] # result_of_operations_for_the_reporting_period_before_tax
        income_tax=profit_and_loss[56] # income_tax
        transfer_of_shares_in_the_result_to_shareholders=profit_and_loss[59] # transfer_of_shares_in_the_result_to_shareholders
        result_of_operations_for_the_reporting_period_after_tax=profit_and_loss[60] # result_of_operations_for_the_reporting_period_after_tax


        values = [
            total_assets,
            non_current_assets,
            intangible_assets,
            total_non_current_tangible_assets,
            land_and_buildings,
            separate_movable_assets_and_sets_of_movable_assets,
            other_long_term_tangible_assets,
            adjustment_item_for_acquired_assets,
            total_long_term_financial_assets,
            bank_balances_with_maturity_longer_than_one_year,
            current_assets,
            inventories,
            long_term_receivables,
            total_short_term_receivables,
            trade_receivables,
            social_security_tax_receivables_and_grants,
            financial_assets,
            other_financial_accounts,
            cash_and_bank_balances,
            total_owners_equity_and_liabilities,
            owners_equity,
            share_capital,
            share_capital_and_changes_in_share_capital,
            claims_for_subscribed_owners_equity,
            capital_funds,
            valuation_differences,
            undivided_profit_or_unpaid_loss_from_previous_years,
            profit_for_the_reporting_period_after_tax,
            liabilities,
            long_term_liabilities_excluding_reserves_and_loans,
            long_term_reserves,
            long_term_bank_loans,
            total_short_term_liabilities_excluding_reserves_loans_and_advances,
            short_term_trade_liabilities,
            liabilities_to_employees_and_social_insurance,
            tax_liabilities_and_grants,
            short_term_reserves,
            current_bank_loans,
            short_term_financial_assistance,
            total_operating_revenues,
            sales_revenue,
            revenue_from_the_sale_of_own_products_and_services,
            change_in_intra_organizational_inventories,
            activation,
            revenue_from_the_sale_of_long_term_intangible_assets_long_term_tangible_assets_and_materials,
            other_revenues_from_operating_activities,
            total_operating_costs,
            costs_incurred_to_acquire_sold_goods,
            consumption_of_materials_energy_and_other_non_inventory_supplies,
            services,
            personnel_costs,
            taxes_and_fees,
            depreciation_and_adjustments_to_long_term_intangible_assets_and_long_term_tangible_assets,
            remaining_cost_of_sold_long_term_assets_and_materials,
            adjustments_to_receivables,
            other_costs_of_operating_activities,
            operating_result_from_operating_activities,
            value_added,
            total_financial_revenues,
            revenue_from_the_sale_of_securities_and_shares,
            revenue_from_long_term_financial_assets,
            revenue_from_short_term_financial_assets,
            interest_income,
            exchange_gains,
            other_revenues_from_financial_activities,
            total_financial_costs,
            sale_of_securities_and_shares,
            costs_of_short_term_financial_assets,
            adjustments_to_financial_assets,
            interest_expenses,
            exchange_losses,
            other_costs_of_financial_activities,
            financial_result,
            result_of_operations_for_the_reporting_period_before_tax,
            income_tax,
            transfer_of_shares_in_the_result_to_shareholders,
            result_of_operations_for_the_reporting_period_after_tax
        ]

        return values


    def __parse_POD_1(self, tables_content):
        # 21
        for table in tables_content:
            name = table.get('nazov')
            data = table.get('data')
            if data is None:
                print('DOES NOT CONTAIN DATA')
        
        return []

    
    def __parse_POD_2(self, tables_content):
        # 22
        for table in tables_content:
            name = table.get('nazov')
            data = table.get('data')
            if data is None:
                print('DOES NOT CONTAIN DATA')
        
        return []