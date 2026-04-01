---
name: test-runner
description: Run the relevant test suite for a change, capture failures and stack traces, and separate preexisting failures from new regressions. Use when validating code changes in this repository.
---

# Test Runner

Use this skill when the task is to validate a change by running tests and reporting exactly what broke.

## Goal

Run the right test command for the affected area, capture the result precisely, and distinguish preexisting failures from failures introduced by the current change.

## Workflow

1. Discover the correct test command before running anything.
   - Inspect existing manifests and test files first.
   - Prefer the repo's established runner if one exists.
   - If this repo has no configured Python test tool and only standard library testing is available, use `python3 -m unittest discover -s tests -p 'test_*.py' -v`.
2. Run the narrowest relevant suite that still validates the change.
3. Capture:
   - commands executed
   - pass/fail result
   - stack traces or import errors
   - whether the failure is preexisting infrastructure, preexisting test failure, or a new regression
4. If tests cannot start because the harness is missing, report that as preexisting infrastructure failure rather than a code regression.

## Guardrails

- Do not modify code unless the task explicitly asks for it.
- Do not collapse old and new failures into one bucket.
- Be exact about what failed first and why.

## Final Response

Report:
- commands executed
- execution result
- exact failures and stack traces
- clear separation between preexisting failures and new failures
