<template>
    <div>
      <h2>Create Task</h2>
      <form @submit.prevent="createTask">
        <div>
          <label for="name">Task Name:</label>
          <input type="text" v-model="task.name" id="name" required>
        </div>
        <div>
          <label for="description">Description:</label>
          <textarea v-model="task.description" id="description"></textarea>
        </div>
        <div>
          <label for="drone">Assign Drone:</label>
          <select v-model="task.drone_id" id="drone" required>
            <option v-for="drone in drones" :key="drone.id" :value="drone.id">{{ drone.name }}</option>
          </select>
        </div>
        <button type="submit">Create Task</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from '@/api/axios';
  
  export default {
    data() {
      return {
        task: {
          name: '',
          description: '',
          drone_id: null
        },
        drones: []
      }
    },
    mounted() {
      axios.get('/drones')
        .then(response => {
          this.drones = response.data
        })
        .catch(error => {
          console.error(error);
        });
    },
    methods: {
      createTask() {
        axios.post('/tasks', this.task)
          .then(() => {
            alert('Task created successfully!')
          })
          .catch(error => {
            console.error(error)
            alert('Failed to create task')
          })
      }
    }
  }
  </script>
  