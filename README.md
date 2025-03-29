# 政府招商引资知识图谱（Investment Promotion Knowledge Graph）

本项目用于构建政府招商引资领域知识图谱，数据由大语言模型抽取而来，政策文件下载自北大法宝平台。

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
![image](https://github.com/user-attachments/assets/1deba891-a521-41fa-b076-fbf9d9f2d5c5)


