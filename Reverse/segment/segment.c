#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct {
    int n;
    int tree[1];
} SegmentTree;

unsigned char pos[] = {
    20, 27,  4,  3, 18, 10, 13, 37, 15, 10, 13,  2, 26,  6, 13,  3, 14,
    29,  0, 23, 12, 16,  8, 18,  1,  3,  0, 11,  1,  5,  6,  4, 24,  0,
    3,  9, 25,  6,  3,  5,  6, 21, 24,  0, 44,
    40, 43, 32, 30, 24, 42, 25, 41, 17, 14, 20, 12, 34, 27, 29, 25, 17,
    31, 22, 32, 37, 37, 40, 37, 27,  6, 31, 33, 32, 21, 40, 18, 25, 21,
    43, 34, 38, 10, 42, 36,  6, 39, 35, 16, 255
};

short sum[] = {
    1470, 1350, 1959, 1903,  403, 2223,  704,  409,  149,  303,  401,
    1008,  614, 1433,  966, 1596,  201,  197, 1756,  614, 1666, 1466,
    2223, 1362, 1963,  440, 2314, 1363, 2271, 1130, 2401, 1097,   97,
    1657, 3044, 1616, 1061,  478, 2919, 2194,  123, 1373,  813, 1404, 0
};

void buildTree(SegmentTree *segTree, const char *arr, int node, int start, int end) {
    if (start == end) {
        segTree->tree[node] = arr[start];
    } else {
        int mid = (start + end) / 2;
        int leftChild = 2 * node + 1;
        int rightChild = 2 * node + 2;
        buildTree(segTree, arr, leftChild, start, mid);
        buildTree(segTree, arr, rightChild, mid + 1, end);
        segTree->tree[node] = segTree->tree[leftChild] + segTree->tree[rightChild];
    }
}

SegmentTree* createSegmentTree(const char *arr, int n) {
    SegmentTree* segTree = (SegmentTree*)malloc(sizeof(int) * (4 * n + 1));
    segTree->n = n;
    buildTree(segTree, arr, 0, 0, n - 1);
    return segTree;
}

int queryTree(SegmentTree* segTree, int L, int R, int node, int start, int end) {
    if (R < start || end < L) {
        return 0;
    }
    if (L <= start && end <= R) {
        return segTree->tree[node];
    }
    int mid = (start + end) / 2;
    int leftChild = 2 * node + 1;
    int rightChild = 2 * node + 2;
    int leftSum = queryTree(segTree, L, R, leftChild, start, mid);
    int rightSum = queryTree(segTree, L, R, rightChild, mid + 1, end);
    return leftSum + rightSum;
}

int querySegmentTree(SegmentTree *segTree, int L, int R) {
    return queryTree(segTree, L, R, 0, 0, segTree->n - 1);
}

void freeSegmentTree(SegmentTree* segTree) {
    free(segTree);
}

int main() {
    char buffer[1024];
    printf("Please input the flag: ");
    scanf("%99s", buffer);
    int n = strlen(buffer);

    SegmentTree* segTree = createSegmentTree(buffer, n);

    for (int i = 0; i < 45; i++) {
        if (querySegmentTree(segTree, pos[i], pos[i + 45]) != sum[i]) {
            printf("Wrong!\n");
            goto end;
        }
    }

    printf("Right!\n");

end:
    freeSegmentTree(segTree);
    return 0;
}


