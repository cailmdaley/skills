---
name: implementing-code
description: >
  Implement scientific analysis code with quality and correctness following research workflow standards.
  Use when writing research code, implementing algorithms, creating analysis scripts, or developing
  scientific computations. Triggers on: "implement", "write code", "code this up", "analysis script",
  "algorithm", "compute", "calculate", or any request to write or implement scientific/numerical code.
---

# Implementing Code

**Core philosophy**: Write it right the first time — clean, concise, conceptually dense code that doesn't need editing afterward. Zero linting violations (ruff or project-specified tools). Check CLAUDE.md for project-specific standards.

## Conceptual Density

Fit as many related operations into one line as possible, where each line has an understandable big-picture purpose. Each line = one complete concept. 88 char max (ruff default).

```python
# Inline calculations in dict construction — not scattered assignments
results = {
    "chi2_E": hartlap_factor * (En @ np.linalg.solve(cov_E, En)),
    "pte_B": 1 - stats.chi2.cdf(chi2_B, nmodes),
    "cov": np.cov(np.array(samples).T),
}

# Eliminate repetition with comprehensions
chi_E, chi_B, chi_EB = [
    np.sum(signal**2 / noise**2)
    for signal, noise in zip((ee, bb, eb), (noise_ee, noise_bb, noise_eb))
]

# Consolidate repeated plotting blocks into loops
for ax, (cl, err, fmt, label) in zip(axes, plot_data):
    ax.errorbar(ell_bins, cl, yerr=err, fmt=fmt)
    ax.set(xlabel=r"$\ell$", ylabel=label, title=f"{label} Power Spectrum")
```

### Concise conditionals

```python
# One-line conditionals over verbose if/else blocks
n_eff = n_samples if cov_path_int is not None else npatch
version_results = results_list[idx] or self.calculate_pure_eb()
output_path = user_path or generate_default_path()

# Short-circuit execution
(var_method == "semianalytic") and self.calculate_semianalytic_cov()
```

### Natural line breaking

When code exceeds 88 chars, break at logical boundaries:
- Comprehensions: after `[` and before `for`
- Function calls: at commas between argument groups
- Dicts: one key-value pair per line
- Chained operations: at method calls or operators

## Anti-Patterns

- **Unnecessary intermediates**: `temp = solve(A, b); result = factor * temp` -- combine into one conceptual line
- **Scattered dict assignments**: `results["a"] = a; results["b"] = b` -- use dict construction with inline calculations
- **Verbose conditionals**: 4-line if/else for simple assignment -- use ternary or `or`
- **Defensive `.get()` with defaults**: `config.get("key", default)` hides missing config -- use `config["key"]` to fail fast
- **Unnecessary try/except**: let errors propagate; missing files and bad inputs are real problems
- **Session-specific comments**: "per your request", "switched to new method" -- comments should be timeless

## Comment Philosophy

Comments explain *why* and *context*, never *what*. Good: `# Hartlap correction for finite sample bias`. Bad: `# Create numpy array`. Remove artifacts like "change to scipy implementation" from library code.

## Error Handling

Trust scientific libraries to validate their domains. Skip defensive programming. Let errors propagate -- failed fast is better than hidden bugs. Use defensive patterns only for known edge cases with clear scientific justification.

## Validation

- Spot-check that code runs without crashing
- Test with toy data where feasible
- Extended validation (literature comparison, edge cases) only when requested
- Focus on "does it work" over exhaustive test suites

## Working Agreements

- Ask for clarification on ambiguous requirements rather than making design decisions
- Batch related implementations together in a single response
- Before implementing numerical algorithms, think through stability and convergence
- Preserve existing project structure and codebase patterns
- Deliver working code, basic validation, and integration notes (if connecting to existing code)
