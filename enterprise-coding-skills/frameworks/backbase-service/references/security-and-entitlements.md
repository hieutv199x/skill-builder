# Security & Entitlements

## Detect

- OAuth2 resource server configuration
- Method security / custom entitlement annotations
- Filters checking service agreements / user context
- Neighbor endpoints’ required scopes/authorities

## Rules

1. Copy the **same** authz pattern as sibling operations of equal sensitivity
2. Fail closed — don’t `permitAll` sensitive banking operations
3. Enforce on server — UI checks are not enough
4. Don’t log tokens or security contexts containing secrets

## Changes that need approval

- Widening access (more roles, public exposure)
- New authentication mechanism
- Cross-tenant data access changes

## Tests

Cover `401` unauthenticated and `403` forbidden for protected writes when the suite supports security tests.
