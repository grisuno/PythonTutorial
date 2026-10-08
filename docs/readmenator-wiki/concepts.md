# Concepts

Second-brain semantic layer: nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

| Concept | Files | Mentions | Top Files |
|---------|-------|----------|-----------|
| `script` | 5 | 11 | `1.py`, `2.py`, `3.py`, `4.py`, `5.py` |
| `python` | 5 | 7 | `1.py`, `2.py`, `3.py`, `4.py`, `5.py` |
| `este` | 5 | 6 | `1.py`, `2.py`, `3.py`, `4.py`, `5.py` |
| `aprenderemos` | 4 | 4 | `2.py`, `3.py`, `4.py`, `5.py` |
| `para` | 3 | 8 | `1.py`, `2.py`, `5.py` |
| `las` | 3 | 5 | `2.py`, `3.py`, `4.py` |
| `una` | 3 | 4 | `1.py`, `3.py`, `4.py` |
| `como` | 3 | 3 | `1.py`, `4.py`, `5.py` |
| `estructuras` | 2 | 3 | `2.py`, `3.py` |
| `con` | 2 | 2 | `4.py`, `5.py` |
| `del` | 2 | 2 | `1.py`, `5.py` |
| `exploraremos` | 2 | 2 | `2.py`, `3.py` |
| `funci` | 2 | 2 | `4.py`, `5.py` |
| `importar` | 2 | 2 | `1.py`, `2.py` |
| `librer` | 2 | 2 | `1.py`, `2.py` |
| `primer` | 2 | 2 | `1.py`, `5.py` |
| `que` | 2 | 2 | `3.py`, `4.py` |
| `segundo` | 2 | 2 | `2.py`, `5.py` |
| `son` | 2 | 2 | `3.py`, `4.py` |
| `usar` | 2 | 2 | `2.py`, `4.py` |

## Dialectic Prompts

- Thesis: `aprenderemos` centralizes 4 files; Antithesis: `como` pulls 3 files with 2 shared (Jaccard 0.40); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `aprenderemos` centralizes 4 files; Antithesis: `con` pulls 2 files with 2 shared (Jaccard 0.50); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `aprenderemos` centralizes 4 files; Antithesis: `este` pulls 5 files with 4 shared (Jaccard 0.80); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `aprenderemos` centralizes 4 files; Antithesis: `estructuras` pulls 2 files with 2 shared (Jaccard 0.50); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `aprenderemos` centralizes 4 files; Antithesis: `exploraremos` pulls 2 files with 2 shared (Jaccard 0.50); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `aprenderemos` centralizes 4 files; Antithesis: `funci` pulls 2 files with 2 shared (Jaccard 0.50); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `aprenderemos` centralizes 4 files; Antithesis: `las` pulls 3 files with 3 shared (Jaccard 0.75); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `aprenderemos` centralizes 4 files; Antithesis: `para` pulls 3 files with 2 shared (Jaccard 0.40); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `aprenderemos` centralizes 4 files; Antithesis: `python` pulls 5 files with 4 shared (Jaccard 0.80); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `aprenderemos` centralizes 4 files; Antithesis: `que` pulls 2 files with 2 shared (Jaccard 0.50); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
