# KittenGen
这是一个基于 python3.8 中 flask 框架为自己打造的一个自动造数据机。
## 使用Docker部署

请先参照[``.env``文件](/KittenGen/.env)，配置好需要的参数。然后使用以下命令启动docker：

```
docker run -d -v $(pwd)/.env:/app/.env -p 2025:2025 introljl/datagen:latest
```
注意：在 Windows 终端下需要将配置文件路径 $(pwd) 替换为绝对路径。

启动后访问``127.0.0.1:2025``，输入设置好的密钥，即可进入页面。

## 更新内容
- 更改为docker部署方式。
- 添加外网访问选项。
- 添加登录验证页面，提高公网使用安全性。
- 使用.env文件来实现自定义参数。