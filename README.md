<div align="center">

# NCATBOT

![logo.png](https://socialify.git.ci/liyihao1110/NcatBot/image?custom_description=ncatbot%EF%BC%8C%E5%9F%BA%E4%BA%8E+OneBot11%E5%8D%8F%E8%AE%AE+%E7%9A%84+QQ+%E6%9C%BA%E5%99%A8%E4%BA%BA+Python+SDK%EF%BC%8C%E5%BF%AB%E9%80%9F%E5%BC%80%E5%8F%91%EF%BC%8C%E8%BD%BB%E6%9D%BE%E9%83%A8%E7%BD%B2%E3%80%82&description=1&font=Jost&forks=1&issues=1&logo=https%3A%2F%2Fimg.remit.ee%2Fapi%2Ffile%2FAgACAgUAAyEGAASHRsPbAAO9Z_FYKczZ5dly9IKmC93J_sF7qRUAAmXEMRtA2ohX1eSKajqfARABAAMCAAN5AAM2BA.jpg&pattern=Signal&pulls=1&stargazers=1&theme=Auto)

[![OneBot v11](https://img.shields.io/badge/OneBot-v11-black.svg)](https://github.com/botuniverse/onebot)
<a><img src="https://img.shields.io/badge/License-NcatBot%20License-green.svg"></a>
<a href="https://qm.qq.com/q/B4zmXOlKik"><img src="https://img.shields.io/badge/官方群聊-201487478-brightgreen.svg"></a>
<a href="https://qm.qq.com/q/sxda3KUwqO"><img src="https://img.shields.io/badge/娱乐群聊-624120550-brightgreen.svg"></a>


[项目文档](https://docs.ncatbot.xyz) & [插件社区](https://www.ityzs.com/)

**ncatbot** 是基于 OneBot11 协议的 Python SDK，它提供了一套方便易用的 Python 接口，用于开发 QQ 机器人。

</div>

## 项目特性

- **快速上手**：简洁的API设计，轻松构建机器人
- **高度扩展**：支持插件系统，满足各种需求
- **功能丰富**：支持群聊、私聊、消息转发等多种场景
- **安全可靠**：完善的错误处理和权限控制
- **文档完善**：详细的文档和丰富的示例

## 项目归属

本项目归属于 **ncatbot项目组** 所有

## 联系我们

1. **联系邮箱**：ncatbot@qq.com
2. **技术交流**：[ncatBot官方群组](https://qm.qq.com/q/B4zmXOlKik)
3. **娱乐交流**：[ncatBot娱乐群组](https://qm.qq.com/q/sxda3KUwqO)

## 快速开始

### 安装

```bash
pip install ncatbot
```

### 基础使用

```python
from ncatbot.core import BotClient, GroupMessage, PrivateMessage
from ncatbot.utils import ncatbot_config, get_log

_log = get_log()

# 配置机器人参数
ncatbot_config.set_bot_uin("123456")  # 设置 bot qq 号 (必填)
ncatbot_config.set_root("123456")  # 设置 bot 超级管理员账号 (建议填写)
ncatbot_config.set_ws_uri("ws://localhost:3001")  # 设置 napcat websocket server 地址
ncatbot_config.set_ws_token("napcat_ws")  # 设置 token (websocket 的 token)
ncatbot_config.set_webui_uri("http://localhost:6099")  # 设置 napcat webui 地址
ncatbot_config.set_webui_token("napcat_webui")  # 设置 token (webui 的 token)

bot = BotClient()

@bot.on_group_message()
async def on_group_message(msg: GroupMessage):
    _log.info(msg)
    if msg.raw_message == "测试":
        await msg.reply(text="NcatBot 测试成功喵~")

@bot.on_private_message()
def on_private_message(msg: PrivateMessage):
    _log.info(msg)
    if msg.raw_message == "测试":
        bot.api.post_private_msg_sync(msg.user_id, text="NcatBot 测试成功喵~")

if __name__ == "__main__":
    bot.run()
```

## 如何使用

- 认真阅读本项目[文档](https://docs.ncatbot.xyz)
- 使用 Docker [部署](https://github.com/ncatbot/NcatBot-Docker)

## 获取帮助

遇到任何困难时，请先按照以下顺序尝试解决：

1. **仔细阅读**[文档](https://docs.ncatbot.xyz)
2. 询问 [Gemini](https://gemini.google.com/), [Kimi](https://kimi.ai) 等人工智能
3. 搜索本项目的 [Issue 列表](https://github.com/liyihao1110/ncatbot/issues)

如果以上方法都无法解决你的问题，那么：
1. 在 [Issue 列表](https://github.com/liyihao1110/ncatbot/issues) 发 Issue 求助
2. 加入我们的官方QQ群提问

## 使用限制

1. **严禁将本项目以任何形式用于传播淫秽、反动或暴力等信息。**
2. **未经授权，禁止将本项目以任何形式用于盈利。**

## 致谢

感谢 [NapCat](https://github.com/NapNeko/NapCatQQ) 提供底层接口 | [IppClub](https://github.com/IppClub) 的宣传支持 | [Fcatbot](https://github.com/Fish-LP/Fcatbot) 提供代码和灵感

感谢 [林枫云](https://www.dkdun.cn/) 提供服务器支持

## 参与贡献

如果在你使用过程中遇到问题，或有任何建议，欢迎在 [GitHub Issues](https://github.com/liyihao1110/ncatbot/issues) 中反馈。欢迎给本 Repo 贡献代码！请先阅读 [贡献指南](CONTRIBUTING.md)。感谢你的支持！

---

<a href="https://github.com/liyihao1110/ncatbot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=liyihao1110/ncatbot" />
</a>
