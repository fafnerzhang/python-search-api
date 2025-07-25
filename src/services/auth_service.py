"""
認證服務
"""

from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
from src.core.config import settings

# 創建HTTPBearer實例
security = HTTPBearer(auto_error=False)


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> Optional[str]:
    """
    驗證Bearer token (可選的)
    在生產環境中，你可以實現真正的token驗證邏輯

    Args:
        credentials: HTTP Bearer認證憑證

    Returns:
        驗證通過的token字串，如果沒有token則返回None

    Raises:
        HTTPException: 當token無效時
    """
    if credentials is None:
        return None

    # 如果設定了API_TOKEN，則驗證token
    if settings.API_TOKEN and credentials.credentials != settings.API_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid authentication token")

    return credentials.credentials
