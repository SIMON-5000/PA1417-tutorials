# PA1417 Tutorials

A hands-on testing tutorial repository for the PA1417 course. Students work through a sequence of guided exercises covering unit and integration testing in Python using pytest, progressing from basic assertions through fixtures, parameterization, and mocking.

## Repository Structure

```
pa1417-tutorials/
├── docs/                       ← tutorial documents and design notes
├── src/                        ← source files students write tests against
│   ├── unit/                   ← modules for unit test tutorials
│   └── integration/            ← modules for integration test tutorials
├── test/
│   ├── student/                ← where students write their tests
│   │   ├── unit/
│   │   └── integration/
│   └── _solutions/             ← reference solutions (try not to peek!)
│       ├── unit/
│       └── integration/
├── pytest.ini                  ← pytest configuration
├── requirements.txt            ← Python dependencies
└── LICENSE
```

Source files in `src/` are provided and should not be modified. Students create test files under `test/student/`, using a stub file in each tutorial as the starting point. Complete solutions are available under `test/_solutions/` for reference.

## Getting Started

See [docs/01 Tutorial Prep and Introduction.md](docs/01%20Tutorial%20Prep%20and%20Introduction.md) for full setup instructions. The short version:

```shell
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest test/_solutions           # all tests should pass
```

## Tutorial Sequence

Work through the tutorials in order. Each builds on the previous.

| # | Tutorial | Key concept |
|---|----------|-------------|
| 01 | [Prep and Introduction](docs/01%20Tutorial%20Prep%20and%20Introduction.md) | Environment setup; repository orientation |
| 02 | [Unit Tests — Assert](docs/02%20Unit%20Tests%20-%20Assert.md) | `assert`, AAA pattern, equivalence partitioning |
| 03 | [Unit Tests — Fixtures](docs/03%20Unit%20Tests%20-%20Fixtures.md) | `@pytest.fixture`, shared setup |
| 04 | [Unit Tests — Parameterization](docs/04%20Unit%20Tests%20-%20Parameterization.md) | `@pytest.mark.parametrize` |
| 05 | [Unit Tests — Mocking Basics](docs/05%20Unit%20Tests%20-%20Mocking%20Basics.md) | `MagicMock`, injected dependencies, `.return_value` |
| 06 | [Unit Tests — Mocking Patching](docs/06%20Unit%20Tests%20-%20Mocking%20Patching.md) | `patch`, namespace rule, stacked decorators |
| 07 | [Integration Tests — Basics](docs/07%20Integration%20Tests%20-%20Basics.md) | Two real components; no mocking |
| 08 | [Integration Tests — Fixtures](docs/08%20Integration%20Tests%20-%20Fixtures.md) | `yield` teardown, filesystem side effects |
| 09 | [Integration Tests — Mocking Injected](docs/09%20Integration%20Tests%20-%20Mocking%20Injected.md) | `MagicMock(spec=...)`, selective mocking, A→B→C chains |
| 10 | [Integration Tests — Patching](docs/10%20Integration%20Tests%20-%20Patching.md) | `patch` in integration tests, namespace rule |

The full design rationale and per-tutorial source/test file index is in [docs/00 Tutorial Design.md](docs/00%20Tutorial%20Design.md).

## Running Tests

Run the full solution suite (should always be green):

```shell
pytest test/_solutions
```

Run only your own work:

```shell
pytest test/student
```

Run a specific tutorial's tests:

```shell
pytest test/student/unit/asserts
```

Coverage is reported automatically on every run (configured in `pytest.ini`).

## License

MIT — see [LICENSE](LICENSE).
