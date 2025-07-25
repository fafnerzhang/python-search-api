"""
DuckDuckGo搜尋服務
"""

import asyncio
from typing import List, Dict, Any
from src.core.logging import logger

try:
    from ddgs import DDGS
except ImportError:
    logger.error("DDGS not found. Please install with: pip install ddgs==9.4.3")
    raise


class DDGSService:
    """DuckDuckGo搜尋服務類"""

    @staticmethod
    async def safe_ddgs_operation(
        operation_func, *args, **kwargs
    ) -> List[Dict[str, Any]]:
        """
        安全執行DDGS操作，處理可能的異常

        Args:
            operation_func: DDGS操作函數
            *args: 位置參數
            **kwargs: 關鍵字參數

        Returns:
            搜尋結果列表

        Raises:
            Exception: 當DDGS操作失敗時
        """
        try:
            # 在線程池中執行同步的DDGS操作
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, operation_func, *args, **kwargs)
            return result
        except Exception as e:
            logger.error(f"DDGS operation failed: {str(e)}")
            raise Exception(f"Search operation failed: {str(e)}")

    @staticmethod
    def text_search(
        query: str,
        region: str = "wt-wt",
        safesearch: str = "moderate",
        timelimit: str = None,
        max_results: int = 10,
    ) -> List[Dict[str, Any]]:
        """
        DuckDuckGo文字搜尋

        Args:
            query: 搜尋關鍵字
            region: 地區代碼
            safesearch: 安全搜尋等級
            timelimit: 時間限制
            max_results: 最大結果數

        Returns:
            搜尋結果列表
        """
        logger.info(f"Starting DDGS text search for query: {query}")

        try:
            with DDGS() as ddgs:
                results = list(
                    ddgs.text(
                        query,  # query as positional argument
                        region=region,
                        safesearch=safesearch,
                        timelimit=timelimit,
                        max_results=max_results,
                    )
                )

                logger.info(f"DDGS text search completed. Found {len(results)} results")
                return results

        except Exception as e:
            logger.error(f"DDGS text search failed: {str(e)}")
            raise

    @staticmethod
    def image_search(
        query: str,
        region: str = "wt-wt",
        safesearch: str = "moderate",
        size: str = None,
        color: str = None,
        type_image: str = None,
        layout: str = None,
        license_image: str = None,
        max_results: int = 10,
    ) -> List[Dict[str, Any]]:
        """
        DuckDuckGo圖片搜尋

        Args:
            query: 搜尋關鍵字
            region: 地區代碼
            safesearch: 安全搜尋等級
            size: 圖片大小
            color: 圖片顏色
            type_image: 圖片類型
            layout: 圖片佈局
            license_image: 圖片授權
            max_results: 最大結果數

        Returns:
            圖片搜尋結果列表
        """
        logger.info(f"Starting DDGS image search for query: {query}")

        try:
            with DDGS() as ddgs:
                results = list(
                    ddgs.images(
                        keywords=query,
                        region=region,
                        safesearch=safesearch,
                        size=size,
                        color=color,
                        type_image=type_image,
                        layout=layout,
                        license_image=license_image,
                        max_results=max_results,
                    )
                )

                logger.info(
                    f"DDGS image search completed. Found {len(results)} results"
                )
                return results

        except Exception as e:
            logger.error(f"DDGS image search failed: {str(e)}")
            raise

    @staticmethod
    def news_search(
        query: str,
        region: str = "wt-wt",
        safesearch: str = "moderate",
        timelimit: str = None,
        max_results: int = 10,
    ) -> List[Dict[str, Any]]:
        """
        DuckDuckGo新聞搜尋

        Args:
            query: 搜尋關鍵字
            region: 地區代碼
            safesearch: 安全搜尋等級
            timelimit: 時間限制
            max_results: 最大結果數

        Returns:
            新聞搜尋結果列表
        """
        logger.info(f"Starting DDGS news search for query: {query}")

        try:
            with DDGS() as ddgs:
                results = list(
                    ddgs.news(
                        keywords=query,
                        region=region,
                        safesearch=safesearch,
                        timelimit=timelimit,
                        max_results=max_results,
                    )
                )

                logger.info(f"DDGS news search completed. Found {len(results)} results")
                return results

        except Exception as e:
            logger.error(f"DDGS news search failed: {str(e)}")
            raise
