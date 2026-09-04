
http://host.docker.internal:9000/search


# Cloud run configure
Secret Volume configure
| 字段 |	值 |
| ---- | ---- |
| 挂载路径（父目录）|/etc/searxng|
| 挂载后的文件名 | 在 Cloud Run 挂载配置里，有一个 Path 字段，填 `settings.yml`|

最终生成的路径就是 /etc/searxng/settings.yml ✅
