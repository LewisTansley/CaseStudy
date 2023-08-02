<template>
  <div class="dataview">
    <MyBook/>
    <GreyBook/>
  </div>
</template>

<script>
import MyBook from '@/components/MyBook.vue'
import GreyBook from '@/components/GreyBook.vue'
export default {
  name: 'My-Books',
  components: {
    MyBook,
    GreyBook
  }
}

</script>

<style>

div{
  padding: 1%;
}


</style>