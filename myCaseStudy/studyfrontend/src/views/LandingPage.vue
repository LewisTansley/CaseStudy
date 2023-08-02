<template>
  <div class="home">
    <nav><router-link></router-link></nav>
    <img alt="Vue logo" src="../assets/logo.png">
    <h1>Library of Babel (.js)</h1>
    <RouterLink to="/LoginPage"><el-button type="primary">Log In</el-button></RouterLink>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Landing-Page',
  components: {
  }
}
</script>
