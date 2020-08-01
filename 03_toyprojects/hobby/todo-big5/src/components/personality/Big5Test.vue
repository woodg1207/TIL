<template>
  <h1>hello</h1>
  <ul v-for="question in questions">
    <p>{{question.content}}</p>
  </ul>
</template>

<script>
  export default {
    name: 'Big5Test',
    data: {
      questions: [{
          content: '1'
        },
        {
          content: '2'
        },
      ]
    },
    props: {
      questions: {
        type: Array,

      }
    }
  }
</script>

<style>

</style>