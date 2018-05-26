// Max sum of the subcolumns
// Algorithm 1 ~ O(N^3)
function al1(list){
	var i, j, k,
		sum, maxSum = 0,
		len = list.length;

	for(i=0; i<len; i++){
		for(j=i; j<len; j++){
			sum = 0;
			for(k=j; k<len; k++){
				sum += list[k];
				if(sum > maxSum){
					maxSum = sum;
				}
			}
		}
	}
	return maxSum;
}

// Algorithm 2 ~ O(N^2)
function al2(list){
	var i, j,
		sum, maxSum = 0,
		len = list.length;

	for(i=0; i<len; i++){
		sum = 0;
		for(j=i; j<len; j++){
			sum += list[j];
			if(sum > maxSum){
				maxSum = sum;
			}
		}
	}
	return maxSum
}

// Algorithm 3 ~ O(Nlg(N))
function al3(list, left, right){
	var i, j,
	sum, maxSum = 0,
	len = list.length,
	int = Math.floor;

	if(left == undefined){
		left = 0;
	}

	if(right == undefined){
		right = len-1;
	}

	var center = int((left + right)/2);
	if(center == left){
		return 0;
	}

	var maxleft = al3(list, left, center),
		maxright = al3(list, center+1, right);

	var leftBorderSum = 0, maxLeftSum = 0;
	for(i=center; i>=left; i--){
		leftBorderSum += list[i];
		if(leftBorderSum > maxLeftSum){
			maxLeftSum = leftBorderSum;
		}
	}

	var rightBorderSum = 0, maxRightSum = 0;
	for(i=center+1; i<=right; i++){
		rightBorderSum += list[i];
		if(rightBorderSum > maxRightSum){
			maxRightSum = rightBorderSum;
		}
	}

	return Math.max(maxleft, maxright, maxLeftSum + maxRightSum);
}

// Algorithm 4 ~ O(N)
function al4(list){
	var i,
		sum = 0, maxSum = 0,
		len = list.length;

	for(i=0; i<len; i++){
		sum += list[i];
		if(sum < 0){
			sum = 0;
		}
		if(sum > maxSum){
			maxSum = sum;
		}
	}
	return maxSum;
}

list = [-6, 5, -3, 6, 9, -8, 1, 20, -10, 15];

console.log(al1(list));
console.log(al2(list));
console.log(al3(list));
console.log(al4(list));

