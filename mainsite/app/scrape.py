from requests_html import HTMLSession
import pandas as pd
import numpy
import math


def force_float(elt):
    try:
        return float(elt)
    except:
        return elt


def scrape(site):
    session = HTMLSession()
    resp = session.get(site)
    tables = pd.read_html(resp.html.raw_html)  
    df = tables[0].copy()
    df.columns = tables[0].columns
    session.close()

    return df


def changeVals(fields_to_change, df):
    for field in fields_to_change:
        if type(df[field][0]) == str:
            df[field] = df[field].str.strip("B").map(force_float)

            df[field] = df[field].map(lambda x: x * 1000000000 if type(x) == numpy.float64 else x)

            df[field] = df[field].map(lambda x: x if type(x) == float else
                                    force_float(x.strip("M")) * 1000000)
    return fields_to_change


def removeNan(field, df):
    df[field] = df[field].map(lambda x: "NA" if math.isnan(x) else x)


def get_top_gains():
    df = scrape("https://finance.yahoo.com/gainers?count=10")
    del df["52 Week Range"]

    df["% Change"] = df["% Change"].map(lambda x: float(x.replace(",", "").strip("%")))

    fields_to_change = [x for x in df.columns.tolist() if "Vol" in x \
                        or x == "Market Cap"]
    fields_to_change = changeVals(fields_to_change, df)

    fields_to_change = removeNan("PE Ratio (TTM)", df)

    return df


# top 10 etfs: https://sg.finance.yahoo.com/etfs?count=10
def get_top_etfs():
    df = scrape("https://sg.finance.yahoo.com/etfs?count=10")

    del df["52-week range"]
    df["% change"] = df["% change"].map(lambda x: float(x.replace(",", "").strip("%")))

    fields_to_change = [x for x in df.columns.tolist() if "Vol" in x]
    fields_to_change = changeVals(fields_to_change, df)

    return df

# top 10 futures based on highest volume: https://sg.finance.yahoo.com/commodities
def get_futures():
    df = scrape("https://sg.finance.yahoo.com/commodities")
    df = df.head(10)

    del df["Day chart"]
    df["% change"] = df["% change"].map(lambda x: float(x.replace(",", "").strip("%")))

    fields_to_change = [x for x in df.columns.tolist() if "Vol" in x]
    fields_to_change = changeVals(fields_to_change, df)
    return df

# https://sg.finance.yahoo.com/bonds
def get_bonds():
    df = scrape("https://sg.finance.yahoo.com/bonds")

    del df["Day chart"]
    del df["52-week range"]
    df["% change"] = df["% change"].map(lambda x: float(x.replace(",", "").strip("%")))

    return df


# get top options with highest open interest: https://finance.yahoo.com/options/highest-open-interest
def get_options():
    df = scrape("https://finance.yahoo.com/options/highest-open-interest")

    df = df.head(10)

    df["% Change"] = df["% Change"].map(lambda x: float(x.replace(",", "").strip("%")))
    fields_to_change = [x for x in df.columns.tolist() if "Vol" in x \
                        or x == "Open Interest"]
    fields_to_change = changeVals(fields_to_change, df)

    return df