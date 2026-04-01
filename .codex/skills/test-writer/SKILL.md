---
name: test-writer
description: Write or adjust the smallest relevant unit or integration tests for the affected area in this repository. Use when a change needs minimal coverage added without broad refactors.
---

# Test Writer

Use this skill when the task is to add or adjust tests for a concrete change.

## Goal

Add the minimum relevant coverage for the affected behavior and nothing broader.
For algorithm examples in this repository, read the example source first and create the corresponding test file in the same directory as the code under test.

## Preferred Scope

When the user does not specify a narrower target, prioritize changes under these repository areas:
- `book-examples/`
- `inverviews/` (`interviews/` in user wording; keep the repository's actual folder name)
- `others-examples/`
- `python-challenges-book/`

Prefer writing or adjusting tests for code in those directories before considering `scripts/` or other repo areas.

## Test Placement

For files under the preferred scope, place tests next to the implementation file instead of requiring a central `tests/` directory.
- Prefer `test_<module_name>.py` when the filename is a valid Python module stem.
- If the source filename contains dashes or other characters that make that awkward, prefer a nearby test filename that stays importable and clearly maps to the source, such as `<module_stem>_test.py`.
- Keep the test file in the same directory as the example being exercised.

## Workflow

1. Identify the changed or affected area first.
   - If the request is broad or ambiguous, inspect the preferred scope directories first and constrain the work to the smallest matching area.
   - Read the algorithm/example source file before writing tests so the assertions match the actual behavior implemented there.
2. Discover the test harness before writing tests.
   - Look for `pytest`, `unittest`, `Makefile`, `pyproject.toml`, `package.json`, or existing test files.
   - Prefer the project's existing runner and conventions.
   - If there is no configured harness in this repo and it is a small Python-only change, default to `unittest`.
3. Add only the smallest useful tests that prove expected behavior.
   - For standalone algorithm examples, prefer focused input/output tests and edge cases over broad integration coverage.
4. Avoid wide refactors, fixture churn, or unrelated cleanup.
5. If the change produces files or outputs, assert stable properties such as path, existence, shape, size, or return values before asserting fragile implementation details.

## Guardrails

- Do not make broad changes outside the affected area.
- Reuse existing conventions if they exist.
- If no tests exist, create the narrowest viable test file in the same directory as the target example when working in the preferred scope.
- Prefer deterministic assertions over visual or snapshot-heavy checks unless the task explicitly requires them.

## Final Response

Report:
- files changed
- tests created or adjusted
- what behavior each test covers
