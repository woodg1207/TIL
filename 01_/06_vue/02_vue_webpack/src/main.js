// Vue 인스턴스를 최종으로 만드는 파일.
// 1. 설치된 vue를 추가
// (내가 만든 파일이 아닌 경우) 현재위치에서 vue이름을 가진 폴더가 없음=> 자동으로 node_modules에서 가져옴
import Vue from 'vue' 

// 2. 최상위 컴포넌트 추가
// (내가 만든 파일) 상대경로 표시
import App from './App.vue'

new Vue({
  render: h => h(App)
}).$mount('#app')
