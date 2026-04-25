#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""测试个股推送功能"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from src.config import get_config
from src.core.pipeline import StockAnalysisPipeline
from src.enums import ReportType

# 只分析 1 只股票
test_stock = "600519"  # 贵州茅台

config = get_config()
pipeline = StockAnalysisPipeline(config)

print(f"🧪 开始测试个股分析推送...")
print(f"📊 测试股票: {test_stock}")
print(f"📧 邮件渠道: {pipeline.notifier.get_channel_names()}")

# 运行分析
results = pipeline.run(
    stock_codes=[test_stock],
    dry_run=False,
    send_notification=True
)

if results:
    print(f"\n✅ 分析成功!")
    for r in results:
        print(f"  - {r.code}: {r.operation_advice} (评分 {r.sentiment_score})")
else:
    print(f"\n❌ 分析失败，请检查日志")
