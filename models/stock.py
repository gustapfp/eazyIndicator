from pydantic import BaseModel

class Stock(BaseModel):
    cotacao: dict
    pl: dict
    pvp: dict
    psr: dict
    dy: dict
    pa: dict
    pcg: dict
    pebit: dict
    pacl: dict
    evebit: dict
    evebitda: dict
    mrgebit: dict
    mrgliq: dict
    roic: dict
    roe: dict
    liqc: dict
    liq2m: dict
    patrliq: dict
    divbpat: dict 
    divbpatr: dict
