import "/assets/js/vendor/firebase/firebase-app-compat.js";
import "/assets/js/vendor/firebase/firebase-auth-compat.js";

const firebaseConfig = {
  apiKey: "AIzaSyACxVc5eViG64XgUo73lrK-QR-q5IHfFkg",
  authDomain: "direitomoz.firebaseapp.com",
  projectId: "direitomoz",
  storageBucket: "direitomoz.firebasestorage.app",
  messagingSenderId: "249964127314",
  appId: "1:249964127314:web:22740005ac8e1663abeb8b",
  measurementId: "G-65V876HNKH"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
export const auth = firebase.auth();