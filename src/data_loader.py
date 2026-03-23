import pandas as pd

def load_tick_data(file_path: str) -> pd.DataFrame:
    """
    Load tick data from a CSV file.
    Expected columns: timestamp, bid_price, ask_price.
    Returns a DataFrame with additional columns: mid_price, spread.
    """
    df = pd.read_csv(file_path, parse_dates=['timestamp'])
    df = df.sort_values('timestamp')
    df['mid_price'] = (df['bid_price'] + df['ask_price']) / 2.0
    df['spread'] = df['ask_price'] - df['bid_price']
    return df
