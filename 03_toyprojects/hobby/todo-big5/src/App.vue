<template>
  <v-app>
    <big-test :questions="questions"></big-test>
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

    data() {
      return {
        questions: [],
      }
    }
  };
</script>