# 服务外包后端

## 项目结构

```
outsourcing/
├── app/                      # 应用的核心代码目录
│   ├── __init__.py           # 初始化 Flask 应用
│   ├── models/               # 数据库模型(ORM 模型)
│   ├── routes/               # 路由
│   ├── services/             # 业务逻辑层
│   ├── utils/                # 工具函数或辅助类
│   ├── templates/            # HTML模板文件
│   └── static/               # 静态文件
├── config/                   # 配置文件目录
├── test/                     # 测试文件目录
├── requirements.txt          # Python 依赖包列表
├── run.py                    # 启动 Flask 应用的入口文件
└── README.md                 # 项目说明文档
```