<template>
  <div>
    <h1>User Data</h1>
    <ul>
      <li v-for="user in users" :key="user.id">User{{ user.name }}</li>
      <li v-for="user in users" :key="user.id">{{ user.age }}</li>
      <li v-for="user in users" :key="user.id">{{ user.sex }}</li>
      <li v-for="user in users" :key="user.id">{{ user.designation }}</li>
      <li v-for="user in users" :key="user.id">{{ user.address }}</li>
      <li v-for="user in users" :key="user.id">{{ user.phone }}</li>
      <li v-for="user in users" :key="user.id">{{ user.bloodgroup }}</li>
      <li v-for="user in users" :key="user.id">{{ user.department }}</li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      users: [],
    };
  },
  mounted() {
    // Fetch user data from the backend API
    this.fetchUsers();
  },
  methods: {
    async fetchUsers() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/users");
        this.users = response.data;
      } catch (error) {
        console.error("Error fetching users:", error);
      }
    },
  },
};
</script>
