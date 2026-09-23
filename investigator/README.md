# Investigator

The Python side of the monorepo: the application that investigates the
test world (`test-world/`).

## Layout

```
investigator/
-├── app/             Investigator application package
├── tests/           Unit tests (run with `python -m pytest`)
├── requirements.txt
└── README.md
```

## Run

Run all commands from the `investigator/` directory (requires Python 3.11+).

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows (Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt

python app/main.py       # entry point (stub)
python -m pytest         # tests
```

## Notes

- Evidence from investigations is written to `../data/` (raw inputs and
  processed evidence).