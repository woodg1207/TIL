<template>
  <div>
    <input @input="onInput" type="text">

  </div>
</template>

<script>

  export default {
    name: 'SearchBar',
    methods: {
      onInput(e) {
        this.$emit('inputChange', e.target.value)
      }
    },
  }
</script>

<style>

</style>