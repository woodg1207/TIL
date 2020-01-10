const MY_FAV = 7

console.log('my favorite number is: ' + MY_FAV)
if (MY_FAV === 7 ) {
  // 블록 유효 범위로 지정된 MY_FAV 이라는 변수를 만드므로 괜찮다.
  // 즉, 전역이 아닌 범위 안이므로 이름 공간에서 충돌이 나지 않는다.
  // 여기서 CONST 는 새로운 블록 유효 범위 이므로 const MY_FAV = 20으로 해도 같이 출력된다.
  let MY_FAV = 20

  console.log('my favorite number is :' + MY_FAV)
}
console.log(MY_FAV)
console.log(a) // undefined
var a = 10
console.log(a)

var a // 선언 & 초기화
console.log(a)
a=10  // 할당
console.log(a)
console.log(b)
let b = 10
console.log(b)

console.log(c)
const c = 10
console.log(c)
