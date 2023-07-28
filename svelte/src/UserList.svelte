<script>
    import { onMount } from "svelte";
    import axios from "axios";
  
    let users = [];
    let newUser = {
      name: "",
      age: "",
      sex: "",
      designation: "",
      address: "",
      phone: "",
      bloodgroup: "",
      department: "",
    };
  
    onMount(async () => {
      // Fetch user data from the backend API
      await fetchUsers();
    });
  
    async function fetchUsers() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/users");
        users = response.data;
      } catch (error) {
        console.error("Error fetching users:", error);
      }
    }
  
    async function createUser() {
      try {
        const response = await axios.post("http://127.0.0.1:8000/users/", newUser);
        users = [...users, response.data];
        // Clear the form fields after successful creation
        newUser = {
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
    }
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
  
  <div>
    <div>
      <h1>User Data</h1>
      <ul>
        {#each users as user}
          <li>
            <div>
              <h3>{user.name}</h3>
              <p>
                Age: {user.age} | Sex: {user.sex} | Designation: {user.designation} | Department: {user.department}
              </p>
              <p>
                Address: {user.address} | Phone: {user.phone} | Blood Group: {user.bloodgroup}
              </p>
            </div>
          </li>
        {/each}
      </ul>
    </div>
  
    <!-- New User Form -->
    <div>
      <h1>Create New User</h1>
      <form on:submit|preventDefault={createUser}>
        <input type="text" bind:value={newUser.name} placeholder="Name" />
        <input type="text" bind:value={newUser.age} placeholder="Age" />
        <input type="text" bind:value={newUser.sex} placeholder="Sex" />
        <input type="text" bind:value={newUser.designation} placeholder="Designation" />
        <input type="text" bind:value={newUser.address} placeholder="Address" />
        <input type="text" bind:value={newUser.phone} placeholder="Phone" />
        <input type="text" bind:value={newUser.bloodgroup} placeholder="Blood Group" />
        <input type="text" bind:value={newUser.department} placeholder="Department" />
        <button type="submit">Create User</button>
      </form>
    </div>
  </div>
  