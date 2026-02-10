SecureEngine – Public API Contract

This document defines the logical interface of SecureEngine. It is intended for design review and integration discussions.

No production implementation is included.

Core Operations
derive(secret, context) -> token

Derives a deterministic token bound to the provided secret and context.

secret: client-provided secret (string / bytes)

context: key-value metadata (device, feature, tier, etc.)

token: opaque string representation

Properties:

Deterministic

Context-bound

Stateless

verify(token, secret, context) -> boolean

Verifies whether a token is valid for the given secret and context.

Properties:

Pure function

No external dependencies

Symmetric derivation

Context Rules

Context is canonicalized before use

Maximum item count is enforced

Keys and values have explicit size limits

Non-Goals

DRM obfuscation

Anti-debugging

Hardware binding

These concerns are intentionally left to higher layers.
