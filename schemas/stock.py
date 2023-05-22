def stock_entity(db_item) -> dict:
    return {
        "id" : str(db_item['_id']),
        "cotacao": db_item['cotacao'],
        "pl": db_item['pl'],
        "pvp": db_item['pvp'],
        "psr": db_item['psr'],
        "dy": db_item['dy'],
        "pa": db_item['pa'],
        "pcg": db_item['pcg'],
        "pebit": db_item['pebit'],
        "pacl": db_item['pacl'],
        "evebit": db_item['evebit'],
        "evebitda": db_item['evebitda'],
        "mrgebit": db_item['mrgebit'],
        "mrgliq": db_item['mrgliq'],
        "roic": db_item['roic'],
        "roe": db_item['roe'],
        "liqc": db_item['liqc'],
        "liq2m": db_item['liq2m'],
        "patrliq": db_item['patrliq'],
        "divbpatr": db_item['divbpatr'],
        "c5y": db_item['c5y'],
        "paper" : db_item['paper']
    }

def stock_list_entity(db_item) -> list:
    stock_list = []
    for item in db_item:
        stock_list.append(stock_entity(item))
    return stock_list