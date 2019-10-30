// 1. 선언식 (statement, declaration)
// 함수 선언식은 코드가 실행되기 전에 로드 된다. 
function add(num1, num2) {
  return num1 + num2
}

console.log(add(2, 7))

// 2.표현식 (expression)
// 함수 표현식은 인터프리터가 해당코드에 도달 했을 때 로드된다. 
const sub = function(num1, num2) {
  return num1 - num2
}
console.log(sub(7,2))

console.log(typeof add)
console.log(typeof sub)

// Arrow Function 화살표 함수.
// 화살표 함수의 경우 일발 function 키워드로 정의한 함수와 100% 동일한 것이 아니다. 
// 화살표 함수는 항상 익명.
// 변수에 할당할 수 있지만, 이름 붙은 함수(생성자)로는 만들 수 없다.

const ssafy1 = function(name) {
  return `hello ${name}`
}

// 리팩토링 (refactoring)  인자 => 표현식
// 1. function 키워드 삭제
const ssafy1 = (name) => {return `hello ${name}`}

// 2. 인자의 '()' 소괄호 생략 (함수 매개변수가 하나일 경우만 생략 가능)
const ssafy1 = name => {return `hello ${name}`}

// 3. {} && return 생략 (단, 함수의 바디에 표현식이 1개일 경우만)
const ssafy1 = name => `hello, ${name}`

// Arrow function refactoring
let square = function(num) {
  return num ** 2
}

let square = (num) => {return num ** 2}

let square = num => {return num ** 2}

let square = num => num ** 2

// 매개변수가 없다면?? () 나 _ 를 사용 
let noArgs = () => 'No args'
let noArgs = _ => 'No args'

// object를 return 한다면
let returnObject = () => {return {key:'value'} } // return 을 명시적으로 적어준다. 

console.log(returnObject())  //{ key: 'value' }

// object를 return 하느데 return  을 사용하지 않을 경우
let returnObject = () => ({key:'value'}) //{ key: 'value' }

// object return 시 문제 사항
// 1. return 이 없는데 ()를 안쓴경우
let returnObject = () => {key:'value'}
const test = returnObject()
console.log(typeof test) //undefined

// 기본 매개변수를 줄 때는 매개변수의 개수와 상관없이 무조건 ()를 해야한다. 
const sayHello = (name = 'noName') => `hi ${name}`

// Anonymous Function (익명함수, 1회용 함수)
// 1. 기명함수로 만들기(변수/ 상수에 할당하기) - 생성과 동시에 함수의 인수로 할당.
const cube = function (num) {return num ** 3} // 변수 할당
const squareRoot = num => num ** 0.5
console.log(cube(2)) //8 
console.log(squareRoot(4)) //2

// 2. 익명함수 즉시 실행
console.log((function (num) {return num ** 3})(2)) // 8
console.log((num => num ** 0.5)(4)) //2

// 함수 호이스팅
ssafy()
function ssafy() {
  console.log('hoisting!')
}
// 변수에 할당한 함수(표현식)는 호이스팅 되지 않는다.
// 이것은 변수의 유효범위 규칙을 따르기 때문이다. 

// let의 경우
ssafy2()
let ssafy2 = function () {
  console.log('hoisting~!!')
}

// let (JS 가 이해한 경우)
let ssafy2 // 변수 선언

ssafy2() // 함수 호출 ssafy2는 초기화도 안됐는데 함수를 호출 ??? (reference error)
ssafy2 = function () { 
  console.log('hoisting')
}  // 변수에 함수 할당

//var  
ssafy3()  //TypeError: ssafy3 is not a function
var ssafy3 = function () {
  console.log('hoisting~')
}

//var (JS 가 이해한 경우)
var ssafy3 // 1. 변수 선언(+초기화)
ssafy3() //2. 함수 호출 -> ssafy3은 변수인데 호출을 한다고 (type error))
ssafy3 = function () {
  console.log('hoisting!~')
} //3. 변수에 함수 할당.