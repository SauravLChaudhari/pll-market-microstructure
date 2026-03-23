# PLL for Market Microstructure – Adaptive Price Denoising

## Signal‑Processing to Quant Translation

In RF systems, a Phase‑Locked Loop (PLL) tracks a noisy carrier.  
The loop filter bandwidth adapts to the signal‑to‑noise ratio (SNR).  
High SNR → narrow filter (low phase noise). Low SNR → wide filter (maintain lock).

Here, the **mid‑price** ( (bid+ask)/2 ) is the “received signal”.  
The **true price** is the latent “carrier”.  
The **bid‑ask spread** is a proxy for measurement noise: wide spread → high uncertainty (low SNR).  

I implement a **Kalman filter with time‑varying measurement noise** `R = (spread/2)² * α`.  
When spread widens, the filter trusts the observation less – exactly like a PLL.

## Mathematical Model

**State** (true price):  
`x_k = x_{k-1} + w_k,   w_k ~ N(0, Q)`  

**Observation** (mid‑price):  
`z_k = x_k + v_k,   v_k ~ N(0, R_k)`  

`R_k = (spread_k / 2)² * α`  
`α` = scaling factor (tuned via historical data).  

Standard Kalman prediction / update.

## Repository Contents

- `src/` – core modules and data generation
- `notebooks/` – interactive demo
- `tests/` – unit tests

## Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
