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

        # assets
        ca = balance_sheet[14]+balance_sheet[16]+balance_sheet[20]
        ta = balance_sheet[0]
        cash = balance_sheet[20]

        # liablities
        eq = balance_sheet[24]
        cl = balance_sheet[37] + balance_sheet[44] + balance_sheet[43]
        ncl = balance_sheet[34] + balance_sheet[36]
        tl = cl + ncl

        # profit and loss
        cf = profit_and_loss[37] + profit_and_loss[13]
        sal = profit_and_loss[1] + profit_and_loss[2] + profit_and_loss[5] + profit_and_loss[20]
        eat = profit_and_loss[37]
        ebit = profit_and_loss[30] + profit_and_loss[35] + profit_and_loss[37]
        
        # ['ca', 'ta', 'eq', 'cl', 'ncl', 'tl', 'cash', 'cf', 'sal', 'eat', 'ebit']
        values = [ca, 0, ta, eq, cl, ncl, tl, cash, cf, sal, eat, ebit, 0, 0, 0, 0, 0]
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

        # assets
        ca = balance_sheet[70] + balance_sheet[52] + balance_sheet[33]
 
        cc = balance_sheet[52]
        ta = balance_sheet[0]
        cash = balance_sheet[70]
        
        # liablities
        eq = balance_sheet[79]
        tl = balance_sheet[100]
        cl = balance_sheet[121]
        
        # profit and loss
        cf = profit_and_loss[60] + profit_and_loss[21]
        sal = profit_and_loss[2] + profit_and_loss[3] + profit_and_loss[4] + profit_and_loss[7] + profit_and_loss[29]
        eat = profit_and_loss[60]
        ebit = profit_and_loss[26] - profit_and_loss[7] + profit_and_loss[23] + profit_and_loss[12] + profit_and_loss[22] + profit_and_loss[24] - profit_and_loss[8]
        ebt = profit_and_loss[55]
        it = profit_and_loss[38] + profit_and_loss[48]
        stock = balance_sheet[33]
        yie = profit_and_loss[1] + profit_and_loss[28]
        cost = profit_and_loss[9] + profit_and_loss[44]
        
        # ['ca', 'ta', 'eq', 'cl', 'ncl', 'tl', 'cash', 'cf', 'sal', 'eat', 'ebit']
        values = [ca, cc, ta, eq, cl, tl - cl, tl, cash, cf, sal, eat, ebit, ebt, stock, cost, it, yie]
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
