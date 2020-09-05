from requests_html import HTMLSession
import pandas as pd


def force_float(elt):
    try:
        return float(elt)
    except:
        return elt



def get_top_gains():
    site = "https://finance.yahoo.com/gainers?count=10"

    session = HTMLSession()
        
    resp = session.get(site)

    tables = pd.read_html(resp.html.raw_html)  

    df = tables[0].copy()

    df.columns = tables[0].columns

    del df["52 Week Range"]

    df["% Change"] = df["% Change"].map(lambda x: float(x.replace(",", "").strip("%")))

    fields_to_change = [x for x in df.columns.tolist() if "Vol" in x \
                        or x == "Market Cap"]

    for field in fields_to_change:
        if type(df[field][0]) == str:
            df[field] = df[field].str.strip("B").map(force_float)
            df[field] = df[field].map(lambda x: x if type(x) == str 
                                                else x * 1000000000)
            
            df[field] = df[field].map(lambda x: x if type(x) == float else
                                    force_float(x.strip("M")) * 1000000)    
    session.close()

    # return df['Symbol'].values.tolist()
    return df

# top 10 etfs: https://sg.finance.yahoo.com/etfs?count=10
