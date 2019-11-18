<template>
  <div>
    <LoginForm/>
  </div>
</template>

<script>
  // @ 는 /src의 alias
  // import LoginForm from '../components/LoginForm' // 상대경로.
  import LoginForm from '@/components/LoginForm'  //절대 경로
  export default {
    name:'login',
    components:{
      LoginForm,
    }
  }
</script>

<style >

</style>