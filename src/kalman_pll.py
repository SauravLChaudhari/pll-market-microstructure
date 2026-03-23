import numpy as np

class AdaptiveKalmanPLL:
    """
    Kalman filter with measurement noise scaled by the bid-ask spread.
    Implements the PLL concept: when spread widens (low SNR), trust observation less.
    """
    def __init__(self, process_noise: float, alpha: float):
        """
        process_noise : Q, the variance of the state transition noise (price volatility)
        alpha         : scaling factor for measurement noise from spread
        """
        self.Q = process_noise          # state transition noise
        self.alpha = alpha              # spread -> measurement noise scaling
        self.x = None                   # state estimate (true price)
        self.P = None                   # error covariance

    def initialize(self, initial_price: float, initial_covariance: float):
        """Set initial state and covariance."""
        self.x = np.array([[initial_price]], dtype=float)
        self.P = np.array([[initial_covariance]], dtype=float)

    def predict(self):
        """State prediction (random walk)."""
        self.x = self.x  # F = 1
        self.P = self.P + self.Q

    def update(self, mid_price: float, spread: float):
        """
        Measurement update with R = (spread/2)^2 * alpha.
        """
        # Measurement noise variance based on spread
        R = (spread / 2.0) ** 2 * self.alpha
        H = np.array([[1.0]])           # observation matrix
        y = mid_price - H @ self.x      # innovation
        S = H @ self.P @ H.T + R        # innovation covariance
        K = self.P @ H.T / S            # Kalman gain

        # Update state and covariance
        self.x = self.x + K * y
        self.P = (np.eye(1) - K @ H) @ self.P
        return float(self.x)            # return filtered price
