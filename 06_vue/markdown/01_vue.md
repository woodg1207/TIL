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

