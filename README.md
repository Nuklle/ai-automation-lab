# ai-automation-lab

Starter repository for experiments, notes, and small automation workflows in Python.

## Layout

- `src/ai_automation_lab/`: application package
- `tests/`: automated tests
- `data/sample/`: sample input data
- `data/output/`: generated output data
- `docs/`: weekly notes and project docs
- `notes/`: quick references and cheatsheets

## Quick start

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .[dev]
pytest
python -m ai_automation_lab.main
```
