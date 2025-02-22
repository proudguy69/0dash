<template>
    {{user_data}}
    ===========================================
    
    <div class="" v-for="guild in guild_data">
        {{guild.name}} | {{ guild.approximate_member_count }}
    </div>
    
</template>

<script setup>
import { inject, onMounted, ref, watch } from 'vue';


const session_data = inject('session_data')
const user_data = ref({})
const guild_data = ref({})



async function getUserData() {
    if (!session_data.value.session_data) {return}
    const headers = {"Authorization": `Bearer ${session_data.value.session_data.access_token}`}
    const response = await fetch('https://discord.com/api/v10/users/@me', {headers: headers})
    const response_json = await response.json()
    return response_json
}

async function getUserGuilds() {
    if (!session_data.value.session_data) {return}
    const headers = {"Authorization": `Bearer ${session_data.value.session_data.access_token}`}
    const response = await fetch('https://discord.com/api/v10/users/@me/guilds?with_counts=true', {headers: headers})
    const response_json = await response.json()
    return response_json
}

async function loadPageData() {
    user_data.value = await getUserData()
    guild_data.value = await getUserGuilds()
}

// on first page load
onMounted(async () => {
    await loadPageData()
})

// on page reload (only App.vue is reloaded, so its on_mount gets called, but not ours) [thats a lie, yes ours gets called but session_data isnt loaded cus it waits on the api call, so session_data isnt populated until AFTER our on_mounted is called]
watch(session_data, async (_) => {
    await loadPageData()
})



</script>

<style>

</style>