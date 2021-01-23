# ASOBIBA

## 遊び場の共有、紹介を目的としたブログアプリ
### ![6316e3cb8218de3505e0b3c3ffab19fc](https://user-images.githubusercontent.com/69189662/105320532-9dfd0d00-5c09-11eb-990b-5bad75afbde7.jpg)


## 概要
### 新しく発見した遊び場所やよく行く遊び場所の魅力などの共有やコミュニケーションを目的としたアプリです。

## App URL
### https://blog-sssssss.herokuapp.com/

## 利用方法

## ・ユーザー管理機能
### https://user-images.githubusercontent.com/69189662/105320166-30e97780-5c09-11eb-8e69-59ddc52653e6.mp4

### ・新規登録
### ・ログイン
### ・ログアウト

## ・投稿機能
### https://user-images.githubusercontent.com/69189662/105320791-f0d6c480-5c09-11eb-89c5-cd4151e29799.mp4


### ・ログインユーザーのみ投稿できる
### ・タイトル、本文、カテゴリーの入力は必須である
### https://user-images.githubusercontent.com/69189662/105320943-28457100-5c0a-11eb-9730-eb42dc38be49.mp4


### ・編集、削除機能
### https://user-images.githubusercontent.com/69189662/105321098-5cb92d00-5c0a-11eb-8005-dcf6f52d86c4.mp4



## コメント機能
### 
https://user-images.githubusercontent.com/69189662/105321205-840ffa00-5c0a-11eb-861f-8109cdd4d9fc.mp4

### ・記事ページを開くと下部にコメント投稿欄が表示される
### ・ゴミ箱マーククリックでコメント削除


## 機能一覧
#### ユーザー管理機能   | 新規登録・ログイン・ログアウトが可能                            |
#### 投稿機能          |画像付きで記事投稿が可能                                       |
#### 投稿詳細表示機能   |各投稿詳細が詳細ページで閲覧可能                                 |
#### 投稿編集・削除機能  | 投稿者本人のみ投稿編集・削除が可能                             |
#### ユーザー詳細表示機能|各ユーザーのプロフィール・投稿一覧が閲覧可能                      |
#### ユーザー情報編集機能|ログイン中のユーザーでアカウント本人であればプロフィール編集が可能    |
#### LIKE機能         |各投稿へLIKEをつけることが可能,LIKE削除も可能|
#### コメント機能       |投稿詳細ページからコメントが可能                      |

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
