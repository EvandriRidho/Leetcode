🧠 LeetCode Journey

Repository ini berisi kumpulan solusi soal LeetCode yang saya kerjain sebagai bagian dari latihan algoritma & data structure.

🎯 Tujuan

- Melatih problem solving

- Mengasah kemampuan algoritma & struktur data

- Persiapan interview technical

📊 Progress
| Difficulty | Solved |
| ---------- | ------ |
| Easy | 0 |
| Medium | 0 |
| Hard | 0 |
| **Total** | 0 |

📝 Format Penjelasan Soal

Setiap folder soal biasanya berisi:

- 💡 Problem link

- 🧠 Approach

- ⏱️ Time Complexity

- 📦 Space Complexity

- 💻 Code Implementation

Contoh template untuk tiap soal:

# Two Sum

## 🔗 Link

https://leetcode.com/problems/two-sum/

## 🧠 Approach

Gunakan hashmap untuk menyimpan value dan index...

## ⏱️ Complexity

- Time: O(n)
- Space: O(n)

## 💻 Code

```js
var twoSum = function (nums, target) {
  const map = {};

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];

    if (map[complement] !== undefined) {
      return [map[complement], i];
    }

    map[nums[i]] = i;
  }
};
```
