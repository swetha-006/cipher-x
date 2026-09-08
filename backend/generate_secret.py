import secrets
print('JWT_SECRET='+secrets.token_urlsafe(48))
print('EVIDENCE_ENCRYPTION_KEY='+__import__('base64').urlsafe_b64encode(secrets.token_bytes(32)).decode())
