import numpy as np
from src.kalman_pll import AdaptiveKalmanPLL

def test_constant_price():
    pll = AdaptiveKalmanPLL(process_noise=1e-6, alpha=1.0)
    pll.initialize(initial_price=100.0, initial_covariance=1.0)
    for _ in range(10):
        pll.predict()
        filt = pll.update(100.0, spread=0.02)
        assert np.isclose(filt, 100.0, atol=1e-4)

def test_convergence():
    pll = AdaptiveKalmanPLL(process_noise=0.001, alpha=1.0)
    pll.initialize(initial_price=90.0, initial_covariance=100.0)
    # Simulate a step change to 100
    for _ in range(50):
        pll.predict()
        filt = pll.update(100.0, spread=0.01)
    assert np.isclose(filt, 100.0, atol=1.0)
