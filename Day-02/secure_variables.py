
"""
Day 2
Type hints + truly unbreakable constants (2025 production standard)
"""

from typing import Final
from pathlib import Path

# ──────── Truly unbreakable constants (impossible to change) ────────
API_BASE_URL: Final[str] = "https://api.securebank.com/v2"
MAX_LOGIN_ATTEMPTS: Final[int] = 5
SESSION_TIMEOUT_MINUTES: Final[int] = 30
DEBUG_MODE: Final[bool] = False

# ──────── Regular typed variables (can change) ────────
user_name: str = "aadija1n"
user_id: int = 1337
balance: float = 9_999.99
is_admin: bool = True

# ──────── Function with proper type hints ────────
def greet_user(name: str, day: int) -> None:
    """Prints a secure welcome message. Returns nothing."""
    print(f"Welcome back, {name}! Day {day}/45")
    print(f"User ID: {user_id} | Balance: ${balance:,.2f}")

def main() -> None:
    greet_user(user_name, current_day := 2)
    print(f"Session expires in {SESSION_TIMEOUT_MINUTES} minutes")
    print(f"Running from: {Path(__file__).resolve()}")

if __name__ == "__main__":
    main()

# Try this later (uncomment one line at a time):
# MAX_LOGIN_ATTEMPTS = 999     # ← mypy/Pylance will scream in red!
# API_BASE_URL = "http://evil.com"   # ← instantly blocked by tools