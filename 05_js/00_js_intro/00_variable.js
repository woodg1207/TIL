// var  최대한 사용하지 않는다.
//let 변수
let x = 1
if (x === 1){
  let x = 2

  console.log(x)
}
console.log(x)

// const  (상수) 
//const 선언시 초기값을 생략하면 오류 발생
// const MY_FAV  
const MY_FAV = 7
console.log('my favorite number is ' + MY_FAV)
// MY_FAV = 20 // 에러 발생 : 재할당 불가.

// 상수를 재선언하려는 시도는 모두 오류 발생
// const MY_FAV = 20
// let MY_FAV = 20
// var MY_FAV = 20
//SyntaxError: Identifier 'MY_FAV' has already been declared

console.log('if test')
if (MY_FAV === 7) {
  // 블록 유효 범위로 지정된 MY_FAV 이라는 변수를 마드므로 괜찮다.
  // 즉, 전역이 아닌 범위안이므로 이름 공간에서 출동이 나지 않는다.
  let MY_FAV = 20
  console.log('my favorite number is ' + MY_FAV)
}
console.log( MY_FAV)


function varTest() {
  var x = 1
  if (true){
    var x = 2
    console.log(x) // 상위블록과 같은변수
  }
  console.log(x)
}
varTest()

// let 과 var
var a = 1
let b = 2
if (a === 1) {
  var a = 11
  let b = 22
  console.log(a) // 11
  console.log(b) // 22
}
console.log(a) // 11
console.log(b) // 2


////식별자 작성 스타일
// 1. 카멜 케이스(camelCase) - 객체, 변수, 함수 (=== lower-camel-case)
let dog
let variableName
// 배열은 복수
const dogs = []
// 정규 표현식은 'r'로 시작
const rDecs = /.*/
//함수
function getPropertyName() {
  return 1
}
// boolean을 반환하는 변수나 함수 'is'로 시작
let isAvailable = false

// 2. 파스칼 케이스(PascalCase) - 클래스, 생성자( === upper-camel-case)
class User {
  constructor(options) {
    this.name = option.name
  }
}

// 3. 대문자 스네이크 케이스 (SNAKE_CASE) -상수
// 이 표현은 변수와 변수의 속성이 변하지 않는다는 것을 프로그래머에게 알려준다.
const API_KEY = 'avsdfsadfl'

