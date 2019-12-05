import jwtDecode from 'jwt-decode'

const state = {
  token : null,
  loading : false,
}
// data(state)를 변경하지 않음
// data를 원본 그대로 혹은 가공된 데이터를 사용.
const getters = {
  isLoggedIn: function(state) {
    return state.token ? true : false
  },
  requestHeader: function(state){
    return{
      headers:{
        Authorization:'JWT '+state.token
      }
    }
  },
  userId: function(state) {
    return state.token ? jwtDecode(state.token).user_id : null
  }
}

// 상태(토큰)를 받아와서 state를 update
const mutations = {
  setToken: function(state, token) {
    state.token = token
  },
  setLoading:function(state, status) {
    state.loading = status
  }

}

// 비동기 로직 (axios로 django서버에 로그인/로그아웃 요청)
// options
// action 에서 사용할 수 있도록 만든 객체 / vuex에서 제공하는 actions 함수에서 사용할 수 있는 option들이 있는 객체
const actions ={
  // commit은 첫번째 인자로 mutations에 정의한 함수를 받는다. 
  // 두번째 인자로 토큰을 받아서, mutations에 정의된 함수를 통해 state를 변경한다. 
  login: function(options, token){
    options.commit('setToken', token)
  },
  // 로그아웃의 경우 추가로 받는 인자느 없고 token의 상태를 null로 변경한다.
  logout: function(options){
    options.commit('setToken')
  },
  startLoading: function(options){
    options.commit('setLoading', true)
  },
  endLoading: function(options){
    options.commit('setLoading', false)
  },
}

export default {
  state,
  mutations,
  actions,
  getters,
}