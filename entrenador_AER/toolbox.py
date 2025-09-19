import numpy as np

def RandomState(dim=2, normalized=True, real=False, seed=None):
    """Genera un vector de estado aleatorio en dimensión 'dim'."""
    if seed is not None:
        np.random.seed(seed)
    if real:
        v = np.random.randn(dim) + 0j
    else:
        v = np.random.randn(dim) + 1j * np.random.randn(dim)
    if normalized:
        v = v / np.linalg.norm(v)
    return v

def BalancedState(numberQbits):
    """Genera un estado balanceado tipo Hadamard para 'numberQbits'."""
    initial = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
    if numberQbits > 1:
        psi_h = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
        for _ in range(numberQbits - 1):
            v = np.kron(initial, psi_h)
    else:
        v = initial
    return v

def Sampler(state_vector, n_shots=1000, seed=None):
    """Simula la medición de un estado con 'n_shots' repeticiones."""
    dim = len(state_vector)
    if seed is not None:
        np.random.seed(seed)
    outcomes_list = np.arange(dim)
    prob = np.abs(state_vector)**2  
    samples = np.random.choice(outcomes_list, size=n_shots, p=prob)
    return {
        'samples': samples,
        'probs': prob
    }

def Estimator(state, n_shots=1000, seed=None):
    """Refina las frecuencias y calcula desviación estándar del muestreo."""
    pub = Sampler(state, n_shots=n_shots, seed=seed)
    sample = pub['samples']
    prob = pub['probs']
    counts = np.array([np.sum(sample == i) for i in range(len(state))])
    freqs = counts / n_shots
    stderr = np.sqrt(freqs * (1 - freqs) / n_shots)
    return {
        'probs_theorical': prob,
        'freqs_sampled': freqs,
        'stderr_sampled': stderr,
        'percent_devest': np.round((100*stderr/freqs), 2),
        'counts': counts,
        'n_shots': n_shots
    }
