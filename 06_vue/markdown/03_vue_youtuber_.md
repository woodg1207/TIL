# 03_vue_youtuber_

###### 사용자가 검색어 입력(search bar)

- 검색결과를 App.vue로 올려줌



##### 단방향 데이터 흐름의 이점

1. vue app의 데이터 흐름을 쉽게 파악할 수 있음
2. 부모 컴포넌트에서 업데이트가 일어나면 자식컴포넌트는 자동업데이트(즉, 자식 컴포넌트의 상태를 관리하지 않아도 된다.)
3. 하위 컴포넌트가 실수로 부모의 상태를 변경하여 app data의 흐름을 추론하기 어렵게 만드는 것을 방지할 수 있다.



#### SearchBar

1. 사용자가  input 에 입력하면 onInput함수가 실행
2. inputChange 이벤트와 사용자가 입력한value가 상위컴포넌트인 App.vue 로 event와 inpout value가 emit 된다. 

##### App

3.  SearchBar에서 넘어온 이벤트 inputChange로 인해 onInputChange함수가 실행된다.
4. onInputChange함수는 유튜브 api요청을 보내고 비디오 리스트를 응답받는다.
5. 넘겨 받은 비디오 리스트를 videos 라는 배열에 저장한다.
6.  `data` object가 (videos 배열이 있는곳) 업데이트 되면, 해당 컴포넌트(App.vue 가 템플릿을 다시 렌더링 한다.)
7. 그리고 바로 자식 컴포넌트들도 모두 다시 렌더링 된다.
8. `VideoList` 컴포넌트가 비디오 배열을 받아 화면을 보여주게 된다.