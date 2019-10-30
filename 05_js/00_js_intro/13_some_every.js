// Array Helper Method

// 6. .some(callback())   : 하나라도!
// 배열 안에 어떤 요소라도 (===하나라도) 주어진 콜백함수를 통과하는지 테스트하고,
// 결과에 따라 boolean 을 return한다.
// 빈 배열은 false 를 return.
// 조건에 맞는 요소를 찾으면 즉시 검색을 멈추고 true 를 return
// 'or' 연산과 유사.

const arr = [1,2,3,4,5,]

const result = arr.some(elem => elem%2===0)
console.log(result) // true

// 7. .every(callback())  : 모든!
// 배열 안에 모든 요소가 주어진 콜백함수를 통과하는지 테스트하고, 
// 결과에 따라 boolean을 return
// 빈 배열은 무조건 true 를 return
// 배열의 모든 요소가 조건에 맞아야 true / 그렇지 않다면 false
// 조건에 맞지 않는 요소를 찾으면 검색을 멈추고 false를 return
// 'and' 연산과 유사.

const result2 = arr.every(elem => elem%2===0)
console.log(result2) // false

// 7-1 연습
// for
// ram이 16보다 작으면 everyComputers를 false로
// 아니면 someComputers를 true로.
var everyComputers = true
var someComputers = false
var computers = [
  {name: 'macbook', ram: 16},
  {name: 'gram', ram: 16},
  {name: 'series9', ram: 32},
]
for (let i = 0; i < computers.length; i++) {
  var computer = computers[i]
  if (computer.ram < 32) {
    everyComputers = false
  }else {
    someComputers = true
  }
}
console.log(everyComputers)
console.log(someComputers)


// some/ every

var COMPUTERS = [
  {name: 'macbook', ram: 8},
  {name: 'gram', ram: 16},
  {name: 'series9', ram: 32},
]
//some 
const newSomeComputers = COMPUTERS.some(computer => computer.ram<32)
console.log(newSomeComputers) //true

//every
const newEveryComputers = COMPUTERS.every(computer => computer.ram<32)
console.log(newEveryComputers) //false