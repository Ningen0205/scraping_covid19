from models import db, Person

# モデルからテーブルを作成する(インポートされているモデルすべてが対象)
db.create_all()

# モデルで定義したデータクラスのインスタンスを作成する。
man1 = Person('Taro', 18)
man2 = Person('Jiro', 18)
man3 = Person('Saburo', 18)

# 作成したテーブルにを追加する(add:追加　add_all：リスト形式の一括追加)
db.session.add_all([man1, man2])
db.session.add(man3)

# テーブルへの変更をcommitで確定する。
db.session.commit()
print(man1, man2, man3)