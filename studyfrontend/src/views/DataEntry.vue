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
      <p>Attach Cover Image:</p>
      <file-select v-model="file"></file-select>
      <p v-if="file">{{file.name}}</p>
      <el-row>
        <el-col :span="12">
          <router-link to="/DataView"><el-button type="danger">cancel</el-button></router-link>
        </el-col>
        <el-col :span="12">
          <el-button type="success" function="addBook">save</el-button>
        </el-col>
      </el-row>
    </el-form>
  </div>
</template>

<script>
import FileSelect from '@/components/FileSelect.vue'
import axios from 'axios';

export default {
  components: {
    FileSelect
  },
  name: 'AddForm',
  data() {
      return {
        titleInput: '',
        authorInput:'',
        descInput:'',        
        file:''
      }
    },
  addBook: function() {
    axios.post('/upload/', {title: this.titleInput, author: this.authorInput, description: this.descInput, book_cover: this.file}).then(
      response => {
        this.books.push(response.data);
      }
    );
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
