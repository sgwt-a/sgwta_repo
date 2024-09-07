# 概要

## 実施事項

### Step1: c++, bazelを用いた足し算プログラムの作成
- 実行コマンド：`bazel run //cpp_bazel_gtest.proj:add_num`

### Step2: gtestの導入
- 実行コマンド：`bazel test //cpp_bazel_gtest.proj/test:test --test_output=all`
- 参考：ChatGPT
- 導入手順
    1. ステップ1: gtest を Bazel ワークスペースに追加  
        まず、gtest の依存関係を WORKSPACE ファイルに記述して、プロジェクトに組み込みます。  
        gtest のソースコードを直接取得して使うために、http_archive を使用してリポジトリを取得します。WORKSPACE ファイルに以下の内容を追加します。  

        ```python
        # WORKSPACE

        load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

        # Google Testのリポジトリを取得
        http_archive(
            name = "gtest",
            urls = ["https://github.com/google/googletest/archive/release-1.12.1.tar.gz"],
            strip_prefix = "googletest-release-1.12.1",
        )
        ```

    1. ステップ2: BUILD ファイルの設定  
        次に、テスト用の BUILD ファイルを作成して、gtest を使ってテストをビルド・実行するように設定します。
        例えば、tests ディレクトリ内にテストを格納する場合、その中に BUILD ファイルを作成します。
        ```css
        ├── src/
        │   └── main.cc
        ├── tests/
        │   ├── my_test.cc
        │   └── BUILD
        ├── WORKSPACE
        └── BUILD
        ```
     1. BUILD ファイルに gtest を使用する設定を追加  
        tests/BUILD ファイルに、cc_test ターゲットを追加して、gtest を使用してテストをビルドするように設定します。
        ```python
        # tests/BUILD

        cc_test(
            name = "my_test",  # テストの名前
            srcs = ["my_test.cc"],  # テストのソースコード
            deps = [
                "@gtest//:gtest",  # gtestの依存関係を指定
                "@gtest//:gtest_main",  # gtestのmain関数を使用
            ],
        )
        ```
  1. ステップ3: テストコードの作成  
        次に、my_test.cc ファイルに Google Test を使ったテストコードを書きます。  
        以下のようなシンプルな Google Test のテストケースを書きます。  
        ```cpp
        // my_test.cc

        #include <gtest/gtest.h>

        // テスト対象のコード（例として、加算関数）
        int add(int a, int b) {
            return a + b;
        }

        // テストケース
        TEST(AdditionTest, PositiveNumbers) {
            EXPECT_EQ(add(1, 2), 3);
        }

        TEST(AdditionTest, NegativeNumbers) {
            EXPECT_EQ(add(-1, -1), -2);
        }

        ```

  1. ステップ4: テストの実行  
        Bazel で gtest を使用してテストを実行するには、次のコマンドを使います。
        ```bash
        bazel test //tests:my_test
        ```
        bazel test コマンドは、指定されたターゲットのビルドとテストを実行します。  
        ここでは、//tests:my_test が tests/BUILD ファイルに定義した cc_test ターゲットを指定しています。  
        実行結果として、テストがビルドされ、gtest のテストが走り、結果が表示されます。

  1. ステップ5: オプションのカスタマイズ
        1. テストの並列実行
        Bazel は並列でテストを実行できるため、大規模なテストスイートの場合は次のようにしてテストを並列に実行することができます。

            ```bash
            bazel test //tests:my_test --jobs=4  # 4つのジョブで並列実行
            ```
        1. テストのフィルタリング
        特定のテストのみを実行するには、--test_filter を使ってテスト名をフィルタリングします。

            ```bash
            bazel test //tests:my_test --test_filter=AdditionTest.PositiveNumbers
            ```
            これにより、AdditionTest.PositiveNumbers のみが実行されます。
