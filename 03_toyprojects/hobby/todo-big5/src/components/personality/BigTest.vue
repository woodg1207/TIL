<template>
<div>
  <v-radio-group v-model="gender" column row>
    <v-radio label="male" value="0"></v-radio>
    <v-radio label="female" value="1"></v-radio>
  </v-radio-group>
  <div v-for="q in questions" :key="q.id">
    <span>{{q.content}}</span>
    <v-radio-group v-model="q.point" column row>
      <v-radio label="Option 1" value="1" ></v-radio>
      <v-radio label="Option 2" value="2" ></v-radio>
      <v-radio label="Option 3" value="3"></v-radio>
      <v-radio label="Option 4" value="4"></v-radio>
      <v-radio label="Option 5" value="5"></v-radio>
    </v-radio-group>
    <!-- <span>{{q.point}}</span> -->
    <hr>
  </div>
  <br>
  <v-btn x-large color="success" dark @click="sumPoint()"> click me! </v-btn>
</div>
  
</template>

<script>
  export default {
    name : 'BigTest',
    data(){
      return {
        gender : '',
        questions : [
          {
            id:1,
            content:'Q1 : 모르는 사람에게 먼저말을 건다.',
            point:'',
          },
          {
            id:2,
            content:'Q2 : 다른 사람이 편안하고 행복한지 확인한다.',
            point:'',
          },
          // {
          //   id:3,
          //   content:'Q3 : 그림, 글, 음악을 창작한다.',
          //   point:'',
          // },
          // {
          //   id:4,
          //   content:'Q4 : 모든 일을 사전에 준비한다.',
          //   point:'',
          // },
          // {
          //   id:5,
          //   content:'Q5 : 울적하거나 우울함을 느낀다.',
          //   point:'',
          // },
          // {
          //   id:6,
          //   content:'Q6 : 회식, 파티, 사교모임을 계획한다.',
          //   point:'',
          // },
          // {
          //   id:7,
          //   content:'Q7 : 사람들을 비난한다.',
          //   point:'',
          // },
          // {
          //   id:8,
          //   content:'Q8 : 철학적이거나 영적인 문제들을 생각한다.',
          //   point:'',
          // },
          // {
          //   id:9,
          //   content:'Q9 : 일이나 물건을 정리하지 않고 어지럽게 그냥 둔다.',
          //   point:'',
          // },
          // {
          //   id:10,
          //   content:'Q10 : 스트레스나 걱정을 느낀다.',
          //   point:'',
          // },
          // {
          //   id:11,
          //   content:'Q11 : 어려운 단어를 사용한다.',
          //   point:'',
          // },
          // {
          //   id:12,
          //   content:'Q12 : 타인의 감정에 공감한다.',
          //   point:'',
          // },
          ],
      }
    },
    methods:{
      sumPoint:function(){
        // console.log(this.questions)
        this.questions.forEach(element => {
          if(element.point == ''){
            console.log('noo')
          }
          else{
            console.log(element.point)
          }
        });        
      }
    },

  }
</script>

<style>

</style>