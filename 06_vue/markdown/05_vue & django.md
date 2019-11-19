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