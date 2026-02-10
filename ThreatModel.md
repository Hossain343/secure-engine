# ThreatModel.md

## Threat Model – SecureEngine (Public Summary)

### Overview

SecureEngine is a deterministic token derivation and verification design intended
for software licensing and feature gating in offline or restricted environments.

This document is a **public-facing threat model** intended to communicate design
boundaries and assumptions. It does not expose internal secrets or production
implementation details.

---

### Assets

* Master Key (product-controlled, not present in this repository)
* Client Secret (end-user controlled)
* Derived Tokens
* Context Integrity

---

### Security Goals

* Deterministic derivation (same inputs → same output)
* Context binding (tokens are tied to explicit metadata)
* Verifiability without external state
* Auditability of assumptions and limitations

---

### In-Scope Threats

* Token forgery without access to secret material
* Context tampering
* Static analysis of public source code

---

### Out-of-Scope Threats

* Kernel or OS-level compromise
* Runtime memory inspection
* Hardware or side-channel attacks

These are explicitly excluded by design.

---

### Assumptions

* Cryptographic primitives are secure
* Secrets are managed externally
* Context values are validated by the embedding system

---

### Notes

This repository intentionally omits the production cryptographic core.
It demonstrates **design thinking**, not deployable security.

---

print("Verify:", engine.verify(t, "DEMO_SECRET", ctx))
```
