from pydantic import BaseModel

class Stock(BaseModel):
    cotacao: int
    pl: int
    pvp: int
    psr: int
    dy: int
    pa: int
    pcg: int
    pebit: int
    pacl: int
    evebit: int
    evebitda: int
    mrgebit: int
    mrgliq: int
    roic: int
    roe: int
    liqc: int
    liq2m: int
    patrliq: int
    divbpatr: int 
    c5y: int
    paper: str
