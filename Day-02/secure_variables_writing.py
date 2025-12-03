
"""
Day 2
Modern, safe, production-ready variables (2025 standard)
"""

from pathlib import Path

# ──────── Immutable constants (never change) ────────
API_BASE_URL: str = "https://api.example.com/v1"
MAX_LOGIN_ATTEMPTS: int = 5
DEBUG_MODE: bool = False
VERSION: str = "2.0.0"

# ──────── Regular variables (can change) ────────
user_name: str = "aadija1n"
current_day: int = 2
score: float = 98.7
is_premium_user: bool = True

# ──────── Safe string building with f-strings only ────────
welcome = f"Welcome back, {user_name}!"
progress = f"Day {current_day}/45 → Score: {score}%"
status = f"Premium: {is_premium_user} | Debug: {DEBUG_MODE}"

# ──────── Walrus operator example (real-world use) ────────
log_file = Path(__file__).parent / "app.log"
if (size := log_file.stat().st_size if log_file.exists() else 0) > 1_000_000:
    print(f"Warning: Log file is getting big: {size:,} bytes")

def main() -> None:
    print(welcome)
    print(progress)
    print(status)
    print(f"Running from: {Path(__file__).resolve()}")

if __name__ == "__main__":
    main()
