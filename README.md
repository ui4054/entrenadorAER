# Entrenador AER 🧑‍💻⚛️

Toolbox mínimo para ejercicios de computación cuántica.  
Incluye funciones:

- `RandomState`
- `BalancedState`
- `Sampler`
- `Estimator`

## Instalación en Google Colab

```python
!pip install git+https://github.com/tuusuario/entrenador_AER.git
```

## Ejemplo de uso

```python
from entrenador_AER import RandomState, Sampler, Estimator

psi = RandomState(dim=2, seed=42)
print("Estado aleatorio:", psi)

resultados = Sampler(psi, n_shots=100)
print(resultados)

estimacion = Estimator(psi, n_shots=1000)
print(estimacion)
```
