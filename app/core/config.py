from pathlib import Path

DB_URL="postgresql://accounting_user:accounting_user@localhost:5432/accounting_db"

PRIVATE_KEY=Path("keys/private.pem").read_text()
PUBLIC_KEY=Path("keys/public.pem").read_text()
