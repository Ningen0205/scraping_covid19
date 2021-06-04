import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

base_dir = os.path.dirname(__file__)

app = Flask(__name__)

# sqliteのファイル保存先を指定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'

# モデルに変更があった場合にシグナル送出の有無を設定する
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# appに設定した内容でDBに接続する
db = SQLAlchemy(app)

# モデルクラスの定義にはdb.Modelクラスを継承する必要がある。
class Person(db.Model):
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    # テーブル名を設定(テーブル名はクラス名の複数形が一般的)
    __tablename__ = 'persons'

    # 作成するテーブルのカラムを定義
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)