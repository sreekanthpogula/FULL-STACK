<template>
  <v-app>
    <v-main>
      <UserList/>
    </v-main>
  </v-app>
</template>

<script>
import UserList from './components/UserList.vue'

export default {
  name: 'App',

  components: {
   UserList,
  },

  data: () => ({
    //
  }),
}
</script>
