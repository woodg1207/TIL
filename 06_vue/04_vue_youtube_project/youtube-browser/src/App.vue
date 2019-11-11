<template>
  <div id="app">
    <!-- 만약 inputChange 이벤트가 일어나면 onInputChange라는 method가 실행됨 -->
    <search-bar @inputChange="onInputChange"></search-bar>
    <video-list :videos="videos"></video-list>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar'
import VideoList from './components/VideoList'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App', // 최상단 컴포넌트기 때문에 이름이 없어도 되지만, 명시적으로 작성한다.
  data() {
      return { // componet에서만 return을 객체로 감싸줘야함. 
        // Vue component에서는 반드시  Object를 return 하는 함수로 작성.
        videos: [],
      }
    },
  components: {
      SearchBar, VideoList,
    },
  
  methods:{
    onInputChange(inputValue) {
      axios.get(API_URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: inputValue,
        }
      })
      .then(response => {
        this.videos = response.data.items
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
}
</script>

<style>

</style>
