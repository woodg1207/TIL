const a = 13
const b = -3
const c = 3.14 //float
const d = 2.998e8 // 2.998*10^8
const e = Infinity
const f = -Infinity
const g = NaN
console.log(a,b,c,d,e,f,g)

// 문자열
const sentence1 = 'sentence'
const sentence2 = "sentence"
const sentence3 = `sentence` 
// backtick `

// const word = "안녕
//  하세요"
const word1 = `안녕 \n하세요.`
console.log(word1)
const word2 = `안녕 
하세요.`
console.log(word2)

// Template Literal
// JS 에서 문자열을 입력하는 방식 
const age = 10
const messaage = `홍길동은 ${age}
세입니다. `
console.log(messaage)

const happy = 'hello'
const hacking = 'world' + 'lol'
console.log(happy+hacking)

// Empty Value

// Number.isNaN() 이 함수는 값이 NaN인지 여부를 판단.
// 
Number.isNaN(1+null) // false --> 숫자
Number.isNaN(1+undefined) // true --> 숫자 X