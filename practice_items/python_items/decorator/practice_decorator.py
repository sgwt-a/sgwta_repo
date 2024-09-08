class Circle:
    def __init__(self, radius):
        print("run __init__()")
        print(f"  self = {self}")
        self._radius = radius

    """ @property
    メソッド（関数）ではなくプロパティ（属性）として扱うように変更。
    c.radius で値を取得できるようになる。
    c.radius() と書いた場合、c.radiusは整数値のため下記エラーになる。
        TypeError: 'int' object is not callable
    """

    @property
    def radius(self):
        return self._radius

    """ @radius.setter
    c.radius = 10 という形でセットする値を与える。
    c.radius(10) と書いた場合、c.radiusは@propertyによって整数値として扱われるため下記エラーになる。
        TypeError: 'int' object is not callable
    """

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("半径は0以上でなければなりません")

    @radius.deleter
    def radius(self):
        del self._radius


c = Circle(5)  # インスタンス生成
print(c.radius)  # 出力: 5

c.radius = 10  # 半径を更新
print(c.radius)  # 出力: 10

# c.radius = -3    # エラー: ValueError（バリデーションにより）

del c.radius  # _radius 属性が削除される
print(c.radius)  # AttributeError: 'Circle' object has no attribute '_radius'
