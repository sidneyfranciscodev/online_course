import { Controller } from "/assets/js/lib/stimulus.js";
import { register, login, logout } from "/assets/js/auth.js";

export default class extends Controller {
  static targets = ["email", "password"];

  async register(event) {
    event.preventDefault();
    /* const email = this.emailTarget.value;
    const password = this.passwordTarget.value;
    const response = await register(email, password);
    console.log(response.user); */
  } 

  async login(event) {
    event.preventDefault();
    const email = this.emailTarget.value;
    const password = this.passwordTarget.value;

    try {
      const request = await login(email, password);
      const idToken = await request.user.getIdToken();

      const res = await this.request(
        "/auth/session",
        "POST",
        {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${idToken}`,
        },
      );
      
      if (!res) throw Error('error')

      if (res.status === 200) {
        window.location.assign("/admin/dashboard");
      }   
    } catch (err) {
      console.error(err);
      alert("Login Failed: " + err.message);
    }
  }

  async logout(event) {
    event.preventDefault();
    await this.request(
      "/auth/logout",
      "POST",
      { "Content-Type": "application/json" },
    );
    await logout();
    window.location.href = "/";
  }

  async request(url, method, headers, body={}) {
    try {
      const response = await fetch(url, {
        method: method,
        headers: headers,
        body: JSON.stringify(body),
      });

      if (!response.ok) {
        throw new Error("Request Failed");
      }
      return await response.json();
    } catch (err) {
      alert(err);
    }
  }
}
