var colors = ['red', 'blue', 'green']

colors.forEach(function (color) {
  console.log(color)
})

colors.forEach(color => {
  console.log(color)
})


const a = function(name) {
  return `hello ${name}`
}
console.log(a(ssafy))
function add(num1, num2) {
  return num1 + num2
}

console.log(add(2, 7))
const sub = function(num1, num2) { // 이와 같이 이름이 없는 함수를 익명함수라고 함
  return num1 - num2
}

console.log(sub(7, 2)) 

const b = function(n) {
  return `hi ${n}`
}
const c = `ssafy`
console.log(b(c))
console.log(b('ssafy dj '))

const d = arrow => `hello ${arrow}`

console.log(d('woo'))

const test = (param1, param2) => param1 + param2


console.log(test(4, 4))