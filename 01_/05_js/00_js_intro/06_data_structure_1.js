const numbers = [1, 2, 3, 4,]

console.log(numbers[0]) //1
console.log(numbers[-1]) // undefined : 정확한 양의 정수 index만 가능.
console.log(numbers.length) //4


console.log(numbers.reverse())// 원본 파괴
console.log(numbers.reverse())

// push : 배열의 길이를 return, 뒤의 요소에 추가
console.log(numbers.push('a')) // 5
console.log(numbers)

// pop : 배열의 가장 마지막 요소 제거후 return
console.log(numbers.pop())
console.log(numbers)

// unshift : 배열의 길이를 return, 앞의 요소에 추가
console.log(numbers.unshift('a')) // 5
console.log(numbers)

// shift : 배열의 앞의 요소 제거후 return
console.log(numbers.shift())
console.log(numbers)

// includes : 배열에 요소가 있는지 boolean return
console.log(numbers.includes(1))

console.log(numbers.push('a','a'))
console.log(numbers)
console.log(numbers.indexOf('a')) // 4 : a가 존재하는 첫 index return

console.log(numbers.indexOf('b')) // -1 : 찾고자 하는 요소가 없으며 -1 return

// join - 배열의 요소를 join 함수의 인자를 기준으로 이어서 문자열로 return
console.log(numbers.join()) // '1,2,3,4,a,a' 문자열로 만들어준다.
// ()안에 아무것도 넣지 않으면 ,를 기준으로)
console.log(numbers.join(''))//1234aa
console.log(numbers.join('-'))//1-2-3-4-a-a
console.log(numbers)  /// 원본은 변화 시키지 않는다. 

