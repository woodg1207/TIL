<template>
  <ul>
    VideoList
    {{ videos.length }}
  </ul>
</template>

<script>
  export default {
    name: 'VideoList',
    props:{
      videos:{
        type: Array,
        required: true,
      },
    },
  }
</script>

<style>

</style>