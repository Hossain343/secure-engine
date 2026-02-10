# SecureEngine

Deterministic, auditable token derivation engine for licensing and feature gating in offline or restricted environments.

---

## What this is

SecureEngine is a small security-focused core that derives and verifies cryptographically bound tokens from:

* a client-controlled secret
* contextual metadata (device, feature, tier, etc.)
* a product-controlled master key

The output is deterministic, explainable, and verifiable without external state.

This project is intentionally minimal: it focuses on *design correctness* and *auditability*, not obfuscation or DRM tricks.

---

## What problem it solves

Many software products need to:

* enforce licenses or feature tiers
* bind licenses to devices or environments
* work offline or in air-gapped systems
* avoid complex infrastructure or time-based checks

SecureEngine provides a clean cryptographic core for these cases, without relying on:

* online servers
* clocks or timestamps
* opaque third-party services

---

## Design principles

* **Deterministic** – same inputs always produce the same token
* **Context-bound** – tokens are bound to explicit, authenticated metadata
* **Auditable** – includes a written threat model and clear security assumptions
* **Minimal** – small codebase, no hidden state
* **Composable** – intended to be embedded into larger systems

Cryptographic primitives used:

* HKDF (SHA-256)
* HMAC-SHA256

---

## Example usage

```python
from engine import SecureEngine, SecureEngineConfig

engine = SecureEngine(
    master_key=b"CHANGE_THIS_MASTER_KEY_TO_REAL_32_BYTES_MIN",
    config=SecureEngineConfig(
        max_context_items=6,
        version="1.0"
    )
)

context = {
    "device": "HWID-ABC",
    "feature": "pro",
}

token = engine.derive("CLIENT_SECRET", context)
print("Token:", token)

print("Verify:", engine.verify(token, "CLIENT_SECRET", context))
```

---

## Threat model

A formal threat model is provided in `ThreatModel.md`, including:

* in-scope and out-of-scope threats
* explicit security assumptions
* design limitations

This project does **not** claim protection against kernel-level, hardware, or side-channel attackers.

---

## Intended use

SecureEngine is suitable as:

* a licensing or feature-gating core
* a building block for custom license formats
* an internal security component for restricted environments

It is **not** intended to be a complete DRM solution.

---

## Status

This repository demonstrates a stable v1.0 design.
Future iterations may introduce domain separation and additional policy layers.
