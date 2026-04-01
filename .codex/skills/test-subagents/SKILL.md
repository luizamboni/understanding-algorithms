---
name: test-subagents
description: Coordinate parallel test-writing and test-running subagents for a scoped change in this repository, then consolidate files changed, tests adjusted, execution result, and next steps.
---

# Test Subagents

Use this skill when the task is to validate a scoped change by splitting work across two subagents:
- one to write or adjust the minimum relevant tests
- one to run the relevant suite and report exactly what broke

## Goal

Parallelize test coverage and test execution, then return one consolidated report.

## Preferred Scope

When the user does not specify a narrower target, inspect and prioritize these repository areas first:
- `book-examples/`
- `inverviews/` (`interviews/` in user wording; keep the repository's actual folder name)
- `others-examples/`
- `python-challenges-book/`

Prefer coordinating work for code in those directories before considering `scripts/` or other repo areas.

## Test Placement

For files under the preferred scope, assume tests should live next to the implementation file instead of in a central `tests/` directory.
- Prefer `test_<module_name>.py` when the filename is a valid Python module stem.
- If the source filename contains dashes or other characters, prefer a nearby importable test filename such as `<module_stem>_test.py`.
- Keep the test file in the same directory as the example being exercised.

## Required Roles

Create exactly two subagents:

1. `test-writer`
   - identify the affected area
   - discover the correct harness first
   - write or adjust the smallest relevant unit or integration tests
   - avoid broad changes outside scope

2. `test-runner`
   - discover the correct test command first
   - run the relevant suite
   - capture commands executed, failures, and stack traces
   - separate preexisting failures from new regressions

## Workflow

1. Inspect the repository enough to discover the likely test command and affected area before spawning subagents.
   - If the request is broad or ambiguous, inspect the preferred scope directories first and constrain the work to the smallest matching area.
   - For algorithm/example files in the preferred scope, read the source first and assume the relevant tests should be created or adjusted in that same directory.
2. Spawn both subagents in parallel with disjoint responsibilities.
3. Let `test-writer` own only test changes.
   - Direct `test-writer` to create or adjust colocated tests for preferred-scope examples.
4. Let `test-runner` own only test execution and failure analysis.
   - Direct `test-runner` to validate the narrowest relevant colocated test file or directory for the chosen example.
5. Wait for both to complete.
6. If `test-writer` added or changed tests in its fork, reproduce the same changes in the main workspace before final local validation.
7. Run the final relevant test command in the main workspace to confirm the consolidated state, targeting the colocated test when working in the preferred scope.

## Guardrails

- Do not make broad changes outside the affected area.
- Do not let the runner silently modify code.
- Do not let the writer broaden coverage unnecessarily.
- Always report old failures separately from failures introduced by the current change.
- If no tests exist yet, treat missing harness as preexisting infrastructure, not a regression.
- Do not treat a missing central `tests/` directory as a regression when the preferred scope uses colocated tests.

## Final Response

Always deliver:
- files changed
- tests created or adjusted
- execution result
- next steps
