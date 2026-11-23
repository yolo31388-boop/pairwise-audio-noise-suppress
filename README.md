# pairwise-audio-noise-suppress

## 领域

游戏、图形与多媒体

## 主题

音频降噪

## 说明

噪声谱冻结、增益平滑与起音保护。

初始状态下 `media/audio_noise_suppress.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
