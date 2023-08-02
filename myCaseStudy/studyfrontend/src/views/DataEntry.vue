<template>
  <div class="addform">
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
