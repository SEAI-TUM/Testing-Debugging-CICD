# Week 10 — Exercise Session: Testing, Debugging & CI/CD

You will write unit tests, expose a bug with
property-based testing, generate tests with an AI assistant and learn why
you still own the oracle, debug a failure with the scientific method, and
automate everything with GitHub Actions.

---

## Setup (2 minutes)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -v                        # the provided tests should run
```

```
aisd-week10-exercises/
├── src/
│   ├── cart.py          # Exercise 1 — pricing library (Create simple tests)
│   ├── rle.py           # Exercises 2 & 4 — run-length coding (has a bug)
│   └── pricing_ai.py    # Exercise 3 — bulk pricing (spec vs. code mismatch)
├── tests/
│   ├── test_cart.py        # Exercise 1 — skeleton with TODOs
│   ├── test_rle.py         # Exercise 2 — weak example test + TODO
│   └── test_pricing_ai.py  # Exercise 3 — paste AI tests, then add the oracle
└── .github/workflows/
    └── ci.yml           # Exercise 5 — skeleton CI pipeline

```


---

## Exercise 1 — Anatomy of a unit test (~12 min)

**File:** `tests/test_cart.py` · **Target:** `src/cart.py`

`src/cart.py` is a small, *correct* pricing library. Pin its behaviour down
with tests, following the **Arrange–Act–Assert** shape in the worked example:

1. Discount happy path: `apply_discount(100.0, 20) == 80.0`.
2. Boundary values with `@pytest.mark.parametrize` — 0 % and 100 %.
3. Error handling with `pytest.raises(ValueError)` for an out-of-range percent.
4. Aggregation: `cart_total([]) == 0.0`, plus a multi-item cart with a discount.

```bash
pytest tests/test_cart.py -v
pytest --cov=src --cov-report=term-missing
```

---

## Exercise 2 — Property-based testing exposes a bug (~12 min)

**File:** `tests/test_rle.py` · **Target:** `src/rle.py`

`src/rle.py` round-trips text: `decode(encode(s))` should equal `s`. The
shipped example test passes **and reaches 100 % line coverage** — yet the
code is wrong. Add a property test with [Hypothesis](https://hypothesis.readthedocs.io).
Plain random text almost never repeats 10+ times, so feed it runs of a single
repeated character and let Hypothesis pick the length:

```python
from hypothesis import given, strategies as st

# A string of one repeated character, length 0..20.
run = st.integers(min_value=0, max_value=20).map(lambda n: "a" * n)

@given(run)
def test_roundtrip(s):
    assert decode(encode(s)) == s
```

Run it and read the **minimal failing example** Hypothesis prints (it shrinks
to a run of 10 identical chars, i.e. `"aaaaaaaaaa"`):

```bash
pytest tests/test_rle.py::test_roundtrip -v
```

---

## Exercise 3 — Generate tests with AI, then own the oracle (~15 min)

**File:** `tests/test_pricing_ai.py` · **Target:** `src/pricing_ai.py`

`final_price` carries a **spec in its docstring** (10 or more units → 10 % discount)
and an implementation that *almost* matches it.

1. **Generate.** Use your AI assistant (Copilot, Cursor, Claude, ChatGPT, …)
   to write a pytest suite for `final_price`.
2. **Run.** `pytest tests/test_pricing_ai.py -v` — the AI tests pass, and
   `pytest --cov=src.pricing_ai` likely shows 100 % coverage.
3. **Check the oracle.** Read the spec. Add one test for the boundary
   `quantity == 10` asserting the value the **spec** requires, not the value
   the code returns:

   ```python
   def test_boundary_10_units_gets_discount():
       assert final_price(100.0, 10) == 900.0   # SPEC: 10+ units -> 10 % off
   ```
---

## Exercise 4 — Debug it with the scientific method (~10 min)

**Target:** `src/rle.py`

Use the minimal failing example from Exercise 2 as your reproduction. Walk the
loop: **observe → hypothesize → predict → experiment → fix.**

```bash
pytest tests/test_rle.py::test_roundtrip -x --pdb
```

Trace the *infection chain* backwards from the failure to the defect, fix
`decode`, then re-run Exercise 2

<details>
<summary>Hint (open only if stuck)</summary>

Encode `"a"` repeated 10 times. What does `encode` produce, and how many
characters of the count does `decode` actually read?
</details>

---

## Exercise 5 — Automate it with GitHub Actions (~12 min)

**File:** `.github/workflows/ci.yml`

Complete the TODOs so that, on every push and pull request, the workflow
checks out the code, sets up Python 3.12, installs `requirements.txt`, and
runs `pytest --cov=src`. Push to GitHub and watch the run under the
**Actions** tab.

---

## Now: your own project

- Add at least one **meaningful unit test** for a function you wrote — and if
  you draft it with AI, **verify the assertion against your intent**, the way
  you did in Exercise 3.
- Add a `.github/workflows/ci.yml` that runs your tests on every push.
- Push and confirm the green check in the **Actions** tab.

---

## Test generators to explore (optional)

Tools you can point at this repo — or your own project — to generate tests:

| Tool | Kind | Try it |
|------|------|--------|
| **Pynguin** | search-based (coverage) | `pip install pynguin`; Python's EvoSuite (DynaMOSA) |
| **Hypothesis ghostwriter** | property-based | `hypothesis write src.cart` drafts property tests |
| **CoverUp** | AI, coverage-guided | `pip install coverup` (needs an OpenAI/Anthropic key) |
| **Copilot / Cursor / Claude** | AI assistant | generate tests inline as you code (Exercise 3) |

Then check whether the generated tests actually *catch bugs*, not just run lines,
with mutation testing — **mutmut** (`pip install mutmut`) or **Cosmic Ray**.


## Quick command reference

```bash
pytest -v                                   # run everything, verbose
pytest tests/test_rle.py::test_roundtrip    # run one test
pytest -x --pdb                             # stop at first failure, debug
pytest --cov=src --cov-report=term-missing  # coverage + missing lines
```
