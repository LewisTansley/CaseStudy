<template>
  <div class="addform">
    <nav><router-link to="/DataView">Back</router-link></nav>
    <AddForm/>
  </div>
</template>

<script>
// @ is an alias to /src
import AddForm from '@/components/AddForm.vue'
export default {
  name: 'DataEntry',
  components: {
    AddForm
  }
}
</script>
