#!/usr/bin/env python3
"""
新架構的應用程式入口點
"""
import sys
import os

# 添加src目錄到Python路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)

# 現在導入應用程式
from app import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "run_new:app",
        host="0.0.0.0",
        port=8999,
        reload=True
    )
