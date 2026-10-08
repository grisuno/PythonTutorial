# root

*Community 0 | 5 files | cohesion 1.00*

## Definition

This community groups 5 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `dividir`, `saludar`, `saludar_persona`, `saludar_persona_con_default`, `sumar`. Core file: `4.py` (5 symbols). Documented purpose: Script 1: Introducción a Python  Este es el primer script de una serie de tutoriales en Python. En este script, cubriremos los conceptos básicos de Python, como.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `1.py` | py | utility | 0 | yes |
| `2.py` | py | utility | 0 | yes |
| `3.py` | py | utility | 0 | yes |
| `4.py` | py | utility | 5 | yes |
| `5.py` | py | utility | 0 | yes |

## Key Symbols

- `saludar` (function, `4.py:9`) `def saludar()`
- `saludar_persona` (function, `4.py:16`) `def saludar_persona(nombre)`
- `sumar` (function, `4.py:23`) `def sumar(a, b)`
- `saludar_persona_con_default` (function, `4.py:31`) `def saludar_persona_con_default(nombre)`
- `dividir` (function, `4.py:43`) `def dividir(a, b)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `1.py`
- `2.py`
- `3.py`
- `4.py`
- `5.py`
