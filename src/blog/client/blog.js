let accessToken = null;
let refreshToken = null;

async function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  try {
    const response = await fetch("http://127.0.0.1:8000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username, password }),
    });

    const data = await response.json();

    if (response.ok) {
      accessToken = data.access;
      refreshToken = data.refresh;
      alert("Login successful!");
    } else {
      alert("Login failed: " + (data.detail || "Unknown error"));
    }
  } catch (error) {
    console.error("Login error:", error);
    alert("Error during login.");
  }
}

async function createPost() {
  const title = document.getElementById("title").value;
  const content = document.getElementById("content").value;

  if (!accessToken) {
    alert("Please login first.");
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:8000/api/posts/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${accessToken}`,
      },
      body: JSON.stringify({ title, content }),
    });

    const data = await response.json();

    if (response.ok) {
      alert("Post created successfully!");
    } else {
      console.error("Create post error:", data);
      alert("Failed to create post: " + JSON.stringify(data));
    }
  } catch (error) {
    console.error("Create post exception:", error);
    alert("Error during post creation.");
  }
}
