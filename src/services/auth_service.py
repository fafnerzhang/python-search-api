"""
認證服務
"""

from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.core.config import settings

# 創建HTTPBearer實例 - 強制要求token
security = HTTPBearer(auto_error=True)


def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> str:
    """
    驗證Bearer token (必須提供)
    在所有環境中都強制要求token驗證

    Args:
        credentials: HTTP Bearer認證憑證

    Returns:
        驗證通過的token字串

    Raises:
        HTTPException: 當token無效或未提供時
    """
    # 如果沒有設定API_TOKEN，拋出配置錯誤
    if not settings.API_TOKEN:
        raise HTTPException(
            status_code=500,
            detail="API_TOKEN not configured. Please set API_TOKEN environment variable."  # noqa: E501
        )

    # 驗證token是否匹配
    if credentials.credentials != settings.API_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid authentication token")

    return credentials.credentials
