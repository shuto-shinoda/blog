# ASOBIBA

## 遊び場の共有、紹介を目的としたブログアプリ
### ![6316e3cb8218de3505e0b3c3ffab19fc](https://user-images.githubusercontent.com/69189662/105320532-9dfd0d00-5c09-11eb-990b-5bad75afbde7.jpg)


## 概要
### 新しく発見した遊び場所やよく行く遊び場所の魅力などの共有やコミュニケーションを目的としたアプリです。

## App URL
### https://blog-sssssss.herokuapp.com/

# 機能一覧
#### ユーザー管理機能

<img width="465" alt="68a9a9b0ed61dc351f1ac4f057834e06" src="https://user-images.githubusercontent.com/69189662/106409952-20e15b80-6485-11eb-9347-1e957ba570a8.png">
<img width="420" alt="f18c8acc15fe8e7ce3821138d48565a2" src="https://user-images.githubusercontent.com/69189662/106409966-276fd300-6485-11eb-8abc-56946727665c.png">

ヘッターより、新規登録・ログイン・ログアウトが可能です。

*全項目入力必須
<img width="1428" alt="7776b6a781255bcf55f52099f40a2915" src="https://user-images.githubusercontent.com/69189662/106410172-95b49580-6485-11eb-9e5b-309c5305f15d.png">

#### 投稿機能
<img width="1432" alt="195a23247be8efe70daa6c7d35bd5e8f" src="https://user-images.githubusercontent.com/69189662/106408494-eb873e80-6481-11eb-8bc0-396491194df7.png">

ログインユーザーのみ投稿できる
(ログインしていないユーザーは閲覧しか出来ない仕様になっています。)

*タイトル、本文、カテゴリーの入力は必須です。

必須項目が空の場合投稿は出来ません。
(空の場合は「このフィールドを入力してください」と表示が出ます。)

<img width="581" alt="811c8e647d579202a06b09ee0c4a7eca" src="https://user-images.githubusercontent.com/69189662/106408940-cd6e0e00-6482-11eb-9592-60bb4e54a6bb.png">

・画像付きで記事投稿が可能(画像表示修正中）

#### 投稿詳細表示機能
各投稿詳細は投稿のタイトルをクリックで閲覧可能です。

#### 投稿編集・削除機能

<img width="1438" alt="6f917ba78bf013c5c263ea3f2c96555f" src="https://user-images.githubusercontent.com/69189662/106409004-ed9dcd00-6482-11eb-8edb-73adde5a08a5.png">

投稿者本人のみ投稿編集・削除が可能です。

#### ユーザー詳細表示機能

<img width="1436" alt="2576472f195fd54ceb45f4fb0d57adbe" src="https://user-images.githubusercontent.com/69189662/106410734-db259280-6486-11eb-9221-4daaf637e5f0.png">

各ユーザーの投稿一覧が閲覧可能

#### 検索機能

<img width="1437" alt="4b0ac972cff1a2588c50950593b5f237" src="https://user-images.githubusercontent.com/69189662/106411258-27250700-6488-11eb-8a62-fd5c6a26d64c.png">

・タイトル、ユーザー名

・日付

・タグ

での検索が可能です。

#### LIKE機能

<img width="506" alt="f3ba8a26c6ff7dd6a23db0d3b6fef514" src="https://user-images.githubusercontent.com/69189662/106411610-04dfb900-6489-11eb-8404-df3783cb8053.png">

各投稿へLIKEをつけることが可能,LIKE削除も可能

#### コメント機能

<img width="1440" alt="7fe0b1db3114d1839835b2308745782e" src="https://user-images.githubusercontent.com/69189662/106409237-7452aa00-6483-11eb-9781-de10e369b59d.png">

記事ページを開くと下部にコメント投稿欄が表示されます。

画面最下部からコメントの入力が可能です。

コメント投稿者のみがコメントの削除が可能です。
(ゴミ箱マーククリックでコメント削除)

## 追加予定機能
#### ・ google mapで位置情報表示機能追加予定
## ローカルでの動作方法

#### $ git clone https://github.com/shuto-shinoda/blog
#### $ cd blog
#### $ python3 manage.py makemigrations
#### $ python3 manage.py migrate
#### $ python3 manage.py runserver
#### 👉 http://localhost:8000

# 開発環境
#### VScode
#### Python 3.9.0
#### Django 3.1.3
#### mysql 5.6.50
#### heroku 7.47.7
