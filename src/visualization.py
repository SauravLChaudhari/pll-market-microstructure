import matplotlib.pyplot as plt
import numpy as np

def plot_results(df, filtered_prices, spread_scaled_noise=None):
    fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

    axes[0].plot(df['timestamp'], df['mid_price'], label='Observed Mid Price', alpha=0.5)
    axes[0].plot(df['timestamp'], filtered_prices, label='Filtered (PLL)', linewidth=2)
    axes[0].set_ylabel('Price')
    axes[0].legend()
    axes[0].set_title('Adaptive Kalman Filter as a PLL for Price Denoising')

    axes[1].plot(df['timestamp'], df['spread'], label='Bid-Ask Spread', color='orange')
    axes[1].set_ylabel('Spread')
    axes[1].legend()

    if spread_scaled_noise is not None:
        axes[2].plot(df['timestamp'], spread_scaled_noise, label='Measurement Noise Variance (scaled)', color='red')
        axes[2].set_ylabel('R')
        axes[2].legend()

    axes[2].set_xlabel('Time')
    plt.tight_layout()
    plt.show()
