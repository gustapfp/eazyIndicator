def stock_entity(db_item) -> dict:
    return {
        "id" : str(db_item['$oid']),
        "cotacao": db_item['cotacao'].values(),
        "pl": db_item['pl'].values(),
        "pvp": db_item['pvp'].values(),
        "psr": db_item['psr'].values(),
        "dy": db_item['dy'].values(),
        "pa": db_item['pa'].values(),
        "pcg": db_item['pcg'].values(),
        "pebit": db_item['pebit'].values(),
        "pacl": db_item['pacl'].values(),
        "evebit": db_item['evebit'].values(),
        "evebitda": db_item['evebitda'].values(),
        "mrgebit": db_item['mrgebit'].values(),
        "mrgliq": db_item['mrgliq'].values(),
        "roic": db_item['roic'].values(),
        "roe": db_item['roe'].values(),
        "liqc": db_item['liqc'].values(),
        "liq2m": db_item['liq2m'].values(),
        "patrliq": db_item['patrliq'].values(),
        "divbpat": db_item['divbpat'].values(),
        "divbpatr": db_item['divbpatr'].values(),
    }