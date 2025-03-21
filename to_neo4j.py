# HanChen UCAS
# 2025.3.20
# utf-8

import pandas as pd
from py2neo import Graph, Node, Relationship

# 使用前请确保在命令行运行 Neo4j 数据库服务（neo4j console）
# 清空数据库：MATCH (n) DETACH DELETE n

# 数据库连接配置（请根据实际情况修改）
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "your_password_here"

# 连接 Neo4j 数据库
graph = Graph(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

# CSV 数据文件路径（请替换为你的数据文件路径）
CSV_FILE_PATH = 'to_neo4j.py'

# 读取 CSV 文件并预处理数据
def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)

    # 格式化实体中的日期字段
    def format_date(value):
        try:
            return pd.to_datetime(value).strftime('%Y-%m-%d')
        except:
            return value

    df['头部实体'] = df['头部实体'].apply(format_date)
    df['尾部实体'] = df['尾部实体'].apply(format_date)

    return df.astype(str)


# 构建知识图谱
def build_knowledge_graph(df, graph_db):
    for _, row in df.iterrows():
        head_label, head_name = row['头部实体类型'], row['头部实体']
        tail_label, tail_name = row['尾部实体类型'], row['尾部实体']
        relation_type = row['关系']

        # 创建或合并头实体节点
        head_node = Node(head_label, name=head_name)
        graph_db.merge(head_node, head_label, "name")

        # 创建或合并尾实体节点
        tail_node = Node(tail_label, name=tail_name)
        graph_db.merge(tail_node, tail_label, "name")

        # 创建或合并关系
        relation = Relationship(head_node, relation_type, tail_node)
        graph_db.merge(relation)


if __name__ == '__main__':
    data_df = load_and_preprocess_data(CSV_FILE_PATH)
    build_knowledge_graph(data_df, graph)
    print("知识图谱构建完成，数据已导入 Neo4j！")