#include <gtest/gtest.h>

// cpp_bazel_gtest.proj/src/calc_add/calc_add.cppの関数を外部から参照するための宣言
int32_t CalcAdd(int32_t num1, int32_t num2);

// テストケース
TEST(AdditionTest, PositiveNumbers) {
    EXPECT_EQ(CalcAdd(1, 2), 3);
}

TEST(AdditionTest, NegativeNumbers) {
    EXPECT_EQ(CalcAdd(-1, -1), -2);
}
