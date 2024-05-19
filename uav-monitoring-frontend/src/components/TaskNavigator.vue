<template>
    <div>
      <h2>Navigate to Task</h2>
      <form @submit.prevent="navigateToTask">
        <div>
          <label for="taskId">Task ID:</label>
          <input type="text" v-model="taskId" id="taskId" required>
        </div>
        <button type="submit">Go to Task</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        taskId: ''
      }
    },
    methods: {
      navigateToTask() {
        this.$router.push(`/task/${this.taskId}`);
      }
    }
  }
  </script>
  