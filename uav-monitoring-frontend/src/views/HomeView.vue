<template>
  <div>
    <DroneList />
    <TaskForm />
    <TaskNavigator />
  </div>
</template>

<script>
import DroneList from '@/components/DroneList.vue'
import TaskForm from '@/components/TaskForm.vue'
import TaskNavigator from '@/components/TaskNavigator.vue'

export default {
  components: {
    DroneList,
    TaskForm,
    TaskNavigator
  }
}
</script>
