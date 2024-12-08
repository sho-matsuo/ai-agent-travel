import streamlit as st
import mysql.connector

args = st.text_input("作成したいアプリケーションについて記載してください")

#データベース接続
config = {
'user': 'aiagent-admin',         # MySQLユーザー名
'password': 'A!agent01',     # MySQLパスワード
'host': 'sql-server-aiagents.database.windows.net',             # ホスト名（例: 'localhost'）
'database': 'db_aiagents' # データベース名
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()

# INSERT文の準備
insert_query = "INSERT INTO input (input_data) VALUES (%s)"
data_to_insert = (args,)  # 挿入するデータ（タプル形式）

# クエリの実行
cursor.execute(insert_query, data_to_insert)

# トランザクションをコミット
connection.commit()

st.text("データが正常に挿入されました！")