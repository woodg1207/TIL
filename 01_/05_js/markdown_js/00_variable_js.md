# 00_variable_js

### 1.변수 & 식별자

- 어디에 쓸지 결정하는 건 프로그래머의 몫
- `PI`, `DAYS_IN_JUNE`과 같은 경우는 상수가 적절
- `WEATHER_TEMP` 처럼 모호한 경우(각자가 생각하는 좋아하는 기온이 다를 수있으니까)이런경우는 변수가 적절 

**최근** **JavaScript문서에서는**

- 일단 모든 선언에서 가능한한 상수를 사용한다.
- 먼저 상수를 생각하고 값이 바뀌는 것이 더 자유로운 상황이라면, 그때 변수로 바꿔서 사요하는 것을 권장.

**간단** **정리**

- var :  할당 및 선언 자유/ 함수 스코프
- let : 할당 자유 /선언은 한번만/ 블록 스코프
- const : 할당및 선언은 한번만/ 블록 스코프

##### let(변수)

- 값을 재할당 할 수 이는 변수를 선언
- 단 각 변수는 한번만 선언할 수 있다.
- 블록 유효 범위(block scope) - 지역변수로만 선언이 된다. 

```javascript
let x = 1					
x = 2  // 가능 
let x = 2 //// syntax error
////
let x = 1
if (x === 1){
  let x = 2

  console.log(x)
}
console.log(x)
>>student@DESKTOP MINGW64 ~/Desktop/TIL/05_js/00_js_intro (master)
$ node 00_variable.js
2
1
```

##### const(상수)

- 값이 변하지 않는 상수를 선언하는 키워드
- 담긴 값이 불변임을 뜻하는게 아니다. 
- 단지 상수의 값은 재할당 할수 없고 재선언도 안된다. 
- 블로 유효 범위(block scope)

```js
// const  (상수) 
//const 선언시 초기값을 생략하면 오류 발생
// const MY_FAV  
const MY_FAV = 7
console.log('my favorite number is ' + MY_FAV)

// MY_FAV = 20 // 에러 발생 : 재할당 불가.
// const MY_FAV = 20//SyntaxError: Identifier 'MY_FAV' has already been declared

if (MY_FAV === 7) {
  // 블록 유효 범위로 지정된 MY_FAV 이라는 변수를 받으므로 괜찮다.
  // 즉, 전역이 아닌 범위안이므로 이름 공간에서 출동이 나지 않는다.
  const MY_FAV = 20
  console.log('my favorite number is ' + MY_FAV)
}
console.log( MY_FAV)
```

##### var(변수)

- ES6 이전의 feature로 예기치 않은 문제를 많이 발생시키는 키워드로 사용하지 않는다.
- 함수 유효 범위(function scope)
- var 로 선언된 변수의 범위는 현재 실행 문맥인데, 그 문맥이 함수 혹은 함수 외부의 전역으로도 갈 수 있다. 

```js
function varTest() {
  var x = 1
  if (true){
    var x = 2
    console.log(x)//2  // 상위블록과 같은변수
  }
  console.log(x)//2
}
varTest()
```



#### 식별자(identifier)

- 변수명은 식별자라고 불리며 특정 규칙을 따른다.

1. 반드시 문자, 달러($), 또는 밑줄로 시작해야한다. 이후는 숫자도 가능.
2. 대소문자를 구분하며 클래스명을 재외하고는 대문자로 시작하지 않는 것이 좋다. 
3. 예약어는 사용 불가능 하다. (class, super, const, case, function ... )

```js
///식별자 작성 스타일
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

```



#### Hoisting

- 이 개념은 js 변수, 함수 나 표현이 최상단으로 올려지는것을 말한다. 
- 끌어 올려지는 변수는 `Undefined`값을 반환한다. 
- 변수와 함수를 위한 메모리 공간을 확보하는 과정. 

###### var 할당과정

1. 선언 & 초기화
2. 할당

```js
console.log(a) // undefined
var a = 10
console.log(a)
//js 가 이해한 코드.. 
//선언을 끌어 올림: hoisting
var a // 선언 & 초기화
console.log(a)
a=10  // 할당
console.log(a)
```

###### let, const 할당 과정 

1. 선언 
2. TDZ: Temporal Dead Zone(임시적 사각지대)
3. 초기화
4. 할당

```js
////let은 ReferenceError: Cannot access 'b' before initialization
console.log(b)
let b = 10
console.log(b)
//// 마찬가지로 아래와 같은 과정을 거친다.
let b  // 선언 & TDZ
console.log(b)
b = 10 // 할당 불가 (초기화가 아직 안됨.)
console.log(b)
```

----

- let, const의 정의가 평가 되기 까지 초기화가 되지않는다는 의미이지, 호이스팅이 되지않아 정의가 되지않는 다는 의미와는 다르다. 

- Babel 로 ES6+ 문법을 그보다 아래버전의 JS로 변경해서 사용하기도 한다. (다운그레이드)

### 2.타입과 연산자

**타입**

1. Primitive
2. Reference

##### Primitive

- 불변하다는 특징을 띄고있다

1. Numbers
   - `infinity` : 양의 무한대와 음의 무한대로 나뉨
   - `NaN` : Not a Number, 표현할 수 없는 값, 자기 자신과 일치하지 않는 유일한 값을 표현
     - 0/0, '문자'*10, Math.sqrt(-9)

2. Strings

   ```js
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
   ```

   - `Literal`

     - 값을 프로그램안에서 직접 지정한다는 의미
     - 값을 만드는 방법
     - JS는 우리가 제공한 리터럴 값을 받아 데이터를 만듦

     ```js
     //room 변수를 가리키는 식별자/ 'conference_room'(따옴표 안)은 리터럴
     let room = 'conference_room'
     let hotelRoom = room
     //에러, conference_room 식별자는 존재하지 않는다.
     hotelRoom = conference_room
     ```

     - JS는 따옴표를 통해 리터럴과 식별자를 구별한다. 
     - 식별자는 숫자로 시작할 수 없으므로 숫자에는 따옴표가 필요 없다. (숫자형 리터럴)

   ```js
   const happy = 'hello'
   const hacking = 'world' + 'lol'
   console.log(happy+hacking)
   ```

3. Boolean

4. Empty Value

   - `null`//`undefined`

     - 동일한 역할을 하는 이 2개의 키워드가 존재하는 이유는 단순한 JS의 설계 실수.
     - 큰 차이를 두지 말고 interchangeable 하게 사용할 수 있도록 권장.

   - `undefined`

     - 값이 없을 경우 JS가 자동으로 할당 해주는 값

     ```js
     let first_name // 선언만 하고 할당하지 않음
     console.log(first_name) // undefined
     ```

   - `null`

     - 값이 없음을 우리가 표현하기 위해서 인위적으로 사요하는 값

     ```js
     let last_name = null
     console.log(last_name) // null 의도적으로 값이 없음을 표현
     ```

     `number.isNaN()`

     https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN

     ```js
     // Number.isNaN() 이 함수는 값이 NaN인지 여부를 판단.
     Number.isNaN(1+null) // false --> 숫자
     Number.isNaN(1+undefined) // true --> 숫자 X
     ```

##### Reference



#### 연산자

동등연산자  	`==`

- ```js
  const a =1
  undefined
  const b='1'
  undefined
  a==b
  true
  a===Number(b)
  true
  ```

  자동 형변환

- ```js
  8*null
  0
  '5'-1
  4
  '5'+1
  "51"
  'five'*2
  NaN
  ```



일치 연산자 `===`

- ```js
  a === b
  false
  a === Number(b)
  true
  ```



논리 연산자 `&&`, `||`, `!`

```js
true && false
false
true && true
true
1 && 2
2
1 && 1
1
false || true
true
1 || 0
1
7 || 4
7
4 || 7
4
!true
false
```



삼항 연산자

boolean 값이 true이면 왼쪽값, false라면 오른쪽 값이 나온다.

```js
true ? 1:2
1
false ? 1:2
2

const result = Math.PI > 4 ? 'yes' : 'no'
undefined
result
"no"
```



`prompt`

```js
const userName = prompt('Hello! Who r u?')
undefined
userName
"harry"
```



if 문

```js
if (userName === '1q2w3e4r') {
	message = '<h1> This is admin page</h1>'
} else if (userName === 'ssafy') {
	message = '<h1> You r from ssafy</h1>'
} else {
	message = `<h1> hello ${userName}</h1>`
}
"<h1> hello harry</h1>"
document.write(message)
```



switch 문 : `break`가 있어야한다. 

```js
switch(userName) {
    case '1q2w3e4r': {
		message = '<h1> this is admin </h1>'
		console.log(message)
		break
    }
    case 'ssfy': {
		message = '<h1> you r from ssafy </h1>'
		console.log(message)
		break
    }
    default: {
        message = `<h1> hello, ${userName}</h1>`
		console.log(message)
		break
    }
}
```



## Datastructure object:array