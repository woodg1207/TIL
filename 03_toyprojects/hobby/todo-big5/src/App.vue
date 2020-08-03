<template>
  <div class="">
    <h1> hi </h1>
    <big-test></big-test>
  </div>
</template>

<script>
  // import HelloWorld from './components/HelloWorld';
  import BigTest from './components/personality/BigTest.vue';

  export default {
    name: 'App',
    components: {
      BigTest,
    },
  };
</script>