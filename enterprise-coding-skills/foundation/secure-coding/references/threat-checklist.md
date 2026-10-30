# Threat Checklist (change-scoped)

| Area | Questions |
|---|---|
| Authz | Can a lower-privilege user invoke this? |
| Input | What’s the largest/malicious payload? |
| Data | Any PII/secrets newly logged or returned? |
| Files | Any user-controlled paths? |
| SSRF | Any user-controlled URLs fetched server-side? |
| Deserialization | Any unsafe decode of untrusted bytes? |
