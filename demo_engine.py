""" This file contains a non-production demo implementation.

It exists solely to demonstrate the API shape and usage flow. The logic is intentionally simplified and MUST NOT be used for real security purposes. """

import hashlib

class DemoSecureEngine: def derive(self, secret: str, context: dict) -> str: material = secret + "|" + "|".join(f"{k}={v}" for k, v in sorted(context.items())) return hashlib.sha256(material.encode()).hexdigest()
def verify(self, token: str, secret: str, context: dict) -> bool:
return self.derive(secret, context) == token
if name == "main": engine = DemoSecureEngine()
  ctx = {
"device": "DEMO-DEVICE",
"feature": "pro",
}


t = engine.derive("DEMO_SECRET", ctx)
print("Token:", t)
print("Verify:", engine.verify(t, "DEMO_SECRET", ctx))
