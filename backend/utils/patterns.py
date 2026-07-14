EMAIL_PATTERN = (
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
)

PHONE_PATTERN = (
    r"(\+?\d[\d\s\-]{8,}\d)"
)

LINKEDIN_PATTERN = (
    r"(https?://)?(www\.)?linkedin\.com/[^\s]+"
)

GITHUB_PATTERN = (
    r"(https?://)?(www\.)?github\.com/[^\s]+"
)

URL_PATTERN = (
    r"https?://[^\s]+"
)