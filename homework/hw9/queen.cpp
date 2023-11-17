#include <iostream>
#include <vector>

using namespace std;

const int N = 8; // 棋盤大小
vector < vector<int> > board(N, vector<int>(N, 0)); // 棋盤

// 檢查皇后是否可以放在(row, col)位置
bool isSafe(int row, int col) {
    // 檢查同一列
    for (int i = 0; i < row; i++) {
        if (board[i][col] == 1) {
            return false;
        }
    }

    // 檢查左上對角線
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 1) {
            return false;
        }
    }

    // 檢查右上對角線
    for (int i = row, j = col; i >= 0 && j < N; i--, j++) {
        if (board[i][j] == 1) {
            return false;
        }
    }

    return true;
}

// 解決八皇后問題的遞歸函數
bool solveNQueens(int row) {
    if (row == N) {
        // 所有皇后都被成功放置，打印棋盤
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cout << board[i][j] << " ";
            }
            cout << endl;
        }
        return true;
    }

    for (int col = 0; col < N; col++) {
        if (isSafe(row, col)) {
            board[row][col] = 1;
            if (solveNQueens(row + 1)) {
                return true;
            }
            board[row][col] = 0; // 回溯
        }
    }
    return false;
}

int main() {
    if (solveNQueens(0)) {
        cout << "" << endl;
    } else {
        cout << "無法找到解。" << endl;
    }

    return 0;
}
