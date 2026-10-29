---
name: rust-best-practices
description: Guides Rust implementation using ownership, borrowing, zero-copy APIs and typed errors. Use when writing or refactoring .rs files, optimizing allocations or configuring Cargo. Supplements the general build and testing workflow.
---

# Rust best practices

## Overview

Use BeautifulRust for Rust implementation choices, including ownership, borrowing, types, error handling, API idioms and performance.

## When to Use

Use when writing and refactoring Rust code. Load the general skills for the task as well; a language specialist does not select a different development workflow.

## Process

1. Read the project's Rust toolchain, edition, minimum supported Rust version and existing lint configuration.
2. Read the [original BeautifulRust skill](../../external-skills/beautiful-rust/skills/rust-best-practices/SKILL.md) and its relevant references. The original sources are preserved unchanged.
3. Give this specialist precedence for Rust language and idiom choices. General skills retain authority over requirements, planning, testing, systematic review, security, performance measurement and shipping. Project constraints remain binding. Surface a concrete conflict instead of silently weakening either rule.
4. Use the project's supported commands and feature combinations. The original's commands are examples, not permission to change its toolchain, enable incompatible features or alter lint policy. Preserve behavior and scope unless the task authorizes a change.
5. Read the [lint baseline](../../external-skills/beautiful-rust/lints/lints.toml) and [Clippy options](../../external-skills/beautiful-rust/lints/clippy.toml) when configuring or recommending lints. Adapt them to application versus library code and the supported toolchain; do not impose them on every crate automatically.

## Common Rationalizations

| Rationalization | Response |
|---|---|
| Rust expertise replaces the general workflow | Use the specialist within the applicable general skills. |
| The upstream lint preset must be copied verbatim | Check the crate's toolchain, purpose and existing policy first. |

## Red Flags

- Treating stylistic preference as a measured performance improvement.
- Suppressing warnings or weakening tests to get a clean result.
- Expanding a Rust review into an unrequested rewrite.

## Verification

- Changes or findings follow the original Rust guidance within the task's scope.
- The applicable general skill's verification, severity and reporting rules still hold. Incorporate Rust findings into that report rather than producing a competing report format.
- Report checks actually run, unresolved conflicts and unverified performance claims.
