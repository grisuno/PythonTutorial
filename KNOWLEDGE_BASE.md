# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 5 | **Total Symbols Extracted:** 5 | **Total Imports:** 2

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
    n_1_py["1.py (py)"]
    class n_1_py mod;
    n_2_py["2.py (py)"]
    class n_2_py mod;
    n_4_py["4.py (py)"]
    class n_4_py mod;
    n_4_py_saludar["saludar"]
    class n_4_py_saludar fn;
    n_4_py --> n_4_py_saludar
    n_4_py_saludar_persona["saludar_persona"]
    class n_4_py_saludar_persona fn;
    n_4_py --> n_4_py_saludar_persona
    n_4_py_sumar["sumar"]
    class n_4_py_sumar fn;
    n_4_py --> n_4_py_sumar
    n_4_py_saludar_persona_con_default["saludar_persona_con_default"]
    class n_4_py_saludar_persona_con_default fn;
    n_4_py --> n_4_py_saludar_persona_con_default
    n_4_py_dividir["dividir"]
    class n_4_py_dividir fn;
    n_4_py --> n_4_py_dividir
    n_3_py["3.py (py)"]
    class n_3_py mod;
    n_5_py["5.py (py)"]
    class n_5_py mod;
    ext_sys["sys"]
    class ext_sys ext;
    n_1_py -.->|imports| ext_sys
    ext_math["math"]
    class ext_math ext;
    n_2_py -.->|imports| ext_math
```

---

## Architecture Reference

### PY (5 files)

#### `1.py`
**Path:** `1.py`

*No symbols extracted*

#### `2.py`
**Path:** `2.py`

*No symbols extracted*

#### `3.py`
**Path:** `3.py`

*No symbols extracted*

#### `4.py`
**Path:** `4.py`

**Functions:**
- `saludar` (line 9) `def saludar()`
- `saludar_persona` (line 16) `def saludar_persona(nombre)`
- `sumar` (line 23) `def sumar(a, b)`
- `saludar_persona_con_default` (line 31) `def saludar_persona_con_default(nombre)`
- `dividir` (line 43) `def dividir(a, b)`

#### `5.py`
**Path:** `5.py`

*No symbols extracted*
