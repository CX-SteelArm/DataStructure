### ADT List
--------------------------
	ADT List{
		数据对象：D = {ai | ai, i = 1,2,...,n, n>=0}
		数据关系：R1 = {<ai-1, ai> | ai-1, ai, i = 2,...,n}
		基本操作：
		InitList(&L),
		DestroyList(&L),
		ClearList(&L),
		ListEmpty(L),
		ListLength(L),
		GetElem(L, i, &e),
		LocataElem(L, e, compare()),//compare()是比较函数，用于筛选值
		PriorElem(L, cur_e, *pre_e),
		NextElem(L, cur_e, *next_e),
		ListInsert(&L, i, e),
		ListDelete(&L, i, &e),//删除的元素存在e中
		ListTraverse(L, visit()),//遍历数组元素
	}ADT List

--------------------------
	使用JS实现链表：建立两个类Node和LList，前者保存元素，后者新建链表
	有head头结点属性，
	有以下方法：
	* init() 
	* clear() 
	* empty()
	* length()
	* find(index) 找到index位置
	* insert(index, element) 插入某个元素
	* delete(index) 删除某个元素
	* next(index) 返回后一个
	* previous(index) 返回前一个
--------------------------

