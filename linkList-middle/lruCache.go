/**
146. LRU 缓存机制
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：

LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。


进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？



示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4


提示：

1 <= capacity <= 3000
0 <= key <= 3000
0 <= value <= 104
最多调用 3 * 104 次 get 和 put
**/
package main

import "fmt"

// 用一个双向链表来维护当前的数据，越靠后表示越后访问
type LinkNode struct {
	Next *LinkNode
	Prev *LinkNode
	Val  int
}

type LRUCache struct {
	Values map[int]int
	// 存储key对应的当前node节点，这个数据结构是为了使用O(1)的时间获取到要调整lru优先级的节点
	Nodes map[int]*LinkNode
	// start指向最先被淘汰的节点
	start    *LinkNode
	end      *LinkNode
	capacity int
	// 当前节点容量
	curCap int
}

func Constructor(capacity int) LRUCache {
	v1 := LRUCache{make(map[int]int), make(map[int]*LinkNode), nil, nil, capacity, 1}
	start := LinkNode{nil, nil, 0}
	v1.start = &start
	v1.end = &start
	return v1
}

func (this *LRUCache) Get(key int) int {
	elem, ok := this.Values[key]
	if ok {
		// O(1)的时间获取到被访问的节点
		node := this.Nodes[key]
		// 把被访问的节点调整到链表的最后，本来就是最后一个访问的节点就不处理
		if node.Next != nil {
			// 把当前节点的上一个节点和下一个节点连接起来
			node.Prev.Next, node.Next.Prev = node.Next, node.Prev
			if this.start == node {
				this.start = node.Next
			}
			// 处理尾节点
			this.end.Next, node.Prev = node, this.end
			node.Next = nil
			this.end = node
		}

		return elem
	} else {
		return -1
	}
}

func (this *LRUCache) Put(key int, value int) {
	_, ok := this.Values[key]
	this.Values[key] = value
	node := &LinkNode{nil, nil, key}

	// 如果当前key已经在链表中，不需要增加当前容量，且以被访问的方式处理之
	if ok {
		node = this.Nodes[key]
		if this.end == node {
			return
		}
		node.Prev.Next, node.Next.Prev = node.Next, node.Prev
		if this.start == node {
			this.start = node.Next
		}
	} else {
		this.curCap += 1
	}
	this.Nodes[key] = node
	this.end.Next, node.Prev = node, this.end
	node.Next = nil
	this.end = node

	if this.curCap > this.capacity {
		delete(this.Values, this.start.Val)
		delete(this.Nodes, this.start.Val)
		this.start = this.start.Next
		this.curCap -= 1
	}
}

func main() {
	// obj := Constructor(2)
	// obj.Put(2, 1)
	// obj.Put(2, 2)
	// param_1 := obj.Get(1)
	// fmt.Println(param_1)

	// obj.Put(3, 3)
	// param_2 := obj.Get(2)
	// fmt.Println(param_2)

	// obj.Put(4, 4)
	// param_3 := obj.Get(1)
	// fmt.Println(param_3)
	// param_4 := obj.Get(3)
	// fmt.Println(param_4)
	// param_5 := obj.Get(4)
	// fmt.Println(param_5)

	obj := Constructor(2)
	obj.Put(2, 1)
	obj.Put(2, 2)

	param_1 := obj.Get(2)
	fmt.Println(param_1)

	obj.Put(1, 1)
	obj.Put(4, 1)

	param_2 := obj.Get(2)
	fmt.Println(param_2)
}
