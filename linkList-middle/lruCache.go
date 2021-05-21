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
