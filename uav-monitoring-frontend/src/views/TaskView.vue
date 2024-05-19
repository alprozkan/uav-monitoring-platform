<template>
    <div>
      <TaskDetails :taskId="$route.params.id" />
    </div>
  </template>
  
  <script>
  import TaskDetails from '@/components/TaskDetails.vue';
  
  export default {
    components: {
      TaskDetails
    }
  }
  </script>
  