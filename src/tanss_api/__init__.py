"""Ein Python-Client fuer die TANSS-REST-Schnittstelle. Getestet gegen TANSS 10.10.

Der Einstieg ist :class:`TanssApi`: ``TanssApi.create(optionen, token)`` baut die Verbindungsschicht,
``api.rest`` ist die vollstaendige erzeugte Schnittstelle, ``api.session`` deckt Anmelden, Erneuern und
Praegen ab.
"""

from .api import TanssApi, TanssApiTokenAuthenticationProvider
from .availability import ApiAvailability
from .errors import TanssApiError
from .options import TanssApiOptions
from .session import TanssLoginResult, TanssSession
from .token_roles import TokenRole, includes_user, is_reachable_with_login_token, required_for
from .tokens import (
    MutableTokenProvider,
    StaticTokenProvider,
    TokenProvider,
    bearer_header_value,
)

__version__ = "1.0.0"
"""Die Fassung dieser Bibliothek."""

__all__ = [
    "ApiAvailability",
    "MutableTokenProvider",
    "StaticTokenProvider",
    "TanssApi",
    "TanssApiError",
    "TanssApiOptions",
    "TanssApiTokenAuthenticationProvider",
    "TanssLoginResult",
    "TanssSession",
    "TokenProvider",
    "TokenRole",
    "__version__",
    "bearer_header_value",
    "includes_user",
    "is_reachable_with_login_token",
    "required_for",
]
