// // const nothing = () => {
// //   console.log('sleeping')
// // }
// function sleep_3s() {
//   setTimeout( () => console.log('wakeup'), 3000)// 대표적인 비동기식 함수.
// }
// console.log('start')
// // setTimeout(nothing, 3000)
// sleep_3s()
// console.log('end')
/////////////////////////////////
// function first() {
//   console.log('first')
// }
// function second() {
//   console.log('second')
// }
// function third() {
//   console.log('third')
// }

// first()
// setTimeout(second, 1000)
// third()
///////////////////////////////////////

// console.log('hi')
// setTimeout(function ssafy() {
//   console.log('ssafy')
// }, 100) // 100ms 후에 콜백큐로 간다.

// console.log('bye')

///////////////////////////////////////

function printHello() {
  console.log('hello from baz')
}

function baz() {
  setTimeout(printHello,3000);
}

function bar() {
  baz()
}

function foo() {
  bar()
}

foo()