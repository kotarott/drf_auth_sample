# drf_auth_sample
  
## Userモデルのカスタマイズ
以下の記事を参考に作成  
https://qiita.com/xKxAxKx/items/60e8fb93d6bbeebcf065  
  
⇒上手くいかなかった…  
  
次は以下のサイトを参考にやってみる  
https://hodalog.com/how-to-extend-django-user-model/  
  
profileなど別のテーブルを作成したうえで1対1のリレーションを作成するのが現実的?  
  
⇒RetrieveUpdateAPIViewを用いて作成。  
最低限のユーザー情報を登録することができる。  
  
## Session + Token認証  
djoserで一発  

