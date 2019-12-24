const me = {
  name: 'ssafy', // key 가 한단어 일때 변수처럼 가능
  'phone number': '01012341234', // key가 여러 단어 일때 
  appleProduct: {
    ipad: '2018pro',
    iphone: '7',
    macbook: '2019pro',
  }
}

console.log(me.name) // ssafy
console.log(me['name']) //ssafy
console.log(me['phone number']) //여러단어는 [] 로 접근...
console.log(me.appleProduct.ipad)


// Object Literal (객체 표현법)  
//ES5 버전에 사용하던 방법
var books = ['Learning JS', 'Eloquent JS']

var comics = {
  'DC': ['Joker', 'Aquaman'],
  'Marvel': ['Captain Marvel', 'Avengers'],
}

var magazines = null

var bookShop = {
  books: books,
  comics: comics,
  magazines: magazines,
}
console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books[0])

// ES6+
// object의 key 와 value가 같다면 , 마치 배열처럼 한번만 작성이 가능
let bookShopTwo = {
  books,
  comics,
  magazines,
}
console.log(bookShopTwo)
console.log(typeof bookShopTwo)
console.log(bookShopTwo.books[0])

// JSON(JS Object Notation, JS 객체 표기법)
// KEY:Value 형태의 자료구조를 JS객체와 유사한 모습으로 표현하는 기법
// 모습만 비슷할 뿐이고, 실제로 Object 처럼 사요하려면 다른 언어들 처럼 
// JS에서도 Parsing(구문분석) 작업이 필요.

const jsonData = JSON.stringify({ //JSON을 string으로 
  coffe: 'Americano',
  iceCream: 'Mint Choco',
})
console.log(jsonData) //{"coffe":"Americano","iceCream":"Mint Choco"}
console.log(typeof jsonData) //string

const parseData = JSON.parse(jsonData) 
console.log(parseData) //{ coffe: 'Americano', iceCream: 'Mint Choco' }
console.log(typeof parseData)  // object

//정리
// Object - JS의 Key:value 페어의 구조
// JSON - 데이터를 표현하기 위한 단순한 문자열.
