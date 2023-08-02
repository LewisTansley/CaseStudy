<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <LoginPrompt/>
  </div>
</template>

<script>
// @ is an alias to /src
import LoginPrompt from '@/components/LoginPrompt.vue'

export default {
  name: 'HomeView',
  components: {
    LoginPrompt
  }
}
</script>
