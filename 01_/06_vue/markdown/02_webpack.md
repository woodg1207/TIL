

# 02_webpack

#### webpack

- 웹펙은 현재 가장 널리 쓰이는 번들러,
- JS뿐만 아니라, CSS,Image파일 등 리소스의 의존성등도 관리한다.



####  모듈

- 어플리케이션을 구성하는 개발적 욧,
- 재사용 가능한 코드 조각
- 모듈로 세부사항을 캡슐화 한다.

#### 모듈 번블러

- 웹 어플리케이션을 구성하는 자원(HTMl, CSS, JS, IMG등)을 모두 각각의 모듈로보고 이를 조합해서 병합된 하나의 결과물로 만드는 도구.
- 

ex) 개발을 편하게 모듈로 개발 => 모듈끼리 연결 (의존성)을 신경쓰기가 어려워짐==> 웹펙아 하나로 만드어줘

webpack.config.js

```js
module.exports = {
  entry: {},
  module: {},
  plugins: {},
  output: {},
}
```

###### entry 

- 여러 js 파일들의 시작점-> 웹팩이 파일을 읽어 들이기 시작하는 부분

###### module

- 웹팩은 js만 변환 가능하기 때문에 html, css 등은 모듈을 통해서 웹팩이 이해할수 있도록 변환이 필요하다.
- 변환 내용을 담는 곳,

###### plugins

- 웹팩을 통해서 번들된 결과물을 추가 처리하는 부분.

###### output

- 여러 js 파일을 **하나로 만들어낸 결과물**.

----

웹팩은 js코드만 이해 가능하기 때문에 vue파일(vue-loader)및 html, css 파일(vue-template-compiler) 등을 변환하기 위하여 모듈을 설치 .

---

최상위 컴포넌트(App.vue)

하위 컴포넌트(TodoList.vue)

---

#### 컴포넌트 등록 3step( App.vue)

1. `<script>`에 등록할 컴포넌트 불러오기(import)
2. `export default`에 `components`항목에 추가
3. `<template>`에서 컴포넌트 사용할 수 있도록 작성.

---

#### vue-cli

웹팩을 직접 작성했을때, 만들었던`webpack.config.js`가 보이지 않는다. 

`vue.config.js`는 vue-cli에 의해 자동으로 로드되는 선택적 구성 파일로 변경되었다.

vue-cli3 버전부터 노출되지 않으며, 설정을 추가하기 위하여