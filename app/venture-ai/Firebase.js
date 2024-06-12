// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyB1EwWgRznK3msEc1F3TO_fXQoiAPvUMtY",
  authDomain: "venture-ai-133a8.firebaseapp.com",
  projectId: "venture-ai-133a8",
  storageBucket: "venture-ai-133a8.appspot.com",
  messagingSenderId: "383096295514",
  appId: "1:383096295514:web:5176bcfca0ee22d1c04863",
  measurementId: "G-GJ2FP7NZ80"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
