# ASOBIBA

## 遊び場の共有、紹介を目的としたブログアプリ
### https://gyazo.com/6316e3cb8218de3505e0b3c3ffab19fc

## 概要
### 新しく発見した遊び場所やよく行く遊び場所の魅力などの共有やコミュニケーションを目的としたアプリです。

## App URL
### https://blog-sssssss.herokuapp.com/

## 利用方法

## ・ユーザー管理機能
### https://gyazo.com/696aab8b13178aa5c378704621405930
### ・新規登録
### ・ログイン
### ・ログアウト

## ・投稿機能
### https://gyazo.com/ce0d84095b9a1341d365abf1eed1480e
### ・ログインユーザーのみ投稿できる
### ・タイトル、本文、カテゴリーの入力は必須である
### https://gyazo.com/95e86413faa330db08551e0c07eabfb6

### ・編集、削除機能
### https://gyazo.com/3752586334d59d5a48349771e038b5b7

## コメント機能
### https://gyazo.com/418ea402e3ffa21d7d334048d9a4875c
### ・記事ページを開くと下部にコメント投稿欄が表示される
### ・ゴミ箱マーククリックでコメント削除

## 開発環境

#### $ git clone https://github.com/shuto-shinoda/blog
#### $ cd blog
#### $ python3 manage.py makemigrations
#### $ python3 manage.py migrate
#### $ python3 manage.py runserver
#### 👉 http://localhost:8000