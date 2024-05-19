<template>
    <div>
      <h2>Task Details</h2>
      <div v-if="task">
        <p><strong>Task Name:</strong> {{ task.name }}</p>
        <p><strong>Description:</strong> {{ task.description }}</p>
        <p><strong>Drone:</strong> {{ task.drone_id }}</p>
        <button @click="executeTask">Execute Task</button>
      </div>
      <div v-if="images.length">
        <h3>Captured Images</h3>
        <ul>
          <li v-for="image in images" :key="image.id">{{ image.path }}</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import axios from '@/api/axios';
  
  export default {
    props: ['taskId'],
    data() {
      return {
        task: null,
        images: []
      }
    },
    mounted() {
      this.fetchTaskDetails();
      this.fetchTaskImages();
    },
    methods: {
      fetchTaskDetails() {
        axios.get(`/tasks/${this.taskId}`)
          .then(response => {
            this.task = response.data;
          })
          .catch(error => {
            console.error(error);
          });
      },
      fetchTaskImages() {
        axios.get(`/tasks/${this.taskId}/images`)
          .then(response => {
            this.images = response.data;
          })
          .catch(error => {
            console.error(error);
          });
      },
      executeTask() {
        axios.post(`/tasks/${this.taskId}/execute`)
          .then(response => {
            this.images = response.data.images;
            alert('Task executed successfully and images captured!');
          })
          .catch(error => {
            console.error(error);
            alert('Failed to execute task');
          });
      }
    }
  }
  </script>
  