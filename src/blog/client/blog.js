let accessToken = null;
let refreshToken =null;

// Étape 1 : Connexion pour récupérer le token
async function loginAndCreatePost() {
  try {
    const response = await fetch("http://127.0.0.1:8000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username: "meda",
        password: "0000"
      })
    });
    const key = response.json()

    const token = await fetch("http://127.0.0.1:8000/api/blog/token/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username: "meda",
        password: "0000"
      })
    });

    const data = await token.json();
;

   /* if (!key.ok) {
      console.error("Erreur lors de la connexion :", key);
      alert("Échec de connexion : " + (key.detail || "Erreur inconnue"));
      return;
    }else{
      console.log(key)
    }*/

    accessToken = data.access;
    console.log("Token récupéré :", accessToken);
    createPost(accessToken);

  } catch (error) {
    console.error("Erreur lors de la connexion :", error);
    alert("Erreur réseau pendant la connexion.");
  }
}

// Étape 2 : Création du post
async function createPost(token) {
  // Récupère les données du formulaire
  const title = document.getElementById("title").value;
  const slug = document.getElementById("slug").value;
  const content = document.getElementById("content").value;
  const author = document.getElementById("author").value || null;
  const category = document.getElementById("category").value || null;
  const published = document.getElementById("published").checked;
  const postData = {
    title,
    slug,
    published,
    content,
    author: author ? parseInt(author) : null,
    category: category ? parseInt(category) : null
  };

  try {
    const response = await fetch("http://127.0.0.1:8000/api/blog/post/new/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      },
      body: JSON.stringify(postData)
    });

    const data = await response.json();

    if (!response.ok) {
      console.error("Erreur API :", data);
      alert("Erreur : " + JSON.stringify(data));
      return;
    }

    console.log("Post créé :", data);
    alert("Post créé avec succès !");
  } catch (error) {
    console.error("Erreur JS :", error);
    alert("Erreur lors de la requête.");
  }
}
