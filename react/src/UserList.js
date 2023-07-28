import React, { useState, useEffect } from "react";
import axios from "axios";
import { Container, Card, CardHeader, CardContent, List, ListItem, ListItemText, TextField, Button } from "@mui/material";

const App = () => {
  const [users, setUsers] = useState([]);
  const [newUser, setNewUser] = useState({
    name: "",
    age: "",
    sex: "",
    designation: "",
    address: "",
    phone: "",
    bloodgroup: "",
    department: "",
  });

  useEffect(() => {
    // Fetch user data from the backend API
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/users");
      setUsers(response.data);
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };

  const createUser = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/users/", newUser);
      setUsers([...users, response.data]);
      // Clear the form fields after successful creation
      setNewUser({
        name: "",
        age: "",
        sex: "",
        designation: "",
        address: "",
        phone: "",
        bloodgroup: "",
        department: "",
      });
    } catch (error) {
      console.log("Error creating user:", error);
    }
  };

  return (
    <Container>
      <Card>
        <CardHeader>
          <h1>User Data</h1>
        </CardHeader>
        <List>
          {users.map((user) => (
            <ListItem key={user.id}>
              <ListItemText
                primary={user.name}
                secondary={`Age: ${user.age} | Sex: ${user.sex} | Designation: ${user.designation} | Department: ${user.department}`}
              />
              <ListItemText
                secondary={`Address: ${user.address} | Phone: ${user.phone} | Blood Group: ${user.bloodgroup}`}
              />
            </ListItem>
          ))}
        </List>
      </Card>

      {/* New User Form */}
      <Card>
        <CardHeader>
          <h1>Create New User</h1>
        </CardHeader>
        <CardContent>
          <TextField
            label="Name"
            value={newUser.name}
            onChange={(e) => setNewUser({ ...newUser, name: e.target.value })}
          />
          <TextField
            label="Age"
            value={newUser.age}
            onChange={(e) => setNewUser({ ...newUser, age: e.target.value })}
          />
          <TextField
            label="Sex"
            value={newUser.sex}
            onChange={(e) => setNewUser({ ...newUser, sex: e.target.value })}
          />
          <TextField
            label="Designation"
            value={newUser.designation}
            onChange={(e) => setNewUser({ ...newUser, designation: e.target.value })}
          />
          <TextField
            label="Address"
            value={newUser.address}
            onChange={(e) => setNewUser({ ...newUser, address: e.target.value })}
          />
          <TextField
            label="Phone"
            value={newUser.phone}
            onChange={(e) => setNewUser({ ...newUser, phone: e.target.value })}
          />
          <TextField
            label="Blood Group"
            value={newUser.bloodgroup}
            onChange={(e) => setNewUser({ ...newUser, bloodgroup: e.target.value })}
          />
          <TextField
            label="Department"
            value={newUser.department}
            onChange={(e) => setNewUser({ ...newUser, department: e.target.value })}
          />
          <Button variant="contained" color="primary" onClick={createUser}>
            Create User
          </Button>
        </CardContent>
      </Card>
    </Container>
  );
};

export default App;
