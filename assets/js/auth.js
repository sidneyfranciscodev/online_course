import { auth } from "/assets/js/firebase.js";

export const register = (email, password) => auth.createUserWithEmailAndPassword(email, password);
export const login = (email, password) => auth.signInWithEmailAndPassword(email, password);
export const logout = () => auth.signOut();
export const authState = callback => auth.onAuthStateChanged(callback);