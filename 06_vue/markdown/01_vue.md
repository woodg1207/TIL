# 1. Vue JS

##### SPA

- single page application

#### vue

```vue
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

#### 바인딩

```html
<body>
  <div id="app"> 
    {{ message }}
  </div>
...
  <script>
    // 바인딩 (Vue와 vue 모델)
    const app = new Vue({
      el: '#app', 
      data: {
        message:'Hello Vue!',
      },
    }) 
  </script>
```



#### 인스턴스 옵션

01_vue_compare_with_js html

```vue

```

- el
  - Vue인스턴스와 DOM을 연결(마운트, mount)하는 옵션
  - View - View Model을 연결시킨다.
  - HTML의 id 나 class 와 마운트가 가능하다.
- data
  - Vue 인스턴스의 데이터 객체, 인스턴스의 `속성`이라고도 부름
  - 데이터 객체는 반드시 기복객체 `{}` 여야함
  - 객체 내부의 아이템들은 value로써 모든 타입의 객체를 가질 수 있다. (object, string, integer array/...)
  - 정의된 속성은 인터플레이션(`{{}}`)을 통해서 View에서 렌더링 가능
  - data에서도 이벤트리스너와 비슷한 이유로 화살표 함수를 작성해서는 안된다.
    - arrow_this.html 참고.
- methods
  - Vue 인스턴스에 추가할 메소드들을 정의하는 곳
  - (주의) 메소드를 정의하는데에 화살표함수를 사용해선 안된다. 



### Vue directive(지시문)

02_vue_todo_app.html 참고.

- 디렉티브는 `v-`접두사가 잇는 특수 속성(attr)이며, 디렉티브 속성의 값은 단일 JS표현식.

##### v-for 반복문.

```html
  <div id="app">
    <li v-for="todo in todos">
      {{ todo }}
    </li>
  </div>
```

#### v-if 조건문

- 특정 조건을 만족할때만 보여지도록(렌더링 되도록) 할 수 있다.
- `v-else`는 반드시 `v-if`엘리먼트 바로 뒤에 와야 인식가능
- `v-else-if` 도 존재

```vue
  <div id="app">
    <li v-for="todo in todos" v-if="!todo.completed">
      {{ todo.content }}
    </li>
    <li v-else>[완료]</li>
  </div>
```

##### 우선순위

- 동일한 노드에서는 v-for 가 v-if  보다 높은 우선순위를 가짐.
- 즉, v-if는 루프가 반복될때 마다 실행이 된다. (일부 항목만 렌더링 할때 유용.)

#### v-on

- JS에서 이벤트리스너랑 비슷한 역할을 함.

- 이벤트 리스너는 HTML element를 querySelector로 가져와 이벤트를 붙여줬다면, Vue는 HTML element자체에 이벤트를 붙여준다.

- `v-on:`뒤에 오는 친구들을 `전달인자`라고 한다.

- `:`을 붙여 사용하는, 디렉티브 바로 뒤에 붙는 친구들을 지칭한다.

- 1번 - inline 방식`v-on:click="todo.completed = true"`

- 2번 - method 정의

  - ```vue
    <div id="app">
        <li v-for="todo in todos" v-if="!todo.completed" v-on:click="check(todo)">
          {{ todo.content }}
        </li>
    ...
        const app = new Vue({
          el: '#app',
          data: {
    ...
          },
          methods: {
            check: function(todo) {
              todo.completed = true
    ...
    ```

#### v-vind

```html
    <img v-bind:src="vueImage" alt="todo-list">
```

- vueImage = '' 이미지 저장.



#### v-model  

02_vue_.. html

- input tag 의  value- View ----- v-model ------------data(VM)



### computed

- 미리 계산된 값을 반환.
- 종속 대상을 따라 저장(캐싱)되는 특성이 있다.
- 연산이 많이 필요한 경우 템플릿 안에서 연산 표현식을 사용하는 것보다  computed를 사용하는 것을 권장.
- `{{ newTodo.split('').reverse().join('') }}`

```vue
computed: {
	reverseNewTodo: function(){
		return this.newTodo.split('').reverse().join('')
	}
}
```



#### Watch

- Vue 인스턴스의 data 변경하고 이에 반응.
- 데이터 변경에 대한 응답으로 비동기 또는 시간이 많이 소요되는 조작을 수행하려는 경우에 적합.
- 특정 데이터가 변경되었을 때 정의한 함수를 실행.
- 

```vue
watch: {
        todos:{
          // handler 특정데이터가 변경 되었을 때, 실행할 함수
          handler: function(todos){
            todoStorage.save(todos)
          },
          // 객체의 nested item 들도 관찰할지 유무를 설정. true인 경우 내부 요소들도 감시하도록 함.
          deep: true,
        }
      },
```



#### mounted

```vue
// 새로고침 될때(DOM과 Vue instance가 연결되는 시점) 실행되는것
mounted: function(){
	this.todos = todoStorage.fetch()
},
```



#### v-if & v-show

05_optional_directive.html

- v-if: 조건에 맞지 않으면 렌더링 자체를 하지 않음
- v-show: 조건과 관계없이 일단 렌더링 후에, 조건에 맞지 않으면 css display 속성을 토글해서 숨겨버림.

```html
   <p v-if="false">{{name3}}</p>
    <p v-show="false">{{name3}}</p>
```



#### short cut

`v-bind:` -> `:`

`v-on:`-> `@`



#### computed VS watch

- computed: 계산해야하는 `목표데이터를 정의하는 방식` (선언형 프로그래밍)
- watch: 감시할 데이터를 지정하고 그 `데이터가 바뀌면 특정 함수를 실행하는 방식 `(명령형 프로그래밍)



### 컴포넌트

03_todo_component.html

"소프트웨어 개발에서 독립적인 단위 모듈"

- 대체로 컴포넌트는 특정 기능이나 관련된 기능의 조합으로 구성되는데, 프로그래밍 설계에서 시스템은 모듈로 구성된 컴포넌트로 나뉜다.
- VUE- "기본 HTML 엘리먼트를 확장하여 재사용가능한 코드로 캡슐화 하는 것"



##### 컴포넌트 naming convention

- 컴포넌트의 첫번째 인자는 태그 이름, 두번째인자는 속성들을 넣어준다.
- `Vue.component('todo-list', {})`

1. kebab-case
   - 호출 할때: `<todo-list></todo-list>`케밥케이스 태그로만 호출이 가능.
2. paskal Case `ToDoList`
   - 호출 할때: `<todo-list></todo-list>`/ `<ToDoList>`둘다 호출 가능.
   - 단, DOM에 직접 작성 할때 는 케밥케이스만 가능.

- 그래서 Vue는 모두 소문자여야하고, 하이픈을 포함하는 규칙을 따르는 것을 권장 한다.



#### props

- 컴포넌트를 재생산 할때 컴포넌트에서 사용할 변수를 부모에서 내려주게 되는데 이를`props`라고 한다.

- 반복되는 컴포넌트에 서로 다른 정보가 들어가야 할 때 사용
- 하위(작식)에서 상위(부모) 데이터를 직접 참조해선 안되고 실제로도 안된다.
- `props`옵션을 통해 부모-> 자시긍로 데이터를 전달.

- 전달 하려고 하는 데이터의 이름을 태그 내의 속성으로, 내용을 속성값으로 넣어준다.

  - ```vue
    <todo-list category="취업특강"></todo-list>
    <todo-list category="SSAFY"></todo-list>
    <todo-list category="기타"></todo-list>
    ```

