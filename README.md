# 🎶 LyricAI

欢迎使用 **LyricAI.py**！🎸✨ 这个小工具可以帮助您轻松创建歌词和简单的简谱。（其实是早期为测试AI能力瞎搞的项目💩

## 功能
- **自动生成歌词**：不需要担心创作障碍。只需输入歌曲标题和风格，按照提示操作即可。
- **支持多种风格**：选择 `流行`、`摇滚`、`乡村`、`爵士` 和 `古典`。
- **简单的简谱**：为您的歌词提供基本的简谱轮廓。❌（AI乱编✅

## 入门指南

### 先决条件
- Python 3.6 或更高版本 🐍
- OpenAI API 密钥 🔑

### 安装
1. **克隆此存储库**：
    ```bash
    clone https://github.com/DeepFog-ORG/LyricAI.git
    cd LyricAI
    ```
2. **安装所需软件包**：
    ```bash
    pip install openai
    ```

### 设置
在脚本中用你的实际 OpenAI API 密钥替换 `your_api_key_here`：
```python
openai.api_key = "your_api_key_here"
```

### 运行程序
打开你的终端并运行脚本：
```bash
python LyricAI.py
```
按照屏幕提示操作，一条🐉。

### 示例
这里是您可能会看到的预览：
```plaintext
欢迎使用歌词生成器！
请按照提示输入歌曲标题和曲风，我们将为您生成歌词和简谱。
请输入歌曲标题：Summer Nights
请输入曲风（可选项：'pop', 'rock', 'country', 'jazz', 'classical'）：
曲风：pop

生成的'Summer Nights'的pop歌曲的歌词：

Under the starry skies, we take a ride,
Feeling the summer breeze, with you by my side...

生成的'Summer Nights'的简谱：

C D E F G A B
A B C D E F G
...
```

## 贡献
有想法让这个项目变得更酷？提出拉取请求或提交问题。

## 许可证
本项目基于 CC0 1.0 许可证发布。

## 致谢
- 感谢 OpenAI 提供的惊人 API！🧠（这段其实是GPT在自夸……
- 还有你，因为使用这个工具而变得了不起。继续 rock！🤓🤘

---

祝您创作愉快！🎶 如果您喜欢这个项目，请不要忘记为仓库加星⭐️。

---
