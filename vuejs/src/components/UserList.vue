<template>
  <div>
    <v-app>
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="6">
            <v-card>
              <v-card-title>
                <h1>User Data</h1>
              </v-card-title>
              <v-list>
                <v-list-item v-for="user in users" :key="user.id">
                  <v-list-item-content>
                    <v-list-item-title>
                      {{ user.name }}
                    </v-list-item-title>
                    <v-list-item-subtitle>
                      Age: {{ user.age }} | Sex: {{ user.sex }} | Designation: {{ user.designation }} | Department: {{ user.department }}
                    </v-list-item-subtitle>
                    <v-list-item-subtitle>
                      Address: {{ user.address }} | Phone: {{ user.phone }} | Blood Group: {{ user.bloodgroup }}
                    </v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>

            <!-- New User Form -->
            <v-card>
              <v-card-title>
                <h1>Create New User</h1>
              </v-card-title>
              <v-form @submit.prevent="createUser">
                <v-text-field v-model="newUser.name" label="Name"></v-text-field>
                <v-text-field v-model="newUser.age" label="Age"></v-text-field>
                <v-text-field v-model="newUser.sex" label="Sex"></v-text-field>
                <v-text-field v-model="newUser.designation" label="Designation"></v-text-field>
                <v-text-field v-model="newUser.address" label="Address"></v-text-field>
                <v-text-field v-model="newUser.phone" label="Phone"></v-text-field>
                <v-text-field v-model="newUser.bloodgroup" label="Blood Group"></v-text-field>
                <v-text-field v-model="newUser.department" label="Department"></v-text-field>
                <v-btn type="submit">Create User</v-btn>
              </v-form>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-app>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      users: [],
      newUser: {
        name: "",
        age: "",
        sex: "",
        designation: "",
        address: "",
        phone: "",
        bloodgroup: "",
        department: "",
      },
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
    async createUser() {
      try {
        const response = await axios.post("http://127.0.0.1:8000/users/", this.newUser);
        this.users.push(response.data);
        // Clear the form fields after successful creation
        this.newUser = {
          name: "",
          age: "",
          sex: "",
          designation: "",
          address: "",
          phone: "",
          bloodgroup: "",
          department: "",
        };
      } catch (error) {
        console.log("Error creating user:", error);
      }
    },
  },
};
</script>

<style>
/* You can add custom styles here if needed */
h1 {
  background-color: royalblue;
  color: black;
  height: 100%;
}

.v-list-item-title {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.v-list-item-subtitle {
  color: rgb(255, 153, 0);
}
</style>
