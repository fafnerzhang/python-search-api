"""
日誌配置模組
"""

import logging
import sys
from typing import Optional


def setup_logging(
    level: str = "INFO", format_string: Optional[str] = None
) -> logging.Logger:
    """
    設定應用程式日誌

    Args:
        level: 日誌等級 (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format_string: 自定義日誌格式

    Returns:
        配置好的logger實例
    """
    if format_string is None:
        format_string = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # 設定基本配置
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format=format_string,
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    # 建立並返回logger
    logger = logging.getLogger("ddgs_api")
    logger.setLevel(getattr(logging, level.upper()))

    return logger


# 建立全域logger實例
logger = setup_logging()
