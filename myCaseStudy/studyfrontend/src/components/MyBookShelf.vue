<template>
  <el-row>
    <el-col :span="6" v-for="(o, index) in 3" :key="o" :offset="index > 0 ? 3 : 0">
      <MyBook></MyBook>
    </el-col>
  </el-row>
</template>

<script>
import MyBook from '../components/MyBook.vue'
export default {
  name: 'My-Books',
components: {
    MyBook
  }
}
</script>

<style>

</style>