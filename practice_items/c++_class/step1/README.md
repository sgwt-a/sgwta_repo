C++のクラスの勉強
1. Step1
- クラスの定義
- インスタンスの生成
- クラスのpublic/privateメンバ変数のアクセス方法の違いの理解
  - public: {インスタンス名}.{public変数名}
  - private: クラスのメソッド等でアクセスするような処理を実装しないとアクセスできない
- クラスのpublic/privateメンバ変数、外部変数を用いたメソッドの実装
  - public/privateメンバ変数はメソッドの引数に与えなくてよい
  メンバ変数はクラス（インスタンス）内ではGlobal扱い？
  - 外部変数は引数で与える必要がある。
参考文献
- 例題：https://qiita.com/Yuya-Shimizu/items/45d42fe2942a684fa96
- メンバ変数のアクセスについて：http://www.s-cradle.com/developer/sophiaframework/tutorial/Cpp/access.html