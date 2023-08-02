<template>
  <div class="hello">

    <h1>Log In</h1>
    <p>
      Please enter your credentials below.
    </p>
    <el-form>
      <el-input placeholder="Please input username" v-model="Uinput"></el-input>
    <el-input placeholder="Please input password" v-model="Pinput" show-password></el-input>
  </el-form>
    <ul>
      <router-link to="/DataView"><el-button type="primary">Login</el-button></router-link>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'LoginPrompt',
  data() {
      return {
        Uinput:'',
        Pinput: ''
        
      }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.el-form{
  width: 33%;
  margin-left: auto;
  margin-right: auto;
}
div{
  padding: 1%;
}
</style>
