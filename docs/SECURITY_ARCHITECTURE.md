# CIPHER-X Secure Architecture

## Security controls implemented

- JWT access tokens with short expiry and hashed refresh-token storage.
- Argon2 password hashing for the built-in research accounts.
- RBAC: ADMIN, INVESTIGATOR, ANALYST/VIEWER case-member model.
- Case-level authorization on evidence, graph, timeline, search and RAG endpoints.
- Upload size, extension, MIME and magic-byte checks.
- Quarantine-before-vault workflow.
- Optional ClamAV malware scanning before encrypted storage.
- AES-compatible Fernet authenticated encryption for evidence at rest.
- SHA-256 fingerprinting of the original artifact and verification again at download.
- Audit log for authentication, case actions, evidence access, search and RAG activity.
- Per-process rate limits for login, API, upload, search and RAG endpoints.
- Security response headers and restricted CORS.
- RAG prompt-injection guard and explicit separation of evidence from instructions.
- Retrieval is constrained to the authorized case before semantic search.
- No API key is sent to the browser; optional LLM access is server-side only.

## Threat model

The application treats uploaded documents as **untrusted input**. A document may contain malicious text, prompt-injection content, misleading metadata, or a filename designed to traverse directories. The parser, OCR and RAG layers must never treat document text as trusted instructions.

The application is an academic/research prototype using synthetic or authorized data. It is not a certified forensic acquisition suite and should not be used to make autonomous determinations of guilt.

## Production hardening checklist

1. Replace SQLite with PostgreSQL and managed backups.
2. Put evidence in private object storage with KMS-managed keys.
3. Run parsers/OCR in isolated workers or containers.
4. Use a dedicated secrets manager; never commit `.env` or encryption keys.
5. Put the API behind HTTPS and a reverse proxy/WAF.
6. Use centralized rate limiting (Redis) rather than the process-local limiter.
7. Enable ClamAV or an enterprise malware scanner.
8. Add SSO/OIDC and MFA for real organizations.
9. Add immutable/WORM audit storage for operational environments.
10. Run dependency, SAST, DAST and container scans in CI/CD.
