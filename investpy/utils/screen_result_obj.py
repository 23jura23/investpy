import math

class ScreenResultObj(object):
    """
    Create a ScreenResultObj from the given dict. Missing values are converted to NaN or ""
    depending on the expected data type
    """
    def __init__(self, obj):
        if not obj:
            raise ValueError("ERR#0039: results obj can not be None.")
        self.id = str_or_null("pair_ID", obj)
        self.symbol = str_or_null("stock_symbol", obj)
        self.parent_id = str_or_null("parent_pair_ID", obj)
        self.pe_ratio = float_or_nan("eq_pe_ratio", obj)
        self.market_cap = float_or_nan("eq_market_cap", obj)
        self.one_yr_return = float_or_nan("eq_one_year_return", obj)
        self.eps = float_or_nan("eq_eps", obj)
        self.dividend = float_or_nan("eq_dividend", obj)
        self.beta = float_or_nan("eq_beta", obj)
        self.revenue = float_or_nan("eq_revenue", obj)
        self.exchange_id = str_or_null("exchange_ID", obj)
        self.security_type = str_or_null("security_type", obj)
        self.a1fcf = float_or_nan("a1fcf", obj)
        self.aastturn = float_or_nan("aastturn", obj)
        self.abepsxclxo = float_or_nan("abepsxclxo", obj)
        self.abvps = float_or_nan("abvps", obj)
        self.acfshr = float_or_nan("acfshr", obj)
        self.acshps = float_or_nan("acshps", obj)
        self.acurratio = float_or_nan("acurratio", obj)
        self.aebitd = float_or_nan("aebitd", obj)
        self.aebt = float_or_nan("aebt", obj)
        self.aebtnorm = float_or_nan("aebtnorm", obj)
        self.aepsinclxo = float_or_nan("aepsinclxo", obj)
        self.aepsxclxor = float_or_nan("aepsxclxor", obj)
        self.agrosmgn = float_or_nan("agrosmgn", obj)
        self.aintcov = float_or_nan("aintcov", obj)
        self.altd2eq = float_or_nan("altd2eq", obj)
        self.aniac = float_or_nan("aniac", obj)
        self.aniacnorm = float_or_nan("aniacnorm", obj)
        self.aniperemp = float_or_nan("aniperemp", obj)
        self.anpmgnpct = float_or_nan("anpmgnpct", obj)
        self.aopmgnpct = float_or_nan("aopmgnpct", obj)
        self.apayratio = float_or_nan("apayratio", obj)
        self.apeexclxor = float_or_nan("apeexclxor", obj)
        self.apenorm = float_or_nan("apenorm", obj)
        self.apr2rev = float_or_nan("apr2rev", obj)
        self.apr2tanbk = float_or_nan("apr2tanbk", obj)
        self.aprfcfps = float_or_nan("aprfcfps", obj)
        self.aprice2bk = float_or_nan("aprice2bk", obj)
        self.aptmgnpct = float_or_nan("aptmgnpct", obj)
        self.arecturn = float_or_nan("arecturn", obj)
        self.arevperemp = float_or_nan("arevperemp", obj)
        self.arevps = float_or_nan("arevps", obj)
        self.aroa5yavg = float_or_nan("aroa5yavg", obj)
        self.aroapct = float_or_nan("aroapct", obj)
        self.aroe5yavg = float_or_nan("aroe5yavg", obj)
        self.aroepct = float_or_nan("aroepct", obj)
        self.aroi5yravg = float_or_nan("aroi5yravg", obj)
        self.aroipct = float_or_nan("aroipct", obj)
        self.atanbvps = float_or_nan("atanbvps", obj)
        self.atotd2eq = float_or_nan("atotd2eq", obj)
        self.bvtrendgr = float_or_nan("bvtrendgr", obj)
        self.csptrendgr = float_or_nan("csptrendgr", obj)
        self.divyield_curttm = float_or_nan("divyield_curttm", obj)
        self.ebitda_ayr5cagr = float_or_nan("ebitda_ayr5cagr", obj)
        self.ebitda_ttmy5cagr = float_or_nan("ebitda_ttmy5cagr", obj)
        self.epschngyr = float_or_nan("epschngyr", obj)
        self.epsgrpct = float_or_nan("epsgrpct", obj)
        self.epstrendgr = float_or_nan("epstrendgr", obj)
        self.ev2fcf_cura = float_or_nan("ev2fcf_cura", obj)
        self.ev2fcf_curttm = float_or_nan("ev2fcf_curttm", obj)
        self.focf2rev_aavg5 = float_or_nan("focf2rev_aavg5", obj)
        self.focf2rev_ttm = float_or_nan("focf2rev_ttm", obj)
        self.focf_ayr5cagr = float_or_nan("focf_ayr5cagr", obj)
        self.grosmgn5yr = float_or_nan("grosmgn5yr", obj)
        self.margin5yr = float_or_nan("margin5yr", obj)
        self.mktcap = float_or_nan("mktcap", obj)
        self.netdebt_a = float_or_nan("netdebt_a", obj)
        self.netdebt_i = float_or_nan("netdebt_i", obj)
        self.npmtrendgr = float_or_nan("npmtrendgr", obj)
        self.opmgn5yr = float_or_nan("opmgn5yr", obj)
        self.pebexclxor = float_or_nan("pebexclxor", obj)
        self.peexclxor = float_or_nan("peexclxor", obj)
        self.peinclxor = float_or_nan("peinclxor", obj)
        self.pr2tanbk = float_or_nan("pr2tanbk", obj)
        self.price2bk = float_or_nan("price2bk", obj)
        self.ptmgn5yr = float_or_nan("ptmgn5yr", obj)
        self.qbvps = float_or_nan("qbvps", obj)
        self.qcshps = float_or_nan("qcshps", obj)
        self.qcurratio = float_or_nan("qcurratio", obj)
        self.qltd2eq = float_or_nan("qltd2eq", obj)
        self.qtanbvps = float_or_nan("qtanbvps", obj)
        self.qtotd2eq = float_or_nan("qtotd2eq", obj)
        self.revchngyr = float_or_nan("revchngyr", obj)
        self.revgrpct = float_or_nan("revgrpct", obj)
        self.revps5ygr = float_or_nan("revps5ygr", obj)
        self.revtrendgr = float_or_nan("revtrendgr", obj)
        self.sharesout = float_or_nan("sharesout", obj)
        self.stld_ayr5cagr = float_or_nan("stld_ayr5cagr", obj)
        self.tanbv_ayr5cagr = float_or_nan("tanbv_ayr5cagr", obj)
        self.ttmastturn = float_or_nan("ttmastturn", obj)
        self.ttmbepsxcl = float_or_nan("ttmbepsxcl", obj)
        self.ttmcfshr = float_or_nan("ttmcfshr", obj)
        self.ttmebitd = float_or_nan("ttmebitd", obj)
        self.ttmebitdps = float_or_nan("ttmebitdps", obj)
        self.ttmebt = float_or_nan("ttmebt", obj)
        self.ttmepschg = float_or_nan("ttmepschg", obj)
        self.ttmepsincx = float_or_nan("ttmepsincx", obj)
        self.ttmepsxclx = float_or_nan("ttmepsxclx", obj)
        self.ttmfcf = float_or_nan("ttmfcf", obj)
        self.ttmfcfshr = float_or_nan("ttmfcfshr", obj)
        self.ttmgrosmgn = float_or_nan("ttmgrosmgn", obj)
        self.ttmintcov = float_or_nan("ttmintcov", obj)
        self.ttmniac = float_or_nan("ttmniac", obj)
        self.ttmniperem = float_or_nan("ttmniperem", obj)
        self.ttmnpmgn = float_or_nan("ttmnpmgn", obj)
        self.ttmopmgn = float_or_nan("ttmopmgn", obj)
        self.ttmpayrat = float_or_nan("ttmpayrat", obj)
        self.ttmpehigh = float_or_nan("ttmpehigh", obj)
        self.ttmpelow = float_or_nan("ttmpelow", obj)
        self.ttmpr2rev = float_or_nan("ttmpr2rev", obj)
        self.ttmprcfps = float_or_nan("ttmprcfps", obj)
        self.ttmprfcfps = float_or_nan("ttmprfcfps", obj)
        self.ttmptmgn = float_or_nan("ttmptmgn", obj)
        self.ttmrecturn = float_or_nan("ttmrecturn", obj)
        self.ttmrevchg = float_or_nan("ttmrevchg", obj)
        self.ttmrevpere = float_or_nan("ttmrevpere", obj)
        self.ttmrevps = float_or_nan("ttmrevps", obj)
        self.ttmroapct = float_or_nan("ttmroapct", obj)
        self.ttmroepct = float_or_nan("ttmroepct", obj)
        self.ttmroipct = float_or_nan("ttmroipct", obj)
        self.vdes_ttm = float_or_nan("vdes_ttm", obj)
        self.RSI = float_or_nan("RSI", obj)
        self.STOCH = float_or_nan("STOCH", obj)
        self.CCI = float_or_nan("CCI", obj)
        self.MACD = float_or_nan("MACD", obj)
        self.ADX = float_or_nan("ADX", obj)
        self.WilliamsR = float_or_nan("WilliamsR", obj)
        self.STOCHRSI = float_or_nan("STOCHRSI", obj)
        self.ATR = float_or_nan("ATR", obj)
        self.HL = float_or_nan("HL", obj)
        self.UO = float_or_nan("UO", obj)
        self.ROC = float_or_nan("ROC", obj)
        self.BullBear = float_or_nan("BullBear", obj)
        self.tech_sum_300 = str_or_null("tech_sum_300", obj)
        self.tech_sum_900 = str_or_null("tech_sum_900", obj)
        self.tech_sum_1800 = str_or_null("tech_sum_1800", obj)
        self.tech_sum_3600 = str_or_null("tech_sum_3600", obj)
        self.tech_sum_18000 = str_or_null("tech_sum_18000", obj)
        self.tech_sum_86400 = str_or_null("tech_sum_86400", obj)
        self.tech_sum_week = str_or_null("tech_sum_week", obj)
        self.tech_sum_month = str_or_null("tech_sum_month", obj)
        self.month_change = float_or_nan("month_change", obj)
        self.ytd = float_or_nan("ytd", obj)
        self.week = float_or_nan("week", obj)
        self.month = float_or_nan("month", obj)
        self.year = float_or_nan("year", obj)
        self.three_year = float_or_nan("3year", obj)
        self.sector_id = str_or_null("sector_id", obj)
        self.industry_id = str_or_null("industry_id", obj)
        self.avg_volume = float_or_nan("avg_volume", obj)
        self.pair_change_percent = float_or_nan("pair_change_percent", obj)
        self.a52_week_high = float_or_nan("a52_week_high", obj)
        self.a52_week_low = float_or_nan("a52_week_low", obj)
        self.turnover_volume = float_or_nan("turnover_volume", obj)
        self.last = float_or_nan("last", obj)
        self.a52_week_high_diff = float_or_nan("a52_week_high_diff", obj)
        self.a52_week_low_diff = float_or_nan("a52_week_low_diff", obj)
        self.exchange_category = str_or_null("exchange_trans", obj)
        self.name = str_or_null("name_trans", obj)
        self.sector = str_or_null("sector_trans", obj)
        self.industry = str_or_null("industry_trans", obj)
        self.daily_vol = int(float_or_nan("daily", obj))

    def as_dict(self):
        return {
            "id": self.id,
            "Name": self.name,
            "Symbol": self.symbol,
            "Sector": self.sector,
            "Industry": self.industry,
            "P/E Ratio": self.pe_ratio,
            "Market Cap": self.market_cap,
            "1-Year Change": self.one_yr_return,
            "EPS": self.eps,
            "Dividend": self.dividend,
            "Beta": self.beta,
            "Revenue": self.revenue,
            "parent_id": self.parent_id,
            "exchange_id": self.exchange_id,
            "security_type": self.security_type,
            "a1fcf": self.a1fcf,
            "aastturn": self.aastturn,
            "abepsxclxo": self.abepsxclxo,
            "abvps": self.abvps,
            "acfshr": self.acfshr,
            "acshps": self.acshps,
            "acurratio": self.acurratio,
            "aebitd": self.aebitd,
            "aebt": self.aebt,
            "aebtnorm": self.aebtnorm,
            "aepsinclxo": self.aepsinclxo,
            "aepsxclxor": self.aepsxclxor,
            "agrosmgn": self.agrosmgn,
            "aintcov": self.aintcov,
            "altd2eq": self.altd2eq,
            "aniac": self.aniac,
            "aniacnorm": self.aniacnorm,
            "aniperemp": self.aniperemp,
            "anpmgnpct": self.anpmgnpct,
            "aopmgnpct": self.aopmgnpct,
            "apayratio": self.apayratio,
            "apeexclxor": self.apeexclxor,
            "apenorm": self.apenorm,
            "apr2rev": self.apr2rev,
            "apr2tanbk": self.apr2tanbk,
            "aprfcfps": self.aprfcfps,
            "aprice2bk": self.aprice2bk,
            "aptmgnpct": self.aptmgnpct,
            "arecturn": self.arecturn,
            "arevperemp": self.arevperemp,
            "arevps": self.arevps,
            "aroa5yavg": self.aroa5yavg,
            "aroapct": self.aroapct,
            "aroe5yavg": self.aroe5yavg,
            "aroepct": self.aroepct,
            "aroi5yravg": self.aroi5yravg,
            "aroipct": self.aroipct,
            "atanbvps": self.atanbvps,
            "atotd2eq": self.atotd2eq,
            "bvtrendgr": self.bvtrendgr,
            "csptrendgr": self.csptrendgr,
            "Div Yield (TTM)": self.divyield_curttm,
            "ebitda_ayr5cagr": self.ebitda_ayr5cagr,
            "ebitda_ttmy5cagr": self.ebitda_ttmy5cagr,
            "epschngyr": self.epschngyr,
            "epsgrpct": self.epsgrpct,
            "epstrendgr": self.epstrendgr,
            "ev2fcf_cura": self.ev2fcf_cura,
            "ev2fcf_curttm": self.ev2fcf_curttm,
            "focf2rev_aavg5": self.focf2rev_aavg5,
            "focf2rev_ttm": self.focf2rev_ttm,
            "focf_ayr5cagr": self.focf_ayr5cagr,
            "grosmgn5yr": self.grosmgn5yr,
            "margin5yr": self.margin5yr,
            "mktcap": self.mktcap,
            "netdebt_a": self.netdebt_a,
            "netdebt_i": self.netdebt_i,
            "npmtrendgr": self.npmtrendgr,
            "opmgn5yr": self.opmgn5yr,
            "pebexclxor": self.pebexclxor,
            "peexclxor": self.peexclxor,
            "peinclxor": self.peinclxor,
            "pr2tanbk": self.pr2tanbk,
            "price2bk": self.price2bk,
            "ptmgn5yr": self.ptmgn5yr,
            "qbvps": self.qbvps,
            "qcshps": self.qcshps,
            "qcurratio": self.qcurratio,
            "qltd2eq": self.qltd2eq,
            "qtanbvps": self.qtanbvps,
            "qtotd2eq": self.qtotd2eq,
            "revchngyr": self.revchngyr,
            "revgrpct": self.revgrpct,
            "revps5ygr": self.revps5ygr,
            "revtrendgr": self.revtrendgr,
            "sharesout": self.sharesout,
            "stld_ayr5cagr": self.stld_ayr5cagr,
            "tanbv_ayr5cagr": self.tanbv_ayr5cagr,
            "ttmastturn": self.ttmastturn,
            "ttmbepsxcl": self.ttmbepsxcl,
            "ttmcfshr": self.ttmcfshr,
            "ttmebitd": self.ttmebitd,
            "ttmebitdps": self.ttmebitdps,
            "ttmebt": self.ttmebt,
            "ttmepschg": self.ttmepschg,
            "ttmepsincx": self.ttmepsincx,
            "ttmepsxclx": self.ttmepsxclx,
            "ttmfcf": self.ttmfcf,
            "ttmfcfshr": self.ttmfcfshr,
            "ttmgrosmgn": self.ttmgrosmgn,
            "ttmintcov": self.ttmintcov,
            "ttmniac": self.ttmniac,
            "ttmniperem": self.ttmniperem,
            "ttmnpmgn": self.ttmnpmgn,
            "ttmopmgn": self.ttmopmgn,
            "ttmpayrat": self.ttmpayrat,
            "P/E High (TTM)": self.ttmpehigh,
            "P/E Low (TTM)": self.ttmpelow,
            "Price to Sales (TTM)": self.ttmpr2rev,
            "ttmprcfps": self.ttmprcfps,
            "ttmprfcfps": self.ttmprfcfps,
            "ttmptmgn": self.ttmptmgn,
            "ttmrecturn": self.ttmrecturn,
            "ttmrevchg": self.ttmrevchg,
            "ttmrevpere": self.ttmrevpere,
            "ttmrevps": self.ttmrevps,
            "ttmroapct": self.ttmroapct,
            "ttmroepct": self.ttmroepct,
            "ttmroipct": self.ttmroipct,
            "vdes_ttm": self.vdes_ttm,
            "RSI": self.RSI,
            "STOCH": self.STOCH,
            "CCI": self.CCI,
            "MACD": self.MACD,
            "ADX": self.ADX,
            "WilliamsR": self.WilliamsR,
            "STOCHRSI": self.STOCHRSI,
            "ATR": self.ATR,
            "HL": self.HL,
            "UO": self.UO,
            "ROC": self.ROC,
            "BullBear": self.BullBear,
            "Technical 5m": self.tech_sum_300,
            "Technical 15m": self.tech_sum_900,
            "Technical 30m": self.tech_sum_1800,
            "Technical 1h": self.tech_sum_3600,
            "Technical 5h": self.tech_sum_18000,
            "Technical 1d": self.tech_sum_86400,
            "Technical 1w": self.tech_sum_week,
            "Technical 1mo": self.tech_sum_month,
            "Month Change": self.month_change,
            "Ytd Perf": self.ytd,
            "1wk Perf": self.week,
            "1mo Perf": self.month,
            "1yr Perf": self.year,
            "3yr Perf": self.three_year,
            "sector_id": self.sector_id,
            "industry_id": self.industry_id,
            "Ave Volume (3mo)": self.avg_volume,
            "pair_change_percent": self.pair_change_percent,
            "a52_week_high": self.a52_week_high,
            "a52_week_low": self.a52_week_low,
            "turnover_volume": self.turnover_volume,
            "last": self.last,
            "a52_week_high_diff": self.a52_week_high_diff,
            "a52_week_low_diff": self.a52_week_low_diff,
            "exchange_category": self.exchange_category,
            "daily_vol": self.daily_vol,
        }


def float_or_nan(key, obj):
    try:
        val = obj[key]
    except KeyError:
        return math.nan
    try:
        return float(val)
    except ValueError:
        return math.nan

def int_or_nan(key, obj):
    try:
        val = obj[key]
    except KeyError:
        return math.nan
    try:
        return int(val)
    except ValueError:
        return math.nan

def str_or_null(key, obj):
    try:
        val = obj[key]
    except KeyError:
        return ""
    return str(val)
