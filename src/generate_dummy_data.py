import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_synthetic_ticks(num_ticks: int = 1000, output_path: str = '../data/sample_ticks.csv'):
    """
    Generates synthetic market microstructure tick data.
    Simulates a latent true price and layers on bid-ask spread noise.
    Includes simulated 'liquidity shocks' where the spread widens significantly.
    """
    np.random.seed(42)
    
    # 1. Simulate Latent True Price (Random Walk)
    true_price = np.zeros(num_ticks)
    true_price[0] = 150.0  # Starting price
    innovations = np.random.normal(loc=0.0, scale=0.05, size=num_ticks)
    
    for i in range(1, num_ticks):
        true_price[i] = true_price[i-1] + innovations[i]
        
    # 2. Simulate Bid-Ask Spread
    # Baseline spread is tight, but we add occasional "spread explosions" (low SNR)
    base_spread = np.random.uniform(0.01, 0.05, size=num_ticks)
    
    # Inject liquidity shocks (widening spread)
    shock_indices = np.random.choice(num_ticks, size=int(num_ticks * 0.05), replace=False)
    base_spread[shock_indices] += np.random.uniform(0.20, 0.50, size=len(shock_indices))
    
    # 3. Calculate Bid and Ask Prices
    # In reality, quotes bounce around the true price
    microstructure_noise = np.random.normal(0, base_spread/4)
    observed_mid = true_price + microstructure_noise
    
    bid_price = observed_mid - (base_spread / 2)
    ask_price = observed_mid + (base_spread / 2)
    
    # 4. Generate Timestamps
    start_time = datetime(2025, 1, 1, 9, 30, 0)
    timestamps = [start_time + timedelta(milliseconds=int(i * 250)) for i in range(num_ticks)]
    
    # 5. Compile DataFrame
    df = pd.DataFrame({
        'timestamp': timestamps,
        'bid_price': np.round(bid_price, 3),
        'ask_price': np.round(ask_price, 3)
    })
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save to CSV
    df.to_csv(output_path, index=False)
    print(f"Successfully generated {num_ticks} synthetic ticks at {output_path}")

if __name__ == "__main__":
    generate_synthetic_ticks()
