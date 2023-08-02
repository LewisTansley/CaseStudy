<template>
  <div class="dataview">

    <nav><router-link to="/">Log Out</router-link></nav>
    <img alt="Vue logo" src="../assets/logo.png">

    <GreyBook/>
    <el-row v-for="(o, index) in 3" :key="o" :offset="index > 0 ? 3 : 0">
      <MyBookShelf/>
    </el-row>


  </div>
</template>

<script>
import MyBookShelf from '@/components/MyBookShelf.vue'
import GreyBook from '@/components/GreyBook.vue'
export default {
  name: 'My-Books',
  components: {
    MyBookShelf,
    GreyBook
  }
}

</script>

<style>

</style>