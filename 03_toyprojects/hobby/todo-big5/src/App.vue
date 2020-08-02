<template>
  <v-app>
    <big-test></big-test>
  </v-app>
</template>

<script>
  // import HelloWorld from './components/HelloWorld';
  import BigTest from './components/personality/Big5Test';

  export default {
    name: 'App',
    components: {
      BigTest,
    },
  };
</script>