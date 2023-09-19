<template>
  <div class="hello">

    <h1>Log In</h1>
    <p>
      Please enter your credentials below.
    </p>
    <el-form @submit.prevent="submit">
      <el-input placeholder="Please input username" v-model="form.username"></el-input>
      <el-input placeholder="Please input password" v-model="form.password" show-password></el-input>
      <RouterLink to="/DataView"><el-button type="primary">Log In</el-button></RouterLink>
      <el-button type="submit">submit</el-button>
      <p v-if="showError" id="error">Username or Password is incorrect</p>
    </el-form>

  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Login-Page",
  components: {},
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
      showError: false
    };
  },
  methods: {
    ...mapActions(["LogIn"]),
    async submit() {
      const User = new FormData();
      User.append("username", this.form.username);
      User.append("password", this.form.password);
      try {
          await this.LogIn(User);
          this.$router.push("/books");
          this.showError = false
      } catch (error) {
        this.showError = true
      }
    },
  },
};
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
