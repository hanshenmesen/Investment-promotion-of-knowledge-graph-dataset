# 政府招商引资知识图谱（Investment Promotion Knowledge Graph）

本项目用于构建政府招商引资领域的知识图谱，便于进行信息检索、分析及辅助决策。

## 项目结构

项目文件夹/
├── triples_results.csv    # 知识图谱数据
└── to_neo4j.py    # Neo4j图谱导入脚本

## 数据说明

数据文件为三元组格式，字段包括：

- 头部实体
- 头部实体类型
- 关系
- 尾部实体
- 尾部实体类型

示例数据：

| 头部实体 | 头部实体类型 | 关系 | 尾部实体 | 尾部实体类型 |
|----------|------------|------|----------|--------------|
|《A政策》  | 政策文件    | 引用 |《B政策》  |  政策文件    |

## 环境配置

### Neo4j数据库

- Neo4j版本：5.x
- 默认端口：7687

安装后启动Neo4j服务，具体参考[Neo4j官方文档](https://neo4j.com/docs/operations-manual/current/installation/)。

安装依赖：

```bash
pip install pandas py2neo
```

## 使用方法

修改`to_neo4j.py`中的数据库连接信息和数据文件路径：

```python
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "your_password_here"

CSV_FILE_PATH = r''
```

导入完成后即可在Neo4j界面查看知识图谱。
