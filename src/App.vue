<template>
  <router-view></router-view>
</template>

<script setup>
import { onMounted, provide, ref } from 'vue';



//get authorization data
const session_data = ref({})


async function getSession() {
    const response = await fetch('/api/get/session')
    const response_json = await response.json()
    return response_json
}

// on first load
onMounted(async ()=> {
    session_data.value = await  getSession()
})


provide('session_data',session_data)
</script>

<style>

</style>