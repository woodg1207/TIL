<template>
  <div class="home">
    <h1>ToDo with Django</h1>
    <TodoInput @createTodo="createTodo"/>
    <TodoList :todos="todos"/>

  </div>
</template>

<script>
// @ is an alias to /src

import router from '../router'
import TodoList from '@/components/TodoList'
import TodoInput from '@/components/TodoInput'
import axios from 'axios'
// import jwtDecode from 'jwt-decode'
import {mapGetters} from 'vuex'

export default {
  name: 'home',
  components: {
    TodoList, TodoInput,
  },
  data(){
    return {
      todos:[],
    }
  },
  computed: {
    ///... spread 문법 -> 각각의 getters
    // mapGetters 함수의 인자로 들어가느 배여레는 getters에서 갖고 오고싶은것 들만 갖고옴
    ...mapGetters([
      'isLoggedIn',
      'requestHeader', 
      'userId',
    ])
  },
  methods:{
    checkLoggedIn() {
      // this.$session.start()
      if (!this.isLoggedIn){
        router.push('/login')
      }
    },
    getTodos(){
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const requestHeader = {
      //   headers:{
      //     Authorization: 'JWT '+ token
      //   }
      // }
      // const user_id = jwtDecode(token).user_id
      // console.log(jwtDecode(token))

      axios.get(`http://127.0.0.1:8000/api/v1/users/${this.userId}/`, this.requestHeader)
        .then(res=>{
          console.log(res)
          this.todos = res.data.todo_set
        })
        .catch(err=>{
          console.log(err)
        })
    },
    createTodo(title) {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const requestHeader = {
      //   headers:{
      //     Authorization: 'JWT '+ token
      //   }
      // }
      // const user_id = jwtDecode(token).user_id
      const requestFrom = new FormData()
      requestFrom.append('user', this.userId)
      requestFrom.append('title', title)
      axios.post('http://127.0.0.1:8000/api/v1/todos/', requestFrom, this.requestHeader)
        .then(res => {
          this.todos.push(res.data)
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    } 
  },
  // DOM  에 Vue instance 가 mount 될때마다 checkLoggedIn 이 실행되어 로그인 여부를 채크
  mounted() {
    this.checkLoggedIn()
    this.getTodos()
  },
}
</script>
