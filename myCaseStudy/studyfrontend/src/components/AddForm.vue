<template>
  <div class="hello">
    <h1>Add new Book</h1>
    <p>
      Please input required information.
    </p>
    <el-form :gutter="100">
      <el-input placeholder="book author" v-model="authorInput"></el-input>
      <el-input placeholder="book title" v-model="titleInput"></el-input>
      <el-input placeholder="book descriptions" v-model="descInput"></el-input>
      <p>Book Cover Image: <file-select v-model="file"></file-select></p>
      <p v-if="file">{{file.name}}</p>
  </el-form>
    <ul>
      <el-button type="primary">SAVE</el-button>
    </ul>
  </div>
</template>

<script>
import FileSelect from '@/components/FileSelect.vue'
export default {
  components: {
    FileSelect
  },
  name: 'AddForm',
  data() {
      return {
        authorInput:'',
        titleInput: '',
        descInput:''        
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
