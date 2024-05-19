<template>
  <div>
    <h2>Drones</h2>
    <ul>
      <li v-for="drone in drones" :key="drone.id">{{ drone.name }} - {{ drone.model }}</li>
    </ul>
  </div>
</template>

<script>
import axios from '@/api/axios';

export default {
  data() {
    return {
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
  }
}
</script>
