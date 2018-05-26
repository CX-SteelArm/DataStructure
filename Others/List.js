// 线性表的顺序存储结构
const ERROR = 1;
const NOTFOUND = -1;

function List(maxlen){
	if(maxlen <= 1){
		console.log("ERROR: Max length can not be less than 2.");
		return ERROR;
	}

	var l = Array(maxlen);
	l.maxlen = maxlen;
	l.cur = 0;
	l.len = 0;
	return l;
}

var InitList = function(l, k){
	ClearList(l);
	if(k instanceof Array){
		for(var i=0; i<k.length; i++){
			ListInsert(l, i, k[i]);
		}
	}
}

var DestroyList = function(l){
	l = null;
}

var ClearList = function(l){
	for(var i=0; i<l.len; i++){
		delete(l[i]);
	}
	l.cur = 0;
	l.len = 0;
}

var ListEmpty = function(l){
	return l.cur == 0;
}

var ListLength = function(l){
	return l.len;
}

var GetElem = function(l, i){
	if(i<0 || i>=l.len){
		console.log("ERROR: Out of range.");
		return ERROR;
	}
	return l[i];
}

var LocateElem = function(l, e, compare){
	if(compare == null || typeof(compare) !== 'function'){
		compare = function(a, b){
			return a === b;
		}
	}
	
	try{
		for(var i=0; i<l.len; i++){
			if(compare(e, l[i])){
				return i;
			}
		}
		return NOTFOUND;
	}catch(ex){
		console.log("ERROR: Locate error..." + ex);
		return ERROR;
	}
	
}

var PriorElem = function(l, i){
	if(i >= l.len || i <= 0){
		console.log("ERROR: index out of range.");
		return ERROR;
	}
	return l[i-1];
}

var NextElem = function(l, i){
	if(i >= l.len-1 || i < 0){
		console.log("ERROR: index out of range.");
		return ERROR;
	}
	return l[i+1];
}

var ListInsert = function(l, i, e){
	if(l.cur >= l.maxlen){
		console.log("ERROR: List is full.");
		return ERROR;
	}
	if(i < 0 || i > l.cur){
		console.log("ERROR: Insert out of range.");
		return ERROR;
	}

	for(var j=l.cur; j>i; j--){
		l[j] = l[j-1];
	}
	l[i] = e;
	l.cur += 1;
	l.len += 1;
}

var ListDelete = function(l, i){
	if(ListEmpty(l)){
		console.log("ERROR: List is empty.");
		return ERROR;
	}
	if(i < 0 || i >= l.cur){
		console.log("ERROR: Delete out of range.");
		return ERROR;
	}

	for(var j=i; j<l.len-1; j++){
		l[j] = l[j+1];
	}
	var e = l[l.cur-1];
	delete l[l.cur-1];
	l.cur -= 1;
	l.len -= 1;
	return e;
}

var ListTraverse = function(l, visit){
	if(visit == null || typeof(visit) !== 'function'){
		return ;
	}
	try{
		for(var i=0; i<l.len; i++){
			visit(l[i]);
		}
	}catch(ex){
		console.log("ERROR: Traverse error..." + ex);
	}
}