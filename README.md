# Python Study — Roadmap tự học từ Python Core đến Algorithms & DSA

> **Cách dùng repo:** mở file này trước. Học từ `00` đến `12`. Mỗi phase (giai đoạn) chỉ chuyển tiếp khi đã làm được checklist. Các file lấy từ TheAlgorithms/Python dùng làm **reference implementation (mã cài đặt tham khảo)**; đừng học bằng cách chép lại nguyên xi.

## Nguyên tắc học

1. **Đọc mục tiêu trong README.**
2. Chạy các file ví dụ ngắn để hiểu cú pháp/API.
3. Đọc 1–2 reference implementation (mã cài đặt tham khảo).
4. Đóng file tham khảo và **tự code lại** trong `my_solutions/`.
5. Tự test bằng nhiều input, đặc biệt edge case (trường hợp biên).
6. Chỉ tick hoàn thành khi có thể giải thích complexity (độ phức tạp) và tự viết lại.

---

## 00 — Python Basics

**Mục tiêu:** đủ cú pháp để viết chương trình thuật toán mà không bị vướng Python.

Học theo thứ tự:

- [ ] `01_variables_types.py` — variable/type (biến/kiểu dữ liệu)
- [ ] `02_input_output.py` — input/output (nhập/xuất)
- [ ] `03_conditionals.py` — condition (rẽ nhánh)
- [ ] `04_loops.py` — loop (vòng lặp)
- [ ] `05_functions.py` — function (hàm)
- [ ] `06_exceptions.py` — exception (ngoại lệ), chỉ cần mức cơ bản

**Tự code:** tổng 1..n, kiểm tra số nguyên tố, GCD, Fibonacci vòng lặp.

**Qua phase khi:** tự viết được chương trình đọc input, xử lý, chia hàm và in output.

---

## 01 — Collections

Collections = **các kiểu dữ liệu chứa nhiều phần tử**.

- [ ] `01_list.py` — list (danh sách/mảng động)
- [ ] `02_tuple.py` — tuple (bộ bất biến)
- [ ] `03_set.py` — set (tập hợp)
- [ ] `04_dict.py` — dictionary/hash map (bảng băm ánh xạ key → value)
- [ ] `05_string.py` — string (chuỗi)
- [ ] `06_copy_mutability.py` — mutable/immutable (thay đổi được/bất biến), shallow/deep copy (sao chép nông/sâu)

**Phải nắm:**

- `list.append`, `pop`, slicing
- membership `x in set`
- đếm tần suất bằng `dict`
- duyệt `dict.items()`
- thao tác string cơ bản

**Tự code:** frequency map, loại trùng, kiểm tra palindrome/anagram.

---

## 02 — Pythonic Tools

Pythonic = **cách viết tận dụng công cụ chuẩn của Python thay vì tự làm mọi thứ**.

- [ ] Comprehension (cú pháp tạo collection)
- [ ] `enumerate`, `zip`
- [ ] `sorted(..., key=...)`, `lambda`
- [ ] `collections.Counter`, `defaultdict`, `deque`
- [ ] `heapq` — priority queue/min-heap (hàng đợi ưu tiên/đống cực tiểu)
- [ ] `bisect` — binary search (tìm kiếm nhị phân) trên list đã sắp xếp
- [ ] `itertools` — tổ hợp/hoán vị/tích lũy

**Qua phase khi:** biết khi nào nên dùng built-in/standard library (hàm có sẵn/thư viện chuẩn) thay vì tự cài.

---

## 03 — Array & String Patterns

Đây là các pattern (mẫu kỹ thuật) xuất hiện rất thường xuyên trong bài thuật toán.

- [ ] Two pointers (hai con trỏ) — `01_two_pointers.py`
- [ ] Sliding window (cửa sổ trượt) — `02_sliding_window.py`
- [ ] Frequency counting (đếm tần suất) — `03_frequency_count.py`
- [ ] Prefix sum (tổng tiền tố) — `04_prefix_sum_reference.py`
- [ ] Merge intervals (gộp khoảng) — `05_merge_intervals.py`
- [ ] Rotate array (xoay mảng) — `06_rotate_array.py`
- [ ] Palindrome/Anagram — `07`, `08`
- [ ] Top-K frequency — `09_top_k_frequent_words.py`

**Tự code:** prefix sum 1D, two-sum trên mảng tăng, max-sum cửa sổ k, longest substring đơn giản.

---

## 04 — Sorting & Searching

### Sorting (sắp xếp)

Học kỹ:

- [ ] Bubble Sort — O(n²)
- [ ] Selection Sort — O(n²)
- [ ] Insertion Sort — O(n²)
- [ ] Merge Sort — O(n log n)
- [ ] Quick Sort — trung bình O(n log n)
- [ ] Heap Sort — O(n log n)

Biết ý tưởng:

- [ ] Counting Sort
- [ ] Radix Sort

### Searching (tìm kiếm)

- [ ] Linear Search — O(n)
- [ ] Binary Search — O(log n)
- [ ] Quick Select — chọn phần tử thứ k
- [ ] Exponential Search — tham khảo

**Quan trọng:** ngoài tự cài binary search, phải dùng được `bisect_left` / `bisect_right` trong code thi.

---

## 05 — Recursion & Backtracking

Recursion = **đệ quy**. Backtracking = **quay lui: thử lựa chọn, sai thì hoàn tác**.

Đi theo thứ tự:

- [ ] Permutations (hoán vị)
- [ ] Combinations (tổ hợp)
- [ ] Subsequences (dãy con theo thứ tự)
- [ ] Generate Parentheses
- [ ] Sum of Subsets
- [ ] N-Queens
- [ ] Word Search
- [ ] Sudoku — chỉ đọc sau cùng

**Qua phase khi:** tự mô tả được state (trạng thái), choice (lựa chọn), base case (điều kiện dừng), undo (hoàn tác).

---

## 06 — Data Structures

Data structure = **cấu trúc dữ liệu**.

### 06.1 Stack & Queue

- [ ] Stack (ngăn xếp)
- [ ] Queue (hàng đợi)
- [ ] Deque (hàng đợi hai đầu)
- [ ] Balanced Parentheses
- [ ] Next Greater Element
- [ ] Queue bằng 2 stack

Python thực tế: ưu tiên `list` cho stack và `collections.deque` cho queue/deque.

### 06.2 Linked List

- [ ] Singly Linked List (danh sách liên kết đơn)
- [ ] Doubly Linked List (liên kết đôi)
- [ ] Floyd cycle detection (phát hiện chu trình)
- [ ] Merge two sorted lists

### 06.3 Heap & Hash

- [ ] Min Heap
- [ ] Max Heap
- [ ] Hash Table / Hash Map

Python thực tế: `heapq`, `dict`, `set` thường quan trọng hơn tự cài.

### 06.4 Tree / Trie / DSU

- [ ] Binary Tree
- [ ] Binary Search Tree — BST (cây tìm kiếm nhị phân)
- [ ] Tree Traversal — preorder/inorder/postorder
- [ ] Trie (cây tiền tố)
- [ ] DSU / Union-Find (tập hợp rời nhau)

---

## 07 — Greedy & Divide and Conquer

### Greedy (tham lam)

- [ ] Activity Selection
- [ ] Fractional Knapsack
- [ ] Minimum Waiting Time
- [ ] Optimal Merge Pattern

Không phải bài nào cũng dùng greedy được. Cần giải thích được **greedy choice (lựa chọn tham lam)** tại sao đúng.

### Divide and Conquer (chia để trị)

- [ ] Inversion Count
- [ ] Maximum Subarray
- [ ] Fast Power
- [ ] Closest Pair of Points — đọc sau

---

## 08 — Dynamic Programming

Dynamic Programming / DP = **quy hoạch động**: lưu kết quả trạng thái con để tránh tính lại.

Học theo thứ tự:

- [ ] Fibonacci
- [ ] Climbing Stairs
- [ ] Max Non-Adjacent Sum
- [ ] 0/1 Knapsack
- [ ] Coin Change
- [ ] LCS — Longest Common Subsequence (dãy con chung dài nhất)
- [ ] LIS — Longest Increasing Subsequence (dãy con tăng dài nhất)
- [ ] Edit Distance (khoảng cách chỉnh sửa)
- [ ] Maximum Subarray
- [ ] Minimum Cost Path
- [ ] Subset Sum
- [ ] Rod Cutting
- [ ] Longest Palindromic Subsequence
- [ ] Matrix Chain Multiplication
- [ ] Word Break

Với mỗi bài phải trả lời được:

1. State (trạng thái) là gì?
2. Transition (công thức chuyển) là gì?
3. Base case (trạng thái cơ sở) là gì?
4. Thứ tự tính ra sao?
5. Time/space complexity (độ phức tạp thời gian/bộ nhớ)?

---

## 09 — Graph

Graph = **đồ thị**.

Thứ tự nên học:

- [ ] Adjacency List / Matrix (danh sách / ma trận kề)
- [ ] BFS — Breadth-First Search (duyệt theo chiều rộng)
- [ ] DFS — Depth-First Search (duyệt theo chiều sâu)
- [ ] Connected Components (thành phần liên thông)
- [ ] Cycle Detection (phát hiện chu trình)
- [ ] Topological Sort — Kahn (sắp xếp topo)
- [ ] Dijkstra — đường đi ngắn với trọng số không âm
- [ ] Bellman-Ford — hỗ trợ cạnh âm
- [ ] Floyd-Warshall — shortest path mọi cặp
- [ ] Kruskal — MST (cây khung nhỏ nhất)
- [ ] Prim — MST
- [ ] SCC — Strongly Connected Components (thành phần liên thông mạnh)

**Tự code lại tối thiểu:** BFS, DFS, topo, Dijkstra, Kruskal + DSU.

---

## 10 — Math & Bit Manipulation

### Math

- [ ] GCD / LCM
- [ ] Prime Check
- [ ] Sieve of Eratosthenes (sàng Eratosthenes)
- [ ] Binary Exponentiation (lũy thừa nhị phân)
- [ ] Modular Exponentiation (lũy thừa modulo)
- [ ] Prime Factorization (phân tích thừa số nguyên tố)
- [ ] Combinations (tổ hợp)

### Bit Manipulation

- [ ] Bit basics
- [ ] AND / OR / XOR
- [ ] Shift (dịch bit)
- [ ] Count set bits (đếm bit 1)
- [ ] Power of two
- [ ] Find unique number bằng XOR
- [ ] Missing number bằng XOR

---

## 11 — Advanced Reference

**Không cần học ngay.** Chỉ quay lại khi bài/lộ trình chính yêu cầu.

### String algorithms

KMP, Rabin-Karp, Z-function, Manacher.

### Data structures

AVL Tree, Red-Black Tree, Treap, Fenwick Tree, Segment Tree.

### Graph nâng cao

A*, bridge (cầu), articulation point (đỉnh khớp), Tarjan SCC, 0-1 BFS.

### Range queries

Sparse Table.

---

## 12 — Practice Bank

`project_euler/` chứa 20 bài đầu của Project Euler cùng **một reference solution (lời giải tham khảo)** cho mỗi bài.

Cách dùng:

1. Mở file và chỉ đọc docstring/problem statement (mô tả bài toán) nếu có.
2. Tự giải trong `my_solutions/`.
3. Sau đó mới xem solution tham khảo.

Đây là bài luyện thêm, **không phải phase bắt buộc trước khi học phần tiếp theo**.

---

# Checklist tổng

- [ ] 00 Python Basics
- [ ] 01 Collections
- [ ] 02 Pythonic Tools
- [ ] 03 Array & String Patterns
- [ ] 04 Sorting & Searching
- [ ] 05 Recursion & Backtracking
- [ ] 06 Data Structures
- [ ] 07 Greedy & Divide and Conquer
- [ ] 08 Dynamic Programming
- [ ] 09 Graph
- [ ] 10 Math & Bit Manipulation
- [ ] 11 Advanced Reference — học theo nhu cầu
- [ ] 12 Practice Bank — luyện xen kẽ

---

## Một lưu ý quan trọng

Repo này **không nhằm giữ mọi thuật toán của TheAlgorithms/Python**. Mục tiêu của nó là tạo một learning path (lộ trình học) rõ ràng. Những mảng như machine learning (học máy), computer vision (thị giác máy tính), blockchain, physics, audio processing, web programming... nên học bằng lộ trình riêng khi cần, thay vì trộn vào DSA.

## Nguồn

Một phần reference implementations được chọn lọc từ **TheAlgorithms/Python** và giữ theo giấy phép MIT trong `LICENSE.md`. Các file Python Core/Pythonic Patterns ngắn trong repo này được thêm riêng để lấp khoảng trống mà repository thuật toán gốc không nhằm dạy.
