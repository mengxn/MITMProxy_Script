# MITMProxy Script
MITMProxy 扩展脚本


## 依赖
- [`MITMProxy`](https://mitmproxy.org/) 开源的抓包软件
- Python


## 使用
1. 在命令行输入以下代码进行安装  
`curl https://raw.githubusercontent.com/mengxn/MITMProxy_Script/master/setup.sh -o setup.sh -s && sh setup.sh`
2. 启用代理软件时，使用`-s`指定脚本  
`mitmproxy -s ~/.mitmproxy/proxy.py`
3. (可选)也可以将脚本配置到`~/.mitmproxy/config.yaml`文件中，免去每次指定脚本的操作  
```
...
scripts: [~/.mitmproxy/proxy.py]
...
```

> :exclamation::exclamation::exclamation: 安装此脚本，会覆盖 `~/.mitmproxy/` 下 `proxy.py`、`keys.yaml` 文件


## 扩展快捷键
- **c** 拷贝请求curl到剪贴板
- **B** 拷贝response到剪贴板
- **s** 保持请求结果（response）到本地
- **S** 保持请求结果（response）到本地，并打开文件
- **P** 切换代理开关


## 扩展指令
- `:pop.proxy true/false` 打开或关闭代理
- `:pop.map_local <flow> <file>` 请求结果代理到本地文件


## 更多
更多功能可提issue
