# 音频包络：ADSR、门限与滑音

音符起音太硬、释放被截断：ADSR 分段边界错，门限漏掉边沿，力度曲线没按 gamma，滑音一次跨过头，释放采样没有从尾部数，时长除零，批量包络只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
audio/__init__.py
audio/envelope.py
tests/test_envelope.py
```

## 当前状态

`audio/envelope.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_envelope.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. ADSR 分段边界
2. 门限含边沿
3. 力度曲线 gamma
4. 滑音按速率逼近
5. 释放从尾部数
6. 时长除零

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `audio/envelope.py`
后 15 条用例应全部通过。
