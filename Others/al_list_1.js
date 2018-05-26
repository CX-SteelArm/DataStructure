// 算法1.1 
// 合并a, b两个表
function union(a, b){
	var la_len = ListLength(a),
		lb_len = ListLength(b);
	for(var i=0; i<lb_len; i++){
		var t = GetElem(b, i);
		if(LocateElem(a, t) < 0){
			ListInsert(a, a.cur, t);
		}
	}
}

var list_a = List(10),
	list_b = List(10);
InitList(list_a, [1,2,3,5,8]);
InitList(list_b, [2,4,6,10]);
console.log(list_a, list_b);

union(list_a, list_b);
console.log(list_a, list_b);

// 算法1.2 
// 如果a, b均为以从小到大排好序的表，合并这两个表
// 采用归并法：i, j分别指向a, b两个表，c = min{a, b}，i, j随时移动
function merge(a, b){
	var la_len = ListLength(a),
		lb_len = ListLength(b);
	var c = List(10);
	InitList(c);

	var i = 0, j = 0;
	while(i<la_len && j<lb_len){
		if(GetElem(a, i) >= GetElem(b, j)){
			ListInsert(c, c.cur, b[j++]);
		}
		else{
			ListInsert(c, c.cur, a[i++]);
		}
	}

	while(i < la_len){
		ListInsert(c, c.cur, GetElem(a, i++, a[i]));
	}
	while(j < lb_len){
		ListInsert(c, c.cur, GetElem(b, j++, b[j]));
	}
	return c;
}

InitList(list_a, [1,2,3,5,8]);

console.log(merge(list_a, list_b));