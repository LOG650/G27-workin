"""
Evalueringsmål for prognosemodeller.

MAPE er dysfunksjonell på lavt volum (små nevnere gir ekstreme prosenter). Vi
rapporterer derfor både den tradisjonelle MAPE og alternativer som er robuste:

- sMAPE (symmetric MAPE): 100 * mean( 2*|A-F| / (|A|+|F|) ) ∈ [0, 200]. Mindre
  følsom for lave faktiske verdier fordi nevneren er summen av begge.
- WAPE (weighted absolute percentage error): 100 * sum|A-F| / sum|A|. Vektet
  mål som ikke blåser opp prosenter på enkeltdager med lavt volum.

Referanse: Hyndman & Koehler (2006), "Another look at measures of forecast
accuracy", International Journal of Forecasting 22(4), 679–688.
"""

import numpy as np
from sklearn.metrics import mean_absolute_error


def mae(actual: np.ndarray, pred: np.ndarray) -> float:
    return float(mean_absolute_error(actual, pred))


def mape(actual: np.ndarray, pred: np.ndarray) -> float:
    """Tradisjonell MAPE. Ekskluderer faktisk=0 for å unngå deling på null."""
    actual, pred = np.asarray(actual, dtype=float), np.asarray(pred, dtype=float)
    mask = actual != 0
    if not mask.any():
        return 0.0
    return float(np.mean(np.abs((actual[mask] - pred[mask]) / actual[mask])) * 100)


def smape(actual: np.ndarray, pred: np.ndarray) -> float:
    """Symmetric MAPE: skalainvariant, robust mot lavt volum. Verdier i [0, 200]."""
    actual, pred = np.asarray(actual, dtype=float), np.asarray(pred, dtype=float)
    nevner = np.abs(actual) + np.abs(pred)
    mask = nevner != 0
    if not mask.any():
        return 0.0
    return float(np.mean(2 * np.abs(actual[mask] - pred[mask]) / nevner[mask]) * 100)


def wape(actual: np.ndarray, pred: np.ndarray) -> float:
    """Weighted APE: total absoluttfeil skalert med totalt faktisk volum."""
    actual, pred = np.asarray(actual, dtype=float), np.asarray(pred, dtype=float)
    sum_actual = np.sum(np.abs(actual))
    if sum_actual == 0:
        return 0.0
    return float(np.sum(np.abs(actual - pred)) / sum_actual * 100)


def bias(actual: np.ndarray, pred: np.ndarray) -> float:
    """Gjennomsnittlig over-/underestimering (positiv = overestimering)."""
    actual, pred = np.asarray(actual, dtype=float), np.asarray(pred, dtype=float)
    return float(np.mean(pred - actual))


def all_metrics(actual: np.ndarray, pred: np.ndarray) -> dict:
    """Returnerer alle målene som en ordbok."""
    return {
        'MAE': mae(actual, pred),
        'MAPE': mape(actual, pred),
        'sMAPE': smape(actual, pred),
        'WAPE': wape(actual, pred),
        'Bias': bias(actual, pred),
    }
