<template>
  <div class="dataview">

    <nav><router-link to="/">Log Out</router-link></nav>
    <img alt="Vue logo" src="../assets/logo.png">
    <GreyBook/>
    <el-row v-for="(o, index) in books" :key="o" :offset="index > 0 ? 3 : 0">
      <MyBook><books/></MyBook>
    </el-row>


  </div>
</template>

<script>
import MyBook from '@/components/MyBook.vue'
import GreyBook from '@/components/GreyBook.vue'
import axios from 'axios';
export default {
  name: 'My-Books',
  components: {
    MyBook,
    GreyBook,
    books: []
  },
  methods: {
    loadBooks: function() {
      axios.get('/api/books/').then(
        response => {
          this.books = response.data;
        }
      );
    },
  },
  created() {
    this.loadBooks();
  }
}

</script>

<style>

</style>