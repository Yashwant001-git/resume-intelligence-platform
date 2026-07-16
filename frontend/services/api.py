"""
Handles communication with the FastAPI backend.
"""

import requests

from utils.constants import (
    API_BASE_URL,
    UPLOAD_ENDPOINT,
    DOWNLOAD_ENDPOINT,
)


class APIService:
    """
    Handles all API requests.
    """

    @staticmethod
    def upload_resume(file) -> dict:
        """
        Upload a resume to the backend.

        Returns
        -------
        dict
            JSON response from FastAPI.
        """

        url = API_BASE_URL + UPLOAD_ENDPOINT

        files = {
            "file": (
                file.name,
                file.getvalue(),
                "application/pdf",
            )
        }

        response = requests.post(
            url=url,
            files=files,
            timeout=120,
        )

        response.raise_for_status()

        return response.json()
    

    @staticmethod
    def download_excel() -> bytes:

        url = API_BASE_URL + DOWNLOAD_ENDPOINT

        response = requests.get(
            url=url,
            timeout=60,
        )

        response.raise_for_status()

        return response.content