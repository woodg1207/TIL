# 05_vue&django_2

![](C:\Users\student\Desktop\TIL\06_vue\markdown\img\Screen Shot 2019-11-19 at 10.31.41 AM.png)

---

`this.$session.start()`

- session-id 초기화. 만약 세션이 없이 저장하려고 하면 vue-session플러그인이 자동으로 새로운 세션을 시작

`this.$session.set(key,value)`

- session에 해당 key에 맞는 값을 저장

`this.$session.has(key)`

- key(JWT)가 존재하는지 여부를 확인

`this.$session.destroy()`

- 세션을 삭제

---

### 흐름

###### 0. Django

- 회원가입

###### 1.Vue -> django

- 로그인 정보(credentials)를  django서버로 보냄

###### 2. Django

- vue 에서 받은 유저정보에 해당하는 고유한 Web Token 발급.

###### 3. Django -> Vue

- 해당 유저에 대한 토큰을 Vue 로 보냄.

###### 4. Vue

- Django에서 받은 토큰을 vue-session을 통해 저장( 이 시점부터 vue에서는 로그인 성공 상태.)

###### 5. Vue -> Django

- vue-session에 저장된 토큰을 가지고 django 에 로그인 요청.

###### 6. Django

- 최초로 보낸 토큰과 일치하는지 여부를 확인(세션에 저장된 토큰 == 요청자 토큰)

---

`.start()`을 통해 `session-id:sess+Date.now()`가만들어짐

`.set()`을 통해 `jwt: jwt값` 이 만들어짐.

---

### vue lifecycle

1. Vue instance 생성 (create)
2. DOM 에 부착 (mounted)
3. 업데이트(Update)
4. 사라짐.(destroy)

----

#### FormData

- 기존 키에 새로운 값을 추가하거나 키가 없는 경우 새로운 키를 추가.(`FormData.append()`)
- `FormData.append(name, value)`
- name : value에 포함되는 데이터 필드 이름
- value : 필드값

---

#### `splice()`

- 배열의 기존 요소를 삭제 혹은 교체하거나 새 요소를 추가하여 배열의 내용을 변경

문법

- `Array.splice(시작idx, 삭제할 요소 수, 배열에 추가할 요소)`
- `splice(start idx, delete_count, [item1, item2, item3...])

1. `start`
   - 배열의 변경을 시작할 인덱스
   - 배열의 길이보다 큰 값인면 시작 인덱스는 배열의 길이로 설정
   - 음수인 경우 배열의 가장 마지막에서 시작
   - 절대값이 배열의 길이보다 큰 경우는 0으로 설정.
2. `delete_count`
   - 배열에서 제거할 요소의 수
   - 생략할 경우 start부터 모든 요소를 제거
   - 0 이하인 경우 어떤요소도 삭제하지 않음. 이때는 최소한 하나의 추가할 새로운 요소 지정.
3. item1, item2...
   - 배열에 추가할 요소
   - 추가할 요소도 지정하지 않으면 요소를 제거만 한다.
   - 즉, **추가할 요소를 지정 하지 않으면 원본 배열의 특정인덱스에서 몇개의 요소를 삭제** 할지 정한다.

---

#### `updated`

타입

- function

상세

- 데이터가 변경되어 DOM이 re-render 되고 patch 되면 호출된다. (DOM의 변화에 반응.)
- DOM의 변화는 일반 적으로 데이터의 변경에 의해 re-render되는 시점에 일어난다.
- 데이터의 변화(상태의 변화)에 반응하기 위해서는 computed나 watch를 사용하는 것이 좋다. 

---

### Vuex

- State 관리를 위해 탄생
- 컴포넌트 간의 통신 혹은 데이터 전달을 유기적으로 관리
- 컴포넌트간의 통신 혹은 이벤트 등의 관계를 한 곳에서 관리하기 쉽게 구조화.
- vue-session의 대체가 아니고 서로하는 일이 다르다.
- 메서드와 data의 대체라고 생각하자.



현재 todo프로젝트에서는 Auth 정보(로그인 혹은 로그 아웃)는 Django로 요청을 보낼 때 항상필요하기 때문에, 요청을 수행하는 모든 컴포넌트에서 알고 있어야 하고 그정보를 내가 필요한 순간에 활용할수 있어야 한다.

1. state
   - 상태(데이터)
2. Getters
   - computed
3. Mutations(변화)
   - methods
   - state를 변경하기 위해서 반드시 동기적인 method만 사용가능
   - 첫번째 인자는 항상 state, 호출은 commit으로 된다.
4. Actions
   - methods
   - 비동기 처리가 가능한 methods까지 가능.(동기, 비동기 가능)
   - mutations와 구분된 이유는 다양한 컴포넌트에서 vuex를 통해 상태관리, 메서드 호출등을 하게 될텐데 그때, 동기와 비동기를 구분하기위해 사용.
   - 첫번째 인자는 항상 context(state/commit/dispatch 등), 호출은 dispatch 로 된다. 